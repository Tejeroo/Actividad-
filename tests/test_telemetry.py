import pytest
from src.telemetry import authorize_operation, consume, validate_telemetry

VALID = {"equipment_id": "PLC_SIM_01", "temperature_c": 42.5, "timestamp": "2026-10-20T10:00:00Z"}


def test_read_is_allowed():
    assert authorize_operation("read") is True


def test_write_is_rejected():
    assert authorize_operation("write") is False


def test_unknown_operation_is_rejected():
    assert authorize_operation("delete") is False


def test_valid_telemetry():
    assert consume(VALID).temperature_c == 42.5


def test_missing_field_rejected():
    with pytest.raises(ValueError):
        validate_telemetry({"equipment_id": "PLC_SIM_01", "temperature_c": 42.5})


def test_invalid_temperature_rejected():
    with pytest.raises(ValueError):
        validate_telemetry({**VALID, "temperature_c": "hot"})


def test_write_consume_rejected():
    with pytest.raises(PermissionError):
        consume(VALID, "write")
