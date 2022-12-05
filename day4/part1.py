def main():
    res = 0

    with open("input") as f:
        for l in f:
            elves = l.split(",")

            bounds = list()

            for elf in elves:
                bounds.append([int(x) for x in elf.split("-")])

            bounds.sort(key=lambda x : x[1] - x[0])

            if bounds[0][0] >= bounds[1][0] and bounds[0][1] <= bounds[1][1]:
                res += 1

    print(res)


if __name__ == "__main__":
    main()