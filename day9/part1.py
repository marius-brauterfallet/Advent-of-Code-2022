def main():
    dirs = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

    visited = set((0, 0))
    head_pos = [0, 0]
    tail_pos = [0, 0]

    with open("input") as f:
        for l in f:
            direction, amount = l.split()
            amount = int(amount)

            for i in range(amount):
                head_pos[0] += dirs[direction][0]
                head_pos[1] += dirs[direction][1]

                x_dif = head_pos[0] - tail_pos[0]
                y_dif = head_pos[1] - tail_pos[1]

                if abs(x_dif) > 1:
                    if x_dif > 0:
                        tail_pos[0] += 1

                    else:
                        tail_pos[0] -= 1

                    if y_dif != 0:
                        tail_pos[1] = head_pos[1]

                    if tuple(tail_pos) not in visited:
                        visited.add((tuple(tail_pos)))

                elif abs(y_dif) > 1:
                    if y_dif > 0:
                        tail_pos[1] += 1

                    else:
                        tail_pos[1] -= 1

                    if x_dif != 0:
                        tail_pos[0] = head_pos[0]

                    if tuple(tail_pos) not in visited:
                        visited.add((tuple(tail_pos)))

    print(len(visited))



if __name__ == "__main__":
    main()
