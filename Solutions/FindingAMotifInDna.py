def find_motif(string, substring):
    positions = []
    substring_length = len(substring)
    for i in range(0, len(string)-substring_length+1):
        if string[i:i+substring_length] == substring:
            positions.append(i+1)
    return positions


def print_motif(string, substring):
    print(' '.join(str(x) for x in find_motif(string, substring)))

