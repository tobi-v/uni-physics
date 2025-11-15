from textwrap import wrap as textwrap_wrap

def wrap(s: str, width: int = 50) -> str:
    """Wrap plain text nicely by inserting newlines. Keeps backslashes/$ intact (use raw strings)."""
    return '\n'.join(textwrap_wrap(s, width=width))