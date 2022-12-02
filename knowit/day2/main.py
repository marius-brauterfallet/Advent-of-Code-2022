def main():
    inp = list()
    with open("input") as f:
        inp = [line.strip().lower() for line in f]

    res = 0
    lines = 1

    for line in inp:
        if lines < 4:
            res += 2
        else:
            res += (lines - 1)

        if "alv" not in line:
            lines += 1

    print(res)


if __name__ == "__main__":
    main()
