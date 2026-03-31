# Data Preparation Plan — Safe Roads Project

## Inspection Summary

- **Dataset**: `data/accidents_raw_master.csv` contains ~66,894 rows of accident data with 52 columns (mixed Hebrew/English headers).
- **Key Columns Identified** (based on header and sample rows):
  - `pk_teuna_fikt`: Accident ID (unique identifier).
  - `SUG_DEREH`: Road type (e.g., 1=urban, 2=rural, 3=highway).
  - `TEURA`: Weather conditions (e.g., 1=clear, 2=rain, 3=fog).
  - `YOM_LAYLA`: Time of day (1=day, 5=night).
  - `OFEN_HAZIYA`: Lighting conditions (e.g., 1=daylight, 2=streetlights, 3=no lights).
  - `HAD_MASLUL`: Junction presence (0=no, 1=yes).
  - `SIMUN_TIMRUR`: Road surface (e.g., 1=dry, 2=wet, 3=unknown).
  - Other: Location (X,Y, SEMEL_YISHUV), severity (HUMRAT_TEUNA), date/time (SHNAT_TEUNA, HODESH_TEUNA, SHAA), etc.
- **Data Dictionary**: `data/data-dictionary-document-accidents.xlsx` (Excel file) provides descriptions and allowed values for columns (referenced in `tools/accidents_analysis.py` for parsing).
- **Current Model Alignment**: The existing rule-based model in `backend/services/model_service.py` uses simplified inputs matching frontend enums. The CSV has richer data that can enhance prediction.

## Proposed Relevant Features for Accident Risk Prediction

Focus on features directly influencing accident risk, aligned with the current model's inputs (road_type, weather, time_of_day, lighting, junction, road_surface). Select features with clear predictive value and availability in the dataset.

- **Road Type** (`SUG_DEREH`): Categorical (1=urban, 2=interurban, 3=highway, etc.). Relevant as highways have higher speeds/risks.
- **Weather** (`TEURA`): Categorical (1=clear, 2=rain, 3=fog, etc.). Directly affects visibility and traction.
- **Time of Day** (`YOM_LAYLA`): Binary/categorical (1=day, 5=night). Night increases risk due to visibility.
- **Lighting** (`OFEN_HAZIYA`): Categorical (1=daylight, 2=streetlights, 3=no streetlights). Critical for night accidents.
- **Junction** (`HAD_MASLUL`): Binary (0=no junction, 1=junction). Junctions add conflict points.
- **Road Surface** (`SIMUN_TIMRUR`): Categorical (1=dry, 2=wet, 3=icy, etc.). Wet surfaces reduce grip.
- **Additional Relevant**:
  - `HUMRAT_TEUNA`: Accident severity (1=fatal, 2=severe, 3=light) — for supervised learning targets.
  - `SHAA`: Hour of day (numeric) — finer granularity than YOM_LAYLA.
  - `YOM_BASHAVUA`: Day of week (1-7) — weekends may have different patterns.
  - `THUM_GEOGRAFI`: Geographic region — could indicate urban/rural density.

These features map closely to the frontend inputs and can be used to train an ML model replacing the rule-based one.

## Features to Discard

Discard features that are irrelevant, redundant, or not predictive for risk modeling. Avoid data leakage (e.g., post-accident details).

- **Identifiers/Keys**: `pk_teuna_fikt`, `YEHIDA` (reporting unit) — unique IDs, no predictive value.
- **Location Coordinates**: `X`, `Y` — precise GPS; use aggregated `SEMEL_YISHUV` (municipality code) if needed for regional analysis.
- **Redundant Time**: `SHNAT_TEUNA`, `HODESH_TEUNA` — year/month; use `SHAA` or derived features.
- **Post-Accident Details**: `SUG_TEUNA` (accident type), `RAV_MASLUL` (multi-lane), `MEHIRUT_MUTERET` (speed limit) — may correlate but risk reverse causality.
- **Low Relevance**: `REHOV1`, `REHOV2`, `BAYIT` (street/building numbers) — too granular; `ZOMET_IRONI`, `KVISH1/2` (road markers) — specific to location.
- **Other**: `STATUS_IGUN` (approval status), `YEAR` (duplicate of SHNAT_TEUNA).

## Necessary Preprocessing Steps

1. **Data Loading and Initial Cleaning**:
   - Load CSV with `pandas` (low_memory=False to handle mixed types).
   - Drop discarded columns.
   - Handle missing values: Use `AccidentsAnalyzer` from `tools/accidents_analysis.py` to analyze nulls; fill categoricals with mode, numerics with median, or drop rows if <5% missing.

2. **Encoding Categorical Features**:
   - Map enums to match frontend (e.g., `SUG_DEREH` 1→"urban", 3→"highway").
   - Use label encoding or one-hot for ML (e.g., pd.get_dummies for weather).
   - Ensure consistency with `backend/app.py` enums.

3. **Normalization/Feature Engineering**:
   - For numerics like `SHAA` (hour), normalize to 0-1 or use cyclical encoding (sin/cos for time).
   - Derive features: e.g., `is_weekend` from `YOM_BASHAVUA`.
   - Cap outliers if any (e.g., extreme coordinates).

4. **Handling Imbalances and Validation**:
   - Check class distribution (e.g., severity levels) — accidents are rare, so balance with SMOTE or undersampling.
   - Split train/val/test (e.g., 70/15/15) by time to avoid leakage.
   - Validate against data dictionary for allowed values.

5. **Integration with Model**:
   - Ensure preprocessed features match `predict_probability` input dict.
   - Test with sample data to confirm no NaN/encoding issues.

This plan prepares the data for ML model training, replacing the rule-based stub while preserving API compatibility.