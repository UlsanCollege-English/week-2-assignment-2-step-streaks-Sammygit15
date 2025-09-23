from typing import List
from collections import Counter

def unique_words_preserve_order(words: List[str]) -> List[str]:
    """Return first occurrences only (case-sensitive)."""
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result

def top_k_frequent_first_tie(words: List[str], k: int) -> List[str]:
    """Return up to k words ordered by frequency (high to low).

    For ties, earlier first-appearance wins.
    If k <= 0, raise ValueError.
    """
    if k <= 0:
        raise ValueError("k must be positive")
    
    # Count frequencies
    freq = Counter(words)
    
    # Use first appearance index to break ties
    first_index = {word: idx for idx, word in enumerate(words)}
    
    # Sort by frequency descending, then first appearance ascending
    sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], first_index[w]))
    
    return sorted_words[:k]

def redact_words(words: List[str], banned: List[str]) -> List[str]:
    """Return a new list where every word in `banned` is replaced by "***".

    Exact matches only; case-sensitive.
    """
    banned_set = set(banned)
    return ["***" if word in banned_set else word for word in words]
