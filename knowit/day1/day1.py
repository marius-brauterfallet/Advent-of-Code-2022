def main():
    d = make_dict("dictionary.txt")
    f = open("letter.txt")
    data = f.read().lower().strip()
    f.close()

    low, high = 0, 1
    res = list()
        
    while low < len(data):
        if data[low: high] in d:
            res.append(data[low: high])
            low = high
            high = low + 1

        elif high - low > 20:

            l = len(res.pop())

            low = low - l
            high = low + l + 1

        else:
            high += 1

    r = " ".join([d[x] for x in res])
    print(r + "\n" + str(len(r)))

def make_dict(filename):
    d = dict()

    with open(filename) as f:
        for line in f:
            a, b = line.lower().strip().split(",")
            d[a] = b

    return d


if __name__ == "__main__":
    main()
