def main():
    f = open("input")
    valids = 0

    for line in f:
        counts, letter, pwd = line.strip().split()

        low, high = [int(x) for x in counts.split("-")]

        if low <= pwd.count(letter[0]) <= high:
            valids += 1

    f.close()

    print(valids)


if __name__ == "__main__":
    main()
