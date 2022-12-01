def main():
    f = open("input")
    m = [x.strip() for x in f]
    f.close()

    height = len(m)
    width = len(m[0])
    res = 1

    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees = 0
        x = 0
        y = 0

        while y < height:
            if m[y][x] == "#":
                trees += 1

            x = (x + dx) % width
            y += dy

        res *= trees

    print(res)

if __name__ == "__main__":
    main()
