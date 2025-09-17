from collections import Counter

def unique_words_preserve_order(words):
    """Return a list of unique words, preserving the order of their first appearance."""
    seen = set()
    unique_words = []
    for word in words:
        if word not in seen:
            seen.add(word)
            unique_words.append(word)
    return unique_words

def top_k_frequent_first_tie(words, k):
    """Return the top k most frequent words, resolving ties by their first appearance."""
    if k <= 0:
        raise ValueError("k must be greater than 0.")
    
    # Count frequencies of words
    word_counts = Counter(words)
    
    # Sort words by frequency (most common first) and by first appearance
    sorted_words = sorted(word_counts, key=lambda word: (-word_counts[word], words.index(word)))
    
    return sorted_words[:k]

def redact_words(words, redact_list):
    """Redact words in the redact_list with '***'."""
    return [word if word not in redact_list else '***' for word in words]
