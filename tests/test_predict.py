"""
Tests for Safe Roads backend prediction preprocessing and output contract.
"""

from backend.services.model_service import predict_probability


class TestPredictOutputStructure:
    def test_output_keys(self):
        input_data = {
            "hour": 8,
            "month": 5,
            "accident_type": 1,
            "speed_limit": 3,
        }

        result = predict_probability(input_data)

        assert set(result.keys()) == {"probability", "risk_percent", "breakdown"}

    def test_output_types(self):
        input_data = {
            "hour": 12,
            "month": 7,
            "accident_type": "2",
            "speed_limit": "4",
        }

        result = predict_probability(input_data)

        assert isinstance(result["probability"], (int, float))
        assert isinstance(result["risk_percent"], int)
        assert isinstance(result["breakdown"], list)
        assert 0.0 <= result["probability"] <= 1.0
        assert 0 <= result["risk_percent"] <= 100


class TestPreprocessingAndEncoding:
    def test_accepts_numeric_and_string_encoded_values(self):
        numeric_payload = {
            "hour": 10,
            "month": 6,
            "accident_type": 1,
            "speed_limit": 2,
        }
        string_payload = {
            "hour": "10",
            "month": "6",
            "accident_type": "1",
            "speed_limit": "2",
        }

        result_numeric = predict_probability(numeric_payload)
        result_string = predict_probability(string_payload)

        assert result_numeric["probability"] == result_string["probability"]
        assert result_numeric["risk_percent"] == result_string["risk_percent"]

    def test_optional_district_is_accepted(self):
        input_data = {
            "hour": 20,
            "month": 12,
            "accident_type": 2,
            "speed_limit": 5,
            "district": 7,
        }

        result = predict_probability(input_data)

        factors = {item["factor"] for item in result["breakdown"]}
        assert "district" in factors

    def test_breakdown_contains_prepared_features(self):
        input_data = {
            "hour": 3,
            "month": 1,
            "accident_type": 4,
            "speed_limit": 6,
        }

        result = predict_probability(input_data)
        factors = {item["factor"] for item in result["breakdown"]}

        assert {"hour", "month", "accident_type", "speed_limit"}.issubset(factors)


class TestValidationBehavior:
    def test_invalid_non_numeric_encoded_value_raises(self):
        input_data = {
            "hour": 8,
            "month": 5,
            "accident_type": "not_encoded",
            "speed_limit": 2,
        }

        try:
            predict_probability(input_data)
            assert False, "Expected ValueError for invalid encoded value"
        except ValueError:
            assert True

    def test_invalid_hour_range_raises(self):
        input_data = {
            "hour": 99,
            "month": 5,
            "accident_type": 1,
            "speed_limit": 2,
        }

        try:
            predict_probability(input_data)
            assert False, "Expected ValueError for invalid hour range"
        except ValueError:
            assert True


class TestConsistency:
    def test_same_input_same_output(self):
        input_data = {
            "hour": 18,
            "month": 9,
            "accident_type": 3,
            "speed_limit": 4,
        }

        result1 = predict_probability(input_data)
        result2 = predict_probability(input_data)

        assert result1["probability"] == result2["probability"]
        assert result1["risk_percent"] == result2["risk_percent"]
        assert result1["breakdown"] == result2["breakdown"]
