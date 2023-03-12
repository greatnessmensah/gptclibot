import os
from click.testing import CliRunner
from unittest.mock import patch
import pytest

from ..main import chat


def test_chat():
    runner = CliRunner()

    with patch("openai.Completion.create") as mock_create:
        mock_create.return_value.choices = [
            {"text": "Hello, how can I help you today?"},
            {"text": "Sure, here's what you need to know..."},
        ]

        result = runner.invoke(
            chat,
            [
                "--model",
                "text-davinci-002",
                "--temperature",
                "0.8",
                "--max-tokens",
                "256",
                "--output-format",
                "md",
                "--text-file",
                "",
                "--speed",
                "fast",
                "--topic",
                "FAQ",
                "--response-length",
                "short",
                "--clear-history",
            ],
            input="Hello",
        )

        assert result.exit_code == 0
        expected_output = (
            "Chat history reset."
        )
        assert result.output.strip() == expected_output
        assert not os.path.isfile("~/chatcli/chatcli.log")


def test_chat_error():
    with patch("builtins.input", return_value="hello"):
        with patch("openai.Completion.create", side_effect=Exception("Test Error")):
            with pytest.raises(Exception):
                chat(...)
