def all_variants(text):
    for str_length in range(1, len(text) + 1):
        for i in range(len(text) - str_length + 1):
            yield text[i : i + str_length]

a = all_variants("abc")

for i in a:
    print(i)