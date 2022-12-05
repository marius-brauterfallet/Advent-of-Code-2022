def main():
    f = open("input")

    res = 0

    for line in f:
        him, me = line.split()

        if me == "X":
            if him == "A":
                res += 4
            elif him == "B":
                res += 1
            else:
                res += 7

        elif me == "Y":
            if him == "A":
                res += 8
            elif him == "B":
                res += 5
            else:
                res += 2

        elif me == "Z":
            if him == "A":
                res += 3
            elif him == "B":
                res += 9
            else:
                res += 6

    f.close()

    print(res)


if __name__ == "__main__":
    main()
