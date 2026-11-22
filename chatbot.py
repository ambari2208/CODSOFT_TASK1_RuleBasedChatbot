"""A friendly command-line chatbot built with rule-based responses.

This project uses regular-expression pattern matching instead of a trained
machine-learning model. It is intentionally small, transparent, and easy to
extend for the CodSoft Artificial Intelligence internship Task 1.
"""

from __future__ import annotations

import random
import re
from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Pattern


Response = str | Callable[[re.Match[str]], str]


@dataclass(frozen=True)
class Rule:
    """One conversation rule: a regular-expression pattern and its response."""

    pattern: Pattern[str]
    response: Response


class RuleBasedChatbot:
    """Responds to user messages using the first matching rule."""

    def __init__(self) -> None:
        self.user_name: str | None = None
        self.should_exit = False
        self.rules = self._build_rules()

    def _build_rules(self) -> list[Rule]:
        return [
            Rule(re.compile(r"\b(?:my name is|i am|i'm)\s+([a-z][a-z '-]{0,30})\b", re.I), self._remember_name),
            Rule(re.compile(r"\b(?:hello|hi|hey|good morning|good afternoon|good evening)\b", re.I), self._greeting),
            Rule(re.compile(r"\bhow are you\b", re.I), "I'm doing well, thank you for asking! How can I help you today?"),
            Rule(re.compile(r"\b(?:your name|who are you)\b", re.I), "I'm CodSoft Bot, a simple rule-based chatbot written in Python."),
            Rule(re.compile(r"\bwhat can you do\b|\bhelp\b", re.I), self._help),
            Rule(re.compile(r"\b(?:time|current time)\b", re.I), self._time),
            Rule(re.compile(r"\b(?:date|today(?:'s| is)? date)\b", re.I), self._date),
            Rule(re.compile(r"\b(?:thank you|thanks|thx)\b", re.I), "You're welcome! Is there anything else I can help with?"),
            Rule(re.compile(r"\b(?:bye|goodbye|exit|quit)\b", re.I), self._goodbye),
        ]

    def reply(self, message: str) -> str:
        """Return the response for *message*, or a fallback if no rule matches."""
        cleaned_message = " ".join(message.strip().split())
        if not cleaned_message:
            return "Please type a message so I can respond."

        for rule in self.rules:
            match = rule.pattern.search(cleaned_message)
            if match:
                if callable(rule.response):
                    return rule.response(match)
                return rule.response

        return random.choice(
            [
                "I'm not sure I understand that yet. Type 'help' to see what I can do.",
                "Sorry, I only know a few rule-based responses right now. Try asking for help.",
                "Could you rephrase that? Type 'help' for example questions.",
            ]
        )

    def _remember_name(self, match: re.Match[str]) -> str:
        self.user_name = match.group(1).strip(" .!?").title()
        return f"Nice to meet you, {self.user_name}! How can I help you today?"

    def _greeting(self, _match: re.Match[str]) -> str:
        name = f", {self.user_name}" if self.user_name else ""
        return f"Hello{name}! How can I help you today?"

    @staticmethod
    def _help(_match: re.Match[str]) -> str:
        return (
            "You can greet me, tell me your name, ask my name, ask how I am, "
            "ask for the time or date, say thanks, or say bye to end the chat."
        )

    @staticmethod
    def _time(_match: re.Match[str]) -> str:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."

    @staticmethod
    def _date(_match: re.Match[str]) -> str:
        return f"Today's date is {datetime.now().strftime('%A, %d %B %Y')}."

    def _goodbye(self, _match: re.Match[str]) -> str:
        self.should_exit = True
        name = f", {self.user_name}" if self.user_name else ""
        return f"Goodbye{name}! Thanks for chatting with me."


def main() -> None:
    """Run an interactive conversation in the terminal."""
    bot = RuleBasedChatbot()
    print("=" * 58)
    print("  CodSoft Bot - Rule-Based Chatbot")
    print("  Type 'help' for examples or 'bye' to exit.")
    print("=" * 58)

    while not bot.should_exit:
        try:
            user_message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Thanks for chatting with me.")
            break

        print(f"Bot: {bot.reply(user_message)}")


if __name__ == "__main__":
    main()
