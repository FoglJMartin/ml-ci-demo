"""Text preprocessing functions for the CI/CD teaching demo."""


def tokenize_text(text: str) -> list[str]:
    """Split text into whitespace-separated tokens."""
    return text.split()
