def is_isogram(string):
    seen = set()
    isAllowed = " -"
    for c in string:
        if c.lower() not in seen or c in isAllowed:
            seen.add(c.lower())
        else:
            return False
    return True
