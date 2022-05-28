from typing import Dict

from app.global_vars import KEYWORDS


def count_occurrences(text: str) -> Dict[str, int]:
    """ Function counts all occurrences of keywords in the text and return a dict with results """

    occurrences: Dict[str, int] = {}

    if text:
        for keyword in KEYWORDS:
            keyword_occurrences: int = text.lower().count(keyword)

            if keyword_occurrences:
                occurrences[keyword] = keyword_occurrences

    return occurrences
