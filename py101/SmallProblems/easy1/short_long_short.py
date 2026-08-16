def short_long_short(s1, s2):
    short, long = (s1, s2) if len(s1) < len(s2) else (s2, s1)
    return short + long + short

print(short_long_short('abc', 'defg'))
print(short_long_short('abcde', 'fgh'))
print(short_long_short('', 'xyz'))

