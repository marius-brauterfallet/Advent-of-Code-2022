def main():
    # Det korteste ordet er 2 chars langt og det lengste 15
    # Det eneste ordet som kan settes sammen av to mindre ord er musika (market)
    # Dette settes sammen av mu (in) og sika (create)

    d = dict()

    with open("dictionary.txt") as f:
        for line in f:
            k, v = line.strip().split(",")
            d[k] = v

    l = ""

    with open("letter.txt") as f:
        l = f.read().strip()


    low, high = 0, 2
    length = len(l)
    res = ""

    while low < length:
        w = ""

        while high - low < 16:
            if l[low: high] in d:
                w = l[low: high]

            high += 1
            if high > length:
                break

        if len(w) == 0:
            print("FUNKER IKKE", low, high, l[low: high], length)
            return

        res += d[w] + " "
        low += len(w)
        high = low + 2

    print(len(res.strip()))



if __name__ == "__main__":
    main()
