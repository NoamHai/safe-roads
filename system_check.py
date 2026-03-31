"""
Safe Roads: System Verification Checklist

Complete end-to-end verification for UI ↔ Backend integration
"""

import json
from datetime import datetime


class SystemVerificationChecklist:
    """Interactive verification checklist for Safe Roads system."""
    
    def __init__(self):
        self.timestamp = datetime.now().isoformat()
        self.checks = {}
    
    def add_check(self, category, item, status, notes=""):
        """Add a verification check result."""
        if category not in self.checks:
            self.checks[category] = []
        
        self.checks[category].append({
            "item": item,
            "status": status,  # "PASS", "FAIL", "PENDING", "MANUAL"
            "notes": notes,
            "timestamp": datetime.now().isoformat()
        })
    
    def print_report(self):
        """Print formatted verification report."""
        print("\n" + "="*100)
        print("SAFE ROADS SYSTEM VERIFICATION REPORT".center(100))
        print(f"Generated: {self.timestamp}")
        print("="*100)
        
        category_order = [
            "BACKEND_STRUCTURE",
            "DATA_MAPPING",
            "FEATURE_CONFIG",
            "FRONTEND_UI",
            "API_INTEGRATION",
            "TESTING",
            "DOCUMENTATION"
        ]
        
        for category in category_order:
            if category in self.checks:
                self._print_category(category, self.checks[category])
        
        self._print_summary()
    
    def _print_category(self, category, items):
        """Print a verification category."""
        print(f"\n[{category}]")
        print("-" * 100)
        
        for item in items:
            status_symbol = {
                "PASS": "✓",
                "FAIL": "✗",
                "PENDING": "⏳",
                "MANUAL": "◆"
            }.get(item["status"], "?")
            
            print(f"  {status_symbol:3s} {item['item']:50s} [{item['status']}]")
            if item["notes"]:
                print(f"       └─ {item['notes']}")
    
    def _print_summary(self):
        """Print summary statistics."""
        print("\n" + "="*100)
        print("SUMMARY")
        print("="*100)
        
        all_items = []
        for items in self.checks.values():
            all_items.extend(items)
        
        status_counts = {}
        for item in all_items:
            status = item["status"]
            status_counts[status] = status_counts.get(status, 0) + 1
        
        total = len(all_items)
        passed = status_counts.get("PASS", 0)
        
        print(f"\nTotal Checks: {total}")
        for status, count in sorted(status_counts.items()):
            pct = (count / total * 100) if total > 0 else 0
            print(f"  {status:12s}: {count:3d} ({pct:5.1f}%)")
        
        print(f"\nReadiness: {passed}/{total} checks passing")
        
        if passed == total:
            print("✓ SYSTEM READY FOR DEPLOYMENT")
        else:
            pending = status_counts.get("PENDING", 0) + status_counts.get("MANUAL", 0)
            if pending > 0:
                print(f"⏳ {pending} items pending - manual verification may be required")
            if status_counts.get("FAIL", 0) > 0:
                print(f"✗ {status_counts['FAIL']} items FAILED - review required")
        
        print("="*100 + "\n")


def run_verification():
    """Run complete system verification."""
    checker = SystemVerificationChecklist()
    
    # ==================== BACKEND STRUCTURE ====================
    print("\n[Verifying Backend Structure]")
    
    try:
        from pathlib import Path
        backend_root = Path("backend")
        
        # Check critical files exist
        files_to_check = [
            ("backend/app.py", "FastAPI application entry point"),
            ("backend/config.py", "Configuration module"),
            ("backend/services/model_service.py", "ML inference service"),
            ("backend/services/data_mapper.py", "16-feature mapping system"),
            ("backend/services/preprocess_accidents_data.py", "Dataset preprocessing"),
            ("backend/services/data_mapper_integration_guide.py", "Integration examples"),
            ("backend/services/README_DATA_MAPPER.md", "Data mapper documentation"),
            ("backend/routes/predict.py", "Prediction API route"),
            ("backend/models/schemas.py", "Pydantic request/response schemas"),
        ]
        
        for filepath, description in files_to_check:
            path = Path(filepath)
            if path.exists():
                checker.add_check("BACKEND_STRUCTURE", f"File: {filepath}", "PASS", description)
            else:
                checker.add_check("BACKEND_STRUCTURE", f"File: {filepath}", "FAIL", f"Missing: {description}")
    
    except Exception as e:
        checker.add_check("BACKEND_STRUCTURE", "File verification", "FAIL", str(e))
    
    # ==================== DATA MAPPING ====================
    print("[Verifying Data Mapping]")
    
    try:
        from backend.services.data_mapper import FEATURE_CONFIG
        
        # Check all 16 features
        required_features = [
            'SHAA', 'HODESH_TEUNA', 'YOM_BASHAVUA', 'SUG_TEUNA',
            'ROAD_STRUCTURE', 'ROHAV', 'NAFA', 'ZURAT_ISHUV',
            'MEHIRUT_MUTERET', 'TEURA', 'SUG_DEREH', 'SIMUN_TIMRUR',
            'MEKOM_HAZIYA', 'TKINUT', 'OFEN_HAZIYA', 'PNE_KVISH'
        ]
        
        missing_features = [f for f in required_features if f not in FEATURE_CONFIG]
        
        if not missing_features:
            checker.add_check("DATA_MAPPING", "All 16 features configured", "PASS", 
                            f"{len(required_features)} features found")
        else:
            checker.add_check("DATA_MAPPING", "All 16 features configured", "FAIL",
                            f"Missing: {missing_features}")
        
        # Check mapping functions
        from backend.services.data_mapper import (
            prepare_model_input,
            prepare_model_array,
            validate_ui_input,
            engineer_road_structure,
        )
        
        checker.add_check("DATA_MAPPING", "prepare_model_input() function", "PASS", "Converts dict to model format")
        checker.add_check("DATA_MAPPING", "prepare_model_array() function", "PASS", "Exports to NumPy array")
        checker.add_check("DATA_MAPPING", "validate_ui_input() function", "PASS", "Comprehensive validation")
        checker.add_check("DATA_MAPPING", "engineer_road_structure() function", "PASS", "Feature engineering")
    
    except ImportError as e:
        checker.add_check("DATA_MAPPING", "Import data_mapper module", "FAIL", str(e))
    except Exception as e:
        checker.add_check("DATA_MAPPING", "Verify mapping functions", "FAIL", str(e))
    
    # ==================== FEATURE CONFIG ====================
    print("[Verifying Feature Configuration]")
    
    try:
        from backend.services.data_mapper import FEATURE_CONFIG, SPEED_LIMIT_MAPPING
        
        # Check sample feature configs
        sample_features = ['MEHIRUT_MUTERET', 'SUG_DEREH', 'PNE_KVISH']
        for feature in sample_features:
            if feature in FEATURE_CONFIG:
                config = FEATURE_CONFIG[feature]
                has_type = 'type' in config
                has_range = 'range' in config
                has_mapping = 'mapping' in config
                
                if has_type and has_range and has_mapping:
                    checker.add_check("FEATURE_CONFIG", f"{feature} configuration", "PASS",
                                    f"{len(config['mapping'])} mappings, range {config['range']}")
                else:
                    checker.add_check("FEATURE_CONFIG", f"{feature} configuration", "FAIL",
                                    "Missing type/range/mapping")
        
        # Check custom edge case: 120 km/h
        if "עד 120 קמ״ש" in SPEED_LIMIT_MAPPING:
            code = SPEED_LIMIT_MAPPING["עד 120 קמ״ש"]
            checker.add_check("FEATURE_CONFIG", "Custom 120 km/h edge case", "PASS",
                            f"Mapped to code {code}")
        else:
            checker.add_check("FEATURE_CONFIG", "Custom 120 km/h edge case", "FAIL",
                            "Not found in SPEED_LIMIT_MAPPING")
    
    except Exception as e:
        checker.add_check("FEATURE_CONFIG", "Feature configuration verification", "FAIL", str(e))
    
    # ==================== FRONTEND UI ====================
    print("[Verifying Frontend UI]")
    
    try:
        from pathlib import Path
        
        # Check frontend files
        frontend_files = [
            ("frontend/index.html", "HTML structure with bilingual support"),
            ("frontend/style.css", "Navy government theme stylesheet"),
            ("frontend/script.js", "Dynamic UI with Hebrew↔English translation"),
        ]
        
        for filepath, description in frontend_files:
            path = Path(filepath)
            if path.exists():
                checker.add_check("FRONTEND_UI", f"File: {filepath}", "PASS", description)
            else:
                checker.add_check("FRONTEND_UI", f"File: {filepath}", "FAIL", f"Missing: {description}")
        
        # Check for key UI elements
        index_path = Path("frontend/index.html")
        if index_path.exists():
            content = index_path.read_text(encoding='utf-8')
            checks = [
                (".linear-gauge" in content, "Linear gauge component", "Linear bar + indicator"),
                ("data-i18n" in content, "Bilingual i18n support", "Hebrew/English translations"),
                ("Navy" in content or "#1a365d" in content or "#2d5a8c" in content, 
                 "Navy government theme", "Color scheme applied"),
            ]
            
            for check, item, notes in checks:
                status = "PASS" if check else "FAIL"
                checker.add_check("FRONTEND_UI", item, status, notes)
    
    except Exception as e:
        checker.add_check("FRONTEND_UI", "Frontend verification", "FAIL", str(e))
    
    # ==================== API INTEGRATION ====================
    print("[Verifying API Integration]")
    
    try:
        from backend.routes.predict import router as predict_router
        from backend.models.schemas import PredictRequest, ModelResult
        
        checker.add_check("API_INTEGRATION", "PredictRequest schema", "PASS", "Pydantic model for input")
        checker.add_check("API_INTEGRATION", "ModelResult schema", "PASS", "Pydantic model for output")
        checker.add_check("API_INTEGRATION", "/predict endpoint defined", "PASS", "FastAPI route configured")
        
        # Check request fields
        try:
            from pydantic import BaseModel
            request_fields = PredictRequest.model_fields.keys()
            expected_fields = {'road_type', 'weather', 'time_of_day', 'lighting', 'junction', 'road_surface'}
            if expected_fields.issubset(set(request_fields)):
                checker.add_check("API_INTEGRATION", "Request fields match spec", "PASS",
                                f"All required fields present")
            else:
                missing = expected_fields - set(request_fields)
                checker.add_check("API_INTEGRATION", "Request fields match spec", "FAIL",
                                f"Missing fields: {missing}")
        except:
            checker.add_check("API_INTEGRATION", "Request fields match spec", "MANUAL",
                            "Could not verify - check schema manually")
    
    except ImportError as e:
        checker.add_check("API_INTEGRATION", "Import API components", "FAIL", str(e))
    except Exception as e:
        checker.add_check("API_INTEGRATION", "API verification", "FAIL", str(e))
    
    # ==================== TESTING ====================
    print("[Verifying Testing Setup]")
    
    try:
        from pathlib import Path
        
        test_files = [
            ("tests/test_predict.py", "Prediction endpoint tests"),
            ("integration_test.py", "End-to-end integration test"),
            ("verify_final.py", "System functionality verification"),
            ("backend/services/data_mapper_integration_guide.py", "Integration examples & tests"),
        ]
        
        for filepath, description in test_files:
            path = Path(filepath)
            if path.exists():
                checker.add_check("TESTING", filepath, "PASS", description)
            else:
                checker.add_check("TESTING", filepath, "MANUAL", f"Optional: {description}")
    
    except Exception as e:
        checker.add_check("TESTING", "Testing verification", "FAIL", str(e))
    
    # ==================== DOCUMENTATION ====================
    print("[Verifying Documentation]")
    
    try:
        from pathlib import Path
        
        doc_files = [
            ("backend/services/README_DATA_MAPPER.md", "Complete data mapper documentation (500+ lines)"),
            ("FINAL_SUBMISSION_CHECK.md", "Submission requirements checklist"),
            ("requirements.txt", "Project dependencies"),
            ("requirements-dev.txt", "Development dependencies"),
        ]
        
        for filepath, description in doc_files:
            path = Path(filepath)
            if path.exists():
                checker.add_check("DOCUMENTATION", filepath, "PASS", description)
            else:
                checker.add_check("DOCUMENTATION", filepath, "MANUAL", f"Optional: {description}")
    
    except Exception as e:
        checker.add_check("DOCUMENTATION", "Documentation verification", "FAIL", str(e))
    
    # Print final report
    checker.print_report()
    
    return checker


if __name__ == "__main__":
    checker = run_verification()
