def main():
    lines = list()
    s = 0

    with open("input") as f:
        lines = [line.strip() for line in f]

    for i in range(0, len(lines), 3):
        s1, s2, s3 = set(lines[i]), set(lines[i + 1]), set(lines[i + 2])

        for c in s1:
            if c in s2 and c in s3:
                s += ord(c)

                if c.islower():
                    s -= 96

                else:
                    s -= 38
                break

    print(s)


if __name__ == "__main__":
    main()
