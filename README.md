# Rule-Based Chatbot | CodSoft AI Internship – Task 1

A simple, interactive command-line chatbot developed in Python for Task 1 of the CodSoft Artificial Intelligence internship. The chatbot uses predefined conversation rules and regular-expression pattern matching to recognise common messages and generate responses.

## Project Overview

This project demonstrates the basic working of a rule-based conversational system. Instead of using a trained machine-learning model, it checks each message against an ordered set of patterns and responds when it finds a match. The approach keeps the chatbot lightweight, easy to understand, and straightforward to extend.

## Features

- **Greeting recognition:** Responds to greetings such as `hello`, `hi`, `hey`, and common time-based greetings.
- **Name recognition:** Stores the name shared by the user and uses it in later greetings and the goodbye message.
- **Basic conversation:** Responds to questions about how it is doing and its identity.
- **Date and time:** Displays the current date and time using the computer's system clock.
- **Help response:** Lists the types of messages the chatbot can understand.
- **Fallback responses:** Gives a friendly prompt when a message does not match any available rule.
- **Exit commands:** Ends the conversation when the user enters `bye`, `goodbye`, `exit`, or `quit`.

## Technologies Used

- Python 3
- Python standard library: `re`, `random`, `datetime`, and `dataclasses`
- `unittest` for automated testing

No third-party Python packages are required.

## Project Structure

```text
CODSOFT_TASK1/
├── chatbot.py       # Chatbot logic and command-line interface
├── test_chatbot.py  # Automated unit tests
└── README.md        # Project documentation
```

## Getting Started

### Prerequisites

Install Python 3 and make sure the `python` command is available in your terminal. You can check the installation with:

```bash
python --version
```

### Run the chatbot

1. Open a terminal in the project folder.
2. Run:

```bash
python chatbot.py
```

3. Enter a message when the `You:` prompt appears. Type `help` to see supported conversation topics, or `bye` to end the chat.

## Example Conversation

```text
==========================================================
  CodSoft Bot - Rule-Based Chatbot
  Type 'help' for examples or 'bye' to exit.
==========================================================
You: My name is Aisha
Bot: Nice to meet you, Aisha! How can I help you today?
You: hello
Bot: Hello, Aisha! How can I help you today?
You: What can you do?
Bot: You can greet me, tell me your name, ask my name, ask how I am, ask for the time or date, say thanks, or say bye to end the chat.
You: bye
Bot: Goodbye, Aisha! Thanks for chatting with me.
```

## How It Works

1. The chatbot receives a message and normalises extra whitespace.
2. It checks the message against a list of regular-expression patterns in the order they are defined.
3. When a pattern matches, the corresponding response is returned. Some rules call helper methods, such as the method that stores the user's name or retrieves the current date and time.
4. If none of the patterns match, the chatbot selects a fallback response.
5. When an exit phrase is recognised, the chatbot sets its exit flag and the command-line loop ends.

## Run the Tests

The project includes unit tests for name recognition, the help response, fallback handling, and the goodbye/exit behaviour.

From the project folder, run:

```bash
python -m unittest -v
```

## Current Scope

This is an introductory rule-based chatbot. It responds only to the patterns and topics defined in the code; it does not understand messages through machine learning or natural-language model inference. Its name memory lasts only for the current run of the program.

## Possible Extension

New conversation patterns and responses can be added to the `_build_rules()` method in `chatbot.py`, along with tests for the new behaviour.
