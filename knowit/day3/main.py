def main():
    pakker = list()

    with open("inp2") as f:
        for line in f:
            pakker.append(sorted([int(x) for x in line.strip().split(",")]))

    s = 0

    for p in pakker:
        if p[2] + p[0] > 55:
            if p[0] + p[1] < 55:
                k = 2 * p[0] + p[2]
                s += k
                print(p, k)

            else:
                k = 2 * (p[2] + p[0])
                s += k
                print(p, k)

        else:
            k = p[0] + p[1]
            s += k
            print(p, k)

    print(s)


if __name__ == "__main__":
    main()
