def is_pangram(sentence):
    seen = set()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c in sentence:
        w = c.lower()
        if w in alphabet and w not in seen:
            seen.add(w)
    return len(seen) == 26
