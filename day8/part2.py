def main():
    with open("input") as f:
        trees = [[int(x) for x in l.strip()] for l in f]

    scores = [[1 for y in x] for x in trees]
    res = 0

    for x in range(1, len(trees) - 1):
        for y in range(1, len(trees) - 1):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x2, y2 = x + dx, y + dy
                n = 1

                while trees[x2][y2] < trees[x][y]:
                    x2 += dx
                    y2 += dy

                    if 0 <= x2 < len(trees) and 0 <= y2 < len(trees):
                        n += 1

                    else:
                        break

                scores[x][y] *= n


            if scores[x][y] > res:
                res = scores[x][y]

    print(res)

    
if __name__ == "__main__":
    main()