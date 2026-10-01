"""Tests for language settings and translations."""

from __future__ import annotations

import unittest
import os

from nirimod import app_settings


class TestLanguageSettings(unittest.TestCase):
    def setUp(self):
        # Reset cache to avoid cross-test contamination
        app_settings._cache = None

    def test_default_language_is_empty(self):
        # Reset to defaults
        app_settings._cache = dict(app_settings._DEFAULTS)
        self.assertEqual(app_settings.get("language", ""), "")

    def test_language_setting_zh_cn(self):
        app_settings._cache = {"language": "zh_CN"}
        self.assertEqual(app_settings.get("language", ""), "zh_CN")

    def test_apply_language_sets_env(self):
        app_settings._cache = {"language": "zh_CN"}
        app_settings.apply_language()
        self.assertEqual(os.environ.get("LANGUAGE"), "zh_CN")
        self.assertEqual(os.environ.get("LC_ALL"), "zh_CN")
        self.assertEqual(os.environ.get("LANG"), "zh_CN")

    def test_apply_language_default_clears_env(self):
        app_settings._cache = {"language": ""}
        app_settings.apply_language()
        # When empty, LANGUAGE and LC_ALL should not be set by us
        self.assertNotIn("LANGUAGE", os.environ)
        self.assertNotIn("LC_ALL", os.environ)
        # LANG may be set by the system, so just verify it's not our zh_CN
        self.assertNotEqual(os.environ.get("LANG", ""), "zh_CN")


class TestTranslations(unittest.TestCase):
    def test_chinese_translation_available(self):
        import gettext
        locale_dir = os.path.join(os.path.dirname(__file__), "..", "nirimod", "locale")
        t = gettext.translation("nirimod", locale_dir, languages=["zh_CN"], fallback=True)
        # Key strings should be translated
        self.assertEqual(t.gettext("Save & Apply"), "保存并应用")
        self.assertEqual(t.gettext("Undo"), "撤销")
        self.assertEqual(t.gettext("NiriMod Preferences"), "NiriMod 首选项")
        self.assertEqual(t.gettext("Language"), "语言")
        self.assertEqual(t.gettext("System Default"), "系统默认")


if __name__ == "__main__":
    unittest.main()