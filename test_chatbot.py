"""Automated checks for the rule-based chatbot."""

import unittest

from chatbot import RuleBasedChatbot


class RuleBasedChatbotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bot = RuleBasedChatbot()

    def test_name_is_saved_and_used_in_greeting(self) -> None:
        self.assertIn("Nice to meet you, Aisha", self.bot.reply("My name is Aisha"))
        self.assertIn("Aisha", self.bot.reply("hello"))

    def test_help_response_lists_supported_topics(self) -> None:
        self.assertIn("time or date", self.bot.reply("help"))

    def test_unknown_message_has_fallback(self) -> None:
        self.assertIn("help", self.bot.reply("tell me about quantum bananas").lower())

    def test_goodbye_ends_conversation(self) -> None:
        self.assertFalse(self.bot.should_exit)
        self.assertIn("Goodbye", self.bot.reply("bye"))
        self.assertTrue(self.bot.should_exit)


if __name__ == "__main__":
    unittest.main()
