from __future__ import annotations

import gettext
import json
import locale
import os
from pathlib import Path

_SETTINGS_DIR = Path(os.path.expanduser("~/.config/nirimod"))
_SETTINGS_FILE = _SETTINGS_DIR / "settings.json"
LOCALE_DIR = Path(__file__).parent / "locale"

_DEFAULTS: dict = {
    "auto_update": True,
    "config_path": "",
    "backup_path": "",
    "auto_backup": True,
    "backup_limit": 10,
    "language": "",  # Empty = system default, "zh_CN" = Chinese
}

_cache: dict | None = None

# Initialize gettext
gettext.bindtextdomain("nirimod", str(LOCALE_DIR))
gettext.textdomain("nirimod")
_ = gettext.gettext


def _load() -> dict:
    global _cache
    if _cache is not None:
        return _cache
    if _SETTINGS_FILE.exists():
        try:
            data = json.loads(_SETTINGS_FILE.read_text())
            _cache = {**_DEFAULTS, **data}
            return _cache
        except (json.JSONDecodeError, OSError):
            pass
    _cache = dict(_DEFAULTS)
    return _cache


def _save(data: dict):
    global _cache
    _SETTINGS_DIR.mkdir(parents=True, exist_ok=True)
    _SETTINGS_FILE.write_text(json.dumps(data, indent=2))
    _cache = data


def apply_language():
    """Apply the language setting from preferences."""
    lang = get("language", "")
    if lang:
        os.environ["LANGUAGE"] = lang
        os.environ["LC_ALL"] = lang
        os.environ["LANG"] = lang
        locale.setlocale(locale.LC_ALL, lang)
        # Update gettext
        gettext.bindtextdomain("nirimod", str(LOCALE_DIR))
        gettext.textdomain("nirimod")
    else:
        # Use system default
        locale.setlocale(locale.LC_ALL, "")
        gettext.bindtextdomain("nirimod", str(LOCALE_DIR))
        gettext.textdomain("nirimod")


def get(key: str, default=None):
    return _load().get(key, default)


def set(key: str, value):  # noqa: A001
    data = dict(_load())
    data[key] = value
    _save(data)
