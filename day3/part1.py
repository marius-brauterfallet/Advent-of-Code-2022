def main():
    with open("input") as f:
        s = 0

        for line in f:
            line = line.strip()
            length = len(line)

            l1, l2 = line[0: length // 2], line[length // 2:]


            for c in l1:
                if c in l2:
                    s += ord(c)
                    if c.islower():
                        s -= 96

                    else:
                        s -= 38

                    break

        print(s)


if __name__ == "__main__":
    main()
