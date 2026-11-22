# CODSOFT_TASK1 - Rule-Based Chatbot

A command-line chatbot that responds to user messages through predefined rules and regular-expression pattern matching. This completes Task 1 of the CodSoft Artificial Intelligence internship.

## Features

- Recognises greetings and common conversational messages
- Remembers the user's name during the current chat
- Responds to questions about its identity, time, and date
- Provides help for its supported commands
- Handles unsupported messages with a friendly fallback response
- Ends the conversation when the user says `bye`, `exit`, or `quit`

## Technologies

- Python 3
- Standard library only: `re`, `random`, `datetime`, `dataclasses`, and `unittest`

## Run the project

```bash
python chatbot.py
```

Example interaction:

```text
You: My name is Aisha
Bot: Nice to meet you, Aisha! How can I help you today?
You: What can you do?
Bot: You can greet me, tell me your name, ask my name, ask how I am, ask for the time or date, say thanks, or say bye to end the chat.
You: bye
Bot: Goodbye, Aisha! Thanks for chatting with me.
```

## Run the tests

```bash
python -m unittest -v
```

## How it works

1. The chatbot cleans the user's input.
2. It checks the input against ordered regular-expression rules.
3. The first matching rule generates a response.
4. If no rule matches, the chatbot gives a helpful fallback response.

The rules are deliberately transparent and easy to extend. Add a new `Rule` inside `_build_rules()` in `chatbot.py` to teach the chatbot another response.

## Suggested demo flow

For a short LinkedIn video, show the program starting, introduce yourself, ask for help, ask the time, type an unknown question to demonstrate the fallback, and end with `bye`.
