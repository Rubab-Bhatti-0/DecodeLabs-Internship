# Project 1: Rule-Based AI Chatbot

This project implements a fundamental **Rule-Based AI Chatbot** as specified in the DecodeLabs Industrial Training Kit. It demonstrates the transition from probabilistic "Black Box" AI to deterministic "White Box" logic engines.

## Key Features

- **Continuous Input Loop**: Stays active until an explicit exit command is received.
- **Robust Sanitization**: Normalizes user input by handling case sensitivity and stripping whitespace.
- **Efficient Knowledge Base**: Uses Python dictionaries for $O(1)$ constant-time intent matching.
- **Deterministic Guardrails**: Implements a reliable fallback mechanism using the `.get()` method to prevent "hallucinations."
- **Clean Exit Strategy**: Gracefully handles termination commands like `exit`, `quit`, or `bye`.

## Implementation Details

The chatbot follows the **IPO Model** (Input-Process-Output):

1.  **Input**: Captures raw user text.
2.  **Process**: Normalizes the text and performs a direct lookup in the `responses` dictionary.
3.  **Output**: Delivers the matched response or a helpful fallback message.

## How to Run

To start the chatbot, run the following command in your terminal:

```bash
python3 chatbot.py
```

## Testing

A test suite is provided to validate the logic, sanitization, and fallback mechanisms:

```bash
python3 test_chatbot.py
```

## Specification Compliance

| Requirement | Implementation | Status |
| :--- | :--- | :--- |
| **Input Loop** | `while True` cycle | |
| **Sanitization** | `.lower().strip()` | |
| **Knowledge Base** | Dictionary with 15+ intents |  |
| **Fallback** | `.get(input, default)` ||
| **Exit Strategy** | `exit`, `quit`, `bye`, `goodbye` 
| **Complexity** | $O(1)$ Dictionary Lookup 
