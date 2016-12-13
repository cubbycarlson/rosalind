def hamming_distance_for_loop(string1, string2):
    count = 0
    for i, base in enumerate(string1):
        if base != string2[i]:
            count += 1
    return count


def hamming_distance(string1, string2):
    return sum([base1 != base2 for base1, base2 in zip(string1, string2)])
