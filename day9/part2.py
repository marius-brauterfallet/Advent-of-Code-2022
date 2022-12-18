def main():
    dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    knots = [(0, 0)] * 10
    visited = {(0,0)}

    with open("input") as f:
        for line in f:
            d, n = line.split()
            
            for i in range(int(n)):
                head = knots[0]

                knots[0] = (head[0] + dirs[d][0], head[1] + dirs[d][1])

                for j, k in enumerate(knots[1:]):
                    p = knots[j]

                    dx, dy = p[0] - k[0], p[1] - k[1]

                    if abs(dx) > 1:
                        if dx > 0:
                            knots[j + 1] = (p[0] - 1, p[1])
                        else:
                            knots[j + 1] = (p[0] + 1, p[1])

                    elif abs(dy) > 1:
                        if dy > 0:
                            knots[j + 1] = (p[0], p[1] - 1)
                        else:
                            knots[j + 1] = (p[0], p[1] + 1)

                visited.add(knots[-1])

        print(len(visited))



if __name__ == "__main__":
    main()
