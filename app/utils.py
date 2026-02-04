import re

import re

def clean_text(text: str) -> str:
    # Remove HTML tags
    text = re.sub(r"<[^>]*>", " ", text)

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # Keep letters/numbers/basic punctuation; replace others with space
    text = re.sub(r"[^a-zA-Z0-9\s.,;:!?()'\"-]", " ", text)

    # Collapse multiple spaces
    text = re.sub(r"\s{2,}", " ", text)

    return text.strip()
