def main():
    res = 0

    with open("input") as f:
        for l in f:
            elves = l.split(",")

            bounds = list()

            for elf in elves:
                bounds.append([int(x) for x in elf.split("-")])

            bounds.sort()

            if bounds[0][0] <= bounds[1][0] <= bounds[0][1] or bounds[0][0] <= bounds[1][1] <= bounds[0][1]:
                print(bounds)
                res += 1
            
    print(res)


if __name__ == "__main__":
    main()