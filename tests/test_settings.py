""" Test module to test Settings class from settings.py"""
import unittest
from src.settings import Settings
# pylint: disable=protected-access

class TestSettings(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """
    def setUp(self):
        """ [Settings] Setup for the Settings class """
        # Arrange
        self.settings = Settings()

    def tearDown(self):
        """ [Settings] Reset for the Settings class """
        # Arrange
        self.settings = None

    def test_init(self):
        """ [Settings] Test that Settings init works as expected """
        self.setUp()

        self.assertEqual(self.settings.rule, "standard")
        self.assertEqual(self.settings.json_data, self.settings._Settings__read_json())

        self.tearDown()

    def test_get_current_settings(self):
        """ [Settings] Test to get correct settings """
        self.setUp()

        self.assertEqual(self.settings.get_current_settings(), "standard")
        self.settings.set_settings("customized")
        self.assertEqual(self.settings.get_current_settings(), "customized")

        self.tearDown()

    def test_json_file(self):
        """ [Settings] Test get data from json file """
        self.setUp()

        custom_data = self.settings.get_settings("customized")
        self.assertIsInstance(custom_data, object)

        standard_data = self.settings.get_settings("standard")
        self.assertIsInstance(standard_data, object)

        self.tearDown()

    def test_set_settings(self):
        """ [Settings] Test to set standard to customized settings """
        self.setUp()

        self.settings.set_settings("customized")
        self.assertEqual(self.settings.get_current_settings(), "customized")

        self.tearDown()

    def test_edit_sentence_newline(self):
        """ [Edit Settings] Test to edit sentence newline rule setting on customized settings """
        self.setUp()

        self.settings.edit_custom_settings("sentence-newline", True)
        customized_settings = self.settings.get_settings("customized")
        self.assertEqual(customized_settings["sentence-newline"], True)

        self.settings.edit_custom_settings("sentence-newline", False)
        self.assertEqual(customized_settings["sentence-newline"], False)

        self.tearDown()

    def test_edit_comment_space(self):
        """ [Edit Settings] Test edit comment space rule setting on customized settings """
        self.setUp()

        self.settings.edit_custom_settings("comment-space", 50)
        customized_settings = self.settings.get_settings("customized")
        self.assertEqual(customized_settings["comment-space"], 50)
        self.assertIsInstance(customized_settings["comment-space"], int)

        self.settings.edit_custom_settings("comment-space", 150)
        customized_settings = self.settings.get_settings("customized")
        self.assertEqual(customized_settings["comment-space"], 150)
        self.assertIsInstance(customized_settings["comment-space"], int)

        self.tearDown()

    def test_edit_emptylines(self):
        """ [Edit Settings] Test edit emptylines rule setting on customized settings """
        self.setUp()

        self.settings.edit_custom_settings("emptylines", 25)
        customized_settings = self.settings.get_settings("customized")
        self.assertEqual(customized_settings["emptylines"], 25)
        self.assertIsInstance(customized_settings["emptylines"], int)

        self.tearDown()

    def test_add_enviroment_blocks_exclude(self):
        """ [Edit Settings] Test to add a enviroment block in the list to exclude """
        self.setUp()

        self.settings.edit_enviroment_blocks_exclude_remove("unittest")
        customized_settings = self.settings.get_settings("customized")
        print(customized_settings["environment_blocks_exclude"])
        self.assertIsInstance(customized_settings["environment_blocks_exclude"], object)
        self.settings.edit_enviroment_blocks_exclude_add("unittest")
        print(customized_settings["environment_blocks_exclude"])

        self.tearDown()