"""Text preprocessing functions for the CI/CD teaching demo."""


def tokenize_text(text: str) -> list[str]:
    """Convert text to lowercase whitespace-separated tokens."""
    return text.lower().split()
