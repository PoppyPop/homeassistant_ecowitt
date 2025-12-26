"""Diagnostics support for Ecowitt Weather Station integration."""

from __future__ import annotations

from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN, DATA_LAST_MESSAGES


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry.

    Includes the last 3 messages received by the integration (payloads),
    with sensitive fields redacted.
    """

    data = hass.data.get(DOMAIN, {}).get(entry.entry_id, {})
    messages = data.get(DATA_LAST_MESSAGES, [])

    # Redact sensitive fields like PASSKEY inside message payloads
    redacted_messages: list[dict[str, Any]] = []
    for m in messages:
        # Copy outer structure
        out: dict[str, Any] = {"timestamp": m.get("timestamp")}
        payload = dict(m.get("data", {}))
        # Remove PASSKEY if present
        if "PASSKEY" in payload:
            payload.pop("PASSKEY", None)
        out["data"] = payload
        redacted_messages.append(out)

    return {
        "entry": {
            "data": entry.data,
            "options": entry.options,
        },
        "last_messages": redacted_messages,
    }
