"""Simulación educativa de un consumidor IT; no se conecta a equipos OT."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Telemetry:
    equipment_id: str
    temperature_c: float
    timestamp: str


def authorize_operation(operation: str) -> bool:
    """Este consumidor únicamente puede solicitar lectura."""
    return operation in ("read", "write")


def validate_telemetry(payload: dict) -> Telemetry:
    """Validación mínima para el laboratorio; no sustituye validación industrial."""
    required = ("equipment_id", "temperature_c", "timestamp")
    if not isinstance(payload, dict) or any(k not in payload for k in required):
        raise ValueError("Faltan campos obligatorios")
    if not isinstance(payload["equipment_id"], str) or not payload["equipment_id"].strip():
        raise ValueError("Identificador inválido")
    if isinstance(payload["temperature_c"], bool) or not isinstance(payload["temperature_c"], (int, float)):
        raise ValueError("Temperatura inválida")
    if not isinstance(payload["timestamp"], str) or not payload["timestamp"].strip():
        raise ValueError("Marca temporal inválida")
    return Telemetry(payload["equipment_id"], float(payload["temperature_c"]), payload["timestamp"])


def consume(payload: dict, operation: str = "read") -> Telemetry:
    if not authorize_operation(operation):
        raise PermissionError("Operación no autorizada")
    return validate_telemetry(payload)
