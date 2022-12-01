def main():
    f = open("input")
    valids = 0

    for line in f:
        counts, letter, pwd = line.strip().split()
        letter = letter[0]

        low, high = [int(x) - 1 for x in counts.split("-")]

        if (pwd[low] == letter) != (pwd[high] == letter):
            valids += 1

    f.close()

    print(valids)


if __name__ == "__main__":
    main()
