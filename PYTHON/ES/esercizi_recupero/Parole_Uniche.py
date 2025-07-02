from string import punctuation


def count_unique_words(s : str) -> dict[str,int]:

    d : dict[str, int] = {}
    s = s.split(" ")

    for token in s:

        token_lower : str = token.lower()
        clean_token : str = token_lower.strip(punctuation)

        if not clean_token:
            continue

        if clean_token in s :
            d[clean_token] += 1

        else:
            d[clean_token] = 1

    return d