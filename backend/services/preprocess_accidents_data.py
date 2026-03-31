"""
Preprocessing Pipeline for Accidents Dataset
Demonstrates how to use the data_mapper module to prepare data for model training.

Usage:
    python preprocess_accidents_data.py --input data/accidents_raw_master.csv --output data/accidents_processed.pkl
"""

import pandas as pd
import numpy as np
import pickle
import argparse
from pathlib import Path
import sys

# Add backend to path if running standalone
sys.path.insert(0, str(Path(__file__).parent))

from data_mapper import (
    engineer_road_structure,
    preprocess_dataset,
    FEATURE_CONFIG,
)


def load_raw_dataset(filepath: str) -> pd.DataFrame:
    """
    Load the raw accidents dataset from CSV.
    
    Args:
        filepath: Path to CSV file
    
    Returns:
        DataFrame with raw data
    """
    print(f"Loading dataset from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {len(df.columns)}")
    return df


def analyze_features(df: pd.DataFrame, features: list = None) -> None:
    """
    Print analysis of feature distributions and missing values.
    
    Args:
        df: Input DataFrame
        features: List of features to analyze (default: all)
    """
    if features is None:
        features = df.columns.tolist()
    
    print("\nFeature Analysis:")
    print("-" * 80)
    
    for feature in features[:10]:  # Show first 10 for brevity
        if feature not in df.columns:
            print(f"{feature:20s}: NOT IN DATASET")
            continue
        
        col = df[feature]
        n_missing = col.isna().sum()
        n_unique = col.nunique()
        dtype = col.dtype
        
        print(f"{feature:20s}: {dtype.__name__:10s} | Missing: {n_missing:5d} | Unique: {n_unique:5d}")
        
        if n_unique <= 10 and dtype == 'object':
            print(f"  {'':20s}  Values: {col.unique()[:5].tolist()}")
    
    if len(features) > 10:
        print(f"  ... and {len(features) - 10} more features")


def check_feature_availability(df: pd.DataFrame) -> tuple:
    """
    Check which of the 16 required features are available in the dataset.
    
    Returns:
        (available_features, missing_features)
    """
    required_features = [
        'SHAA', 'HODESH_TEUNA', 'YOM_BASHAVUA', 'SUG_TEUNA',
        'ROAD_STRUCTURE', 'ROHAV', 'NAFA', 'ZURAT_ISHUV',
        'MEHIRUT_MUTERET', 'TEURA', 'SUG_DEREH', 'SIMUN_TIMRUR',
        'MEKOM_HAZIYA', 'TKINUT', 'OFEN_HAZIYA', 'PNE_KVISH'
    ]
    
    available = [f for f in required_features if f in df.columns]
    missing = [f for f in required_features if f not in df.columns]
    
    # ROAD_STRUCTURE is engineered, so check if components exist
    if 'ROAD_STRUCTURE' not in df.columns:
        if 'HAD_MASLUL' in df.columns or 'RAV_MASLUL' in df.columns:
            available.append('ROAD_STRUCTURE')
            if 'ROAD_STRUCTURE' in missing:
                missing.remove('ROAD_STRUCTURE')
    
    return available, missing


def prepare_dataset_for_model(
    input_path: str,
    output_path: str,
    target_column: str = "NIKVIYUT_TEUNA"
) -> pd.DataFrame:
    """
    Complete preprocessing pipeline: load, engineer, validate, and save dataset.
    
    Args:
        input_path: Path to raw CSV
        output_path: Path to save processed pickle
        target_column: Name of target column (accident severity)
    
    Returns:
        Processed DataFrame
    """
    # Step 1: Load
    df_raw = load_raw_dataset(input_path)
    print(f"\nOriginal dataset size: {df_raw.shape[0]} rows × {df_raw.shape[1]} columns")
    
    # Step 2: Check features
    available, missing = check_feature_availability(df_raw)
    print(f"\n✓ Available features: {len(available)}/16")
    print(f"✗ Missing features: {len(missing)}")
    if missing:
        print(f"  {missing}")
    
    # Step 3: Analyze
    print("\nAnalyzing raw features...")
    analyze_features(df_raw)
    
    # Step 4: Preprocess
    print("\nPreprocessing dataset...")
    df_processed = preprocess_dataset(df_raw, target_column=target_column)
    print(f"  ✓ Processed size: {df_processed.shape[0]} rows × {df_processed.shape[1]} columns")
    print(f"  ✓ Removed {df_raw.shape[0] - df_processed.shape[0]} incomplete rows")
    
    # Step 5: Validate
    print("\nData validation:")
    for col in available:
        if col in df_processed.columns:
            unique_vals = df_processed[col].nunique()
            print(f"  {col:20s}: {unique_vals} unique values")
    
    # Step 6: Save
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'wb') as f:
        pickle.dump(df_processed, f)
    
    print(f"\n✓ Saved to {output_path}")
    print(f"  File size: {output_path.stat().st_size / 1024:.2f} KB")
    
    return df_processed


def generate_feature_mapping_report(output_path: str = "data/FEATURE_MAPPINGS.txt") -> None:
    """
    Generate a human-readable report of all feature mappings for documentation.
    
    Args:
        output_path: Where to save the report
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("FEATURE MAPPINGS REPORT\n")
        f.write("Frontend (Hebrew) → Backend (Integer Codes)\n")
        f.write("=" * 80 + "\n\n")
        
        for feature_name, config in FEATURE_CONFIG.items():
            f.write(f"\n{feature_name}\n")
            f.write(f"Description: {config['description']}\n")
            f.write(f"Type: {config['type']}\n")
            f.write("-" * 60 + "\n")
            
            mapping = config['mapping']
            for text, code in sorted(mapping.items(), key=lambda x: x[1]):
                f.write(f"  {code:2d}  ←  {text}\n")
        
        f.write("\n" + "=" * 80 + "\n")
        f.write("END OF REPORT\n")
        f.write("=" * 80 + "\n")
    
    print(f"\n✓ Feature mapping report saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Preprocess accidents dataset for model training"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="data/accidents_raw_master.csv",
        help="Path to raw CSV file"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/accidents_processed.pkl",
        help="Path to save processed pickle file"
    )
    parser.add_argument(
        "--target",
        type=str,
        default="NIKVIYUT_TEUNA",
        help="Target column name"
    )
    parser.add_argument(
        "--report",
        type=str,
        default="data/FEATURE_MAPPINGS.txt",
        help="Save feature mapping report"
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Don't save processed data"
    )
    
    args = parser.parse_args()
    
    # Check if input exists
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}")
        sys.exit(1)
    
    # Run preprocessing
    try:
        df_processed = prepare_dataset_for_model(
            str(input_path),
            args.output,
            args.target
        )
        
        # Generate report
        generate_feature_mapping_report(args.report)
        
        print("\n✓ Preprocessing complete!")
        print(f"  Processed data shape: {df_processed.shape}")
        
    except Exception as e:
        print(f"\nERROR during preprocessing: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
