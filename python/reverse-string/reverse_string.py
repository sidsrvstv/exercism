def reverse(input=''):
    res = []
    for c in reversed(input):
        res.append(c)
    return ''.join(res)
