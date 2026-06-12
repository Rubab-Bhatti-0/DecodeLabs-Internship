#!/usr/bin/env python3
import unittest
from unittest.mock import patch
import io
import sys
from chatbot import main

class TestRuleBasedChatbot(unittest.TestCase):
    """Test suite for the Rule-Based AI Chatbot."""

    @patch('builtins.input', side_effect=['hello', 'exit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_greeting_and_exit(self, mock_stdout, mock_input):
        """Test a basic greeting and clean exit."""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Hi there!", output)
        self.assertIn("Goodbye!", output)

    @patch('builtins.input', side_effect=['  HELP  ', 'bye'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sanitization(self, mock_stdout, mock_input):
        """Test input sanitization (case and whitespace)."""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("I can respond to greetings", output)
        self.assertIn("Goodbye!", output)

    @patch('builtins.input', side_effect=['unknown command', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fallback(self, mock_stdout, mock_input):
        """Test the fallback mechanism for unknown inputs."""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("I don't understand that", output)

    @patch('builtins.input', side_effect=['what is ai', 'explain logic engine', 'exit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_knowledge_base(self, mock_stdout, mock_input):
        """Test specific knowledge base entries."""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("AI (Artificial Intelligence) is the simulation", output)
        self.assertIn("logic engine processes inputs", output)

if __name__ == '__main__':
    unittest.main()
