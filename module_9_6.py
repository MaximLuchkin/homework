def all_variants(text):
    a = len(text)
    for b in range(1, a + 1):
        for i in range(a - b + 1):
            yield text[i:i + b]


a = all_variants("abc")
for i in a:
    print(i)