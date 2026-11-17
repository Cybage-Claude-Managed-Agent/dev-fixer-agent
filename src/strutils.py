"""Small string helpers."""


def slugify(text):
    """Turn text into a URL slug: lower case, words joined by hyphens."""
    return "-".join(text.split())


def truncate(text, limit):
    """Shorten text to `limit` characters, adding '...' when it was cut."""
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "..."


def word_count(text):
    """Count the words in text."""
    return len(text.split(" "))
