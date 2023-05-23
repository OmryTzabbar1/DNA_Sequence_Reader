sequence = "GATCCAGATCCCCATAC"


def PatternCount(sequence):
    twoMers = {}
    for i in range(len(sequence) - 1):

        current = sequence[i: i + 2]
        if current in twoMers:
            twoMers[current] += 1

        else:
            twoMers[current] = 1

    return (twoMers)


def FrequentWord(sequence):
    words = []
    Mers = PatternCount(sequence)
    m = max(Mers.values())
    for i in Mers:
        if Mers[i] == m:
            words.append(i)
    return words


print(PatternCount(sequence))


def find_complement(sequence):
    complement_sequence = ""
    for i in sequence:
        if i == "A":
            complement_sequence = complement_sequence + "T"
        elif i == "T":
            complement_sequence = complement_sequence + "A"
        elif i == "G":
            complement_sequence = complement_sequence + "C"
        elif i == "C":
            complement_sequence = complement_sequence + "G"
        else:
            print("Invalid. There is a value here that's not a nucleotide base")
    return (complement_sequence)

