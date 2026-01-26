#!/usr/bin/env python3
"""
Final verification test script for Safe Roads project.
Tests backend imports, predictions, and overall functionality.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

def test_backend_imports():
    """Test that all backend modules can be imported."""
    print("Testing backend imports...")

    try:
        from backend.app import app
        print("✅ Backend app imported successfully")
        print(f"   Routes: {len(app.routes)}")

        from backend.services.model_service import predict_probability
        print("✅ Model service imported successfully")

        from backend.models.schemas import PredictRequest, ModelResult
        print("✅ Schemas imported successfully")

        from backend.config import settings
        print("✅ Config imported successfully")

        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_prediction_functionality():
    """Test the prediction functionality."""
    print("\nTesting prediction functionality...")

    try:
        from backend.services.model_service import predict_probability

        # Test basic prediction
        result = predict_probability({
            'road_type': 'urban',
            'weather': 'clear',
            'time_of_day': 'day',
            'lighting': 'daylight',
            'junction': 'no_junction',
            'road_surface': 'dry'
        })

        # Validate result structure
        required_keys = {'probability', 'risk_percent', 'breakdown'}
        if not set(result.keys()) == required_keys:
            print(f"❌ Missing keys in result: {result.keys()}")
            return False

        if not isinstance(result['probability'], (int, float)):
            print(f"❌ Probability not numeric: {result['probability']}")
            return False

        if not isinstance(result['risk_percent'], int):
            print(f"❌ Risk percent not int: {result['risk_percent']}")
            return False

        if not isinstance(result['breakdown'], list):
            print(f"❌ Breakdown not list: {result['breakdown']}")
            return False

        print("✅ Prediction test successful")
        print(f"   Result: probability={result['probability']:.3f}, risk_percent={result['risk_percent']}%")
        print(f"   Breakdown items: {len(result['breakdown'])}")

        return True
    except Exception as e:
        print(f"❌ Prediction error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_schema_validation():
    """Test Pydantic schema validation."""
    print("\nTesting schema validation...")

    try:
        from backend.models.schemas import PredictRequest, ModelResult
        from backend.services.model_service import predict_probability

        # Test valid input
        valid_input = {
            'road_type': 'urban',
            'weather': 'clear',
            'time_of_day': 'day',
            'lighting': 'daylight',
            'junction': 'no_junction',
            'road_surface': 'dry'
        }

        request = PredictRequest(**valid_input)
        print("✅ Valid input accepted")

        # Test prediction with validated input
        payload = request.model_dump(mode="json")
        result = predict_probability(payload)
        response = ModelResult(**result)
        print("✅ Response validation successful")

        return True
    except Exception as e:
        print(f"❌ Schema validation error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_frontend_files():
    """Test that frontend files exist and are readable."""
    print("\nTesting frontend files...")

    frontend_files = ['frontend/index.html', 'frontend/script.js', 'frontend/style.css']

    for file_path in frontend_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if len(content) > 0:
                        print(f"✅ {file_path} exists and readable ({len(content)} chars)")
                    else:
                        print(f"❌ {file_path} is empty")
                        return False
            except Exception as e:
                print(f"❌ Error reading {file_path}: {e}")
                return False
        else:
            print(f"❌ {file_path} not found")
            return False

    return True

def main():
    """Run all verification tests."""
    print("🔍 Safe Roads Project - Final Verification")
    print("=" * 50)

    tests = [
        test_backend_imports,
        test_prediction_functionality,
        test_schema_validation,
        test_frontend_files
    ]

    results = []
    for test in tests:
        results.append(test())

    print("\n" + "=" * 50)
    print("📊 VERIFICATION RESULTS")

    passed = sum(results)
    total = len(results)

    for i, (test, result) in enumerate(zip(tests, results)):
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test.__name__}")

    print(f"\nOverall: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All verification tests passed! Project is ready for submission.")
        return 0
    else:
        print("⚠️  Some tests failed. Please review and fix issues.")
        return 1

if __name__ == "__main__":
    sys.exit(main())