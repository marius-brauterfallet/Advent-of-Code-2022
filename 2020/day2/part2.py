def main():
    f = open("input")
    valids = 0

    for line in f:
        counts, letter, pwd = line.strip().split()

        low, high = [int(x) for x in counts.split("-")]

        if len(pwd) > high + 1 and pwd[low + 1] == letter[0] and pwd[high + 1] != letter[0]:
            valids += 1

    f.close()

    print(valids)


if __name__ == "__main__":
    main()
