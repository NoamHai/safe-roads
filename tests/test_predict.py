"""
Tests for the Safe Roads backend predict functionality.
Tests work with rule-based fallback (no ML model required).
"""

import pytest
from typing import Dict, Any, List

# Import the predict function
from backend.services.model_service import predict_probability


class TestPredictOutputStructure:
    """Test that predict_probability returns correct output structure."""

    def test_output_keys(self):
        """Test that output contains required keys."""
        input_data = {
            "road_type": "urban",
            "weather": "clear",
            "time_of_day": "day",
            "lighting": "daylight",
            "junction": "no_junction",
            "road_surface": "dry"
        }

        result = predict_probability(input_data)

        required_keys = {"probability", "risk_percent", "breakdown"}
        assert set(result.keys()) == required_keys

    def test_output_types(self):
        """Test that output values have correct types."""
        input_data = {
            "road_type": "urban",
            "weather": "clear",
            "time_of_day": "day",
            "lighting": "daylight",
            "junction": "no_junction",
            "road_surface": "dry"
        }

        result = predict_probability(input_data)

        # Check types
        assert isinstance(result["probability"], (int, float))
        assert isinstance(result["risk_percent"], int)
        assert isinstance(result["breakdown"], list)

        # Check probability range
        assert 0.0 <= result["probability"] <= 1.0

        # Check risk_percent range
        assert 0 <= result["risk_percent"] <= 100

        # Check breakdown structure
        for item in result["breakdown"]:
            assert isinstance(item, dict)
            assert "factor" in item
            assert "value" in item
            assert "delta" in item
            assert "note" in item

    def test_breakdown_item_types(self):
        """Test that breakdown items have correct types."""
        input_data = {
            "road_type": "urban",
            "weather": "clear",
            "time_of_day": "day",
            "lighting": "daylight",
            "junction": "no_junction",
            "road_surface": "dry"
        }

        result = predict_probability(input_data)

        for item in result["breakdown"]:
            assert isinstance(item["factor"], str)
            assert isinstance(item["value"], str)
            assert isinstance(item["delta"], (int, float))
            assert isinstance(item["note"], str)


class TestPredictSanityCases:
    """Test predict_probability with various input combinations."""

    def test_low_risk_scenario(self):
        """Test with conditions that should result in low risk."""
        input_data = {
            "road_type": "urban",
            "weather": "clear",
            "time_of_day": "day",
            "lighting": "daylight",
            "junction": "no_junction",
            "road_surface": "dry"
        }

        result = predict_probability(input_data)

        # Should be relatively low risk
        assert result["probability"] < 0.5
        assert result["risk_percent"] < 50
        assert len(result["breakdown"]) > 0

    def test_high_risk_scenario(self):
        """Test with conditions that should result in high risk."""
        input_data = {
            "road_type": "highway",
            "weather": "fog",
            "time_of_day": "night",
            "lighting": "dark_no_streetlights",
            "junction": "junction",
            "road_surface": "wet"
        }

        result = predict_probability(input_data)

        # Should be relatively high risk
        assert result["probability"] > 0.1  # At least some risk
        assert result["risk_percent"] > 10
        assert len(result["breakdown"]) > 0

    def test_rainy_conditions(self):
        """Test specifically rainy conditions."""
        input_data = {
            "road_type": "urban",
            "weather": "rain",
            "time_of_day": "day",
            "lighting": "daylight",
            "junction": "no_junction",
            "road_surface": "wet"
        }

        result = predict_probability(input_data)

        # Rain should increase risk
        assert result["probability"] > 0.1
        assert len(result["breakdown"]) > 0

        # Check that weather factor is in breakdown
        weather_factors = [item for item in result["breakdown"] if item["factor"] == "weather"]
        assert len(weather_factors) == 1
        assert weather_factors[0]["value"] == "rain"

    def test_night_driving(self):
        """Test night driving conditions."""
        input_data = {
            "road_type": "urban",
            "weather": "clear",
            "time_of_day": "night",
            "lighting": "dark_with_streetlights",
            "junction": "no_junction",
            "road_surface": "dry"
        }

        result = predict_probability(input_data)

        # Night driving should increase risk
        assert result["probability"] > 0.1
        assert len(result["breakdown"]) > 0

        # Check that time_of_day factor is in breakdown
        time_factors = [item for item in result["breakdown"] if item["factor"] == "time_of_day"]
        assert len(time_factors) == 1
        assert time_factors[0]["value"] == "night"

    def test_all_factors_present(self):
        """Test that all input factors appear in breakdown."""
        input_data = {
            "road_type": "highway",
            "weather": "fog",
            "time_of_day": "night",
            "lighting": "dark_no_streetlights",
            "junction": "junction",
            "road_surface": "wet"
        }

        result = predict_probability(input_data)

        breakdown_factors = {item["factor"] for item in result["breakdown"]}
        expected_factors = {"road_type", "weather", "time_of_day", "lighting", "junction", "road_surface"}

        assert breakdown_factors == expected_factors

        # Verify values match input
        for item in result["breakdown"]:
            factor = item["factor"]
            if factor in input_data:
                assert item["value"] == input_data[factor]


class TestPredictEdgeCases:
    """Test edge cases and error conditions."""

    def test_missing_input_keys(self):
        """Test behavior with missing input keys (should use defaults)."""
        # Partial input - missing some keys
        input_data = {
            "road_type": "urban",
            "weather": "clear"
            # Missing: time_of_day, lighting, junction, road_surface
        }

        # Should not crash and should provide defaults
        result = predict_probability(input_data)

        assert "probability" in result
        assert "risk_percent" in result
        assert "breakdown" in result
        assert len(result["breakdown"]) > 0

    def test_invalid_input_values(self):
        """Test with invalid input values (should handle gracefully)."""
        # Invalid values - should use defaults or handle gracefully
        input_data = {
            "road_type": "invalid_type",
            "weather": "invalid_weather",
            "time_of_day": "invalid_time",
            "lighting": "invalid_lighting",
            "junction": "invalid_junction",
            "road_surface": "invalid_surface"
        }

        # Should not crash
        result = predict_probability(input_data)

        assert "probability" in result
        assert "risk_percent" in result
        assert "breakdown" in result
        assert isinstance(result["probability"], (int, float))
        assert isinstance(result["risk_percent"], int)


class TestPredictConsistency:
    """Test that predictions are consistent for same inputs."""

    def test_same_input_same_output(self):
        """Test that identical inputs produce identical outputs."""
        input_data = {
            "road_type": "urban",
            "weather": "rain",
            "time_of_day": "night",
            "lighting": "dark_with_streetlights",
            "junction": "junction",
            "road_surface": "wet"
        }

        result1 = predict_probability(input_data)
        result2 = predict_probability(input_data)

        assert result1["probability"] == result2["probability"]
        assert result1["risk_percent"] == result2["risk_percent"]
        assert len(result1["breakdown"]) == len(result2["breakdown"])

        # Breakdown should be identical
        for i, item in enumerate(result1["breakdown"]):
            assert item["factor"] == result2["breakdown"][i]["factor"]
            assert item["value"] == result2["breakdown"][i]["value"]
            assert item["delta"] == result2["breakdown"][i]["delta"]
            assert item["note"] == result2["breakdown"][i]["note"]