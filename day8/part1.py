def main():
    with open("input") as f:
        trees = [[int(x) for x in l.strip()] for l in f]

    visible = [[False for y in x] for x in trees]
    res = 0
    
    highest_down = [-1] * len(trees)
    highest_up = [-1] * len(trees)
    highest_right = [-1] * len(trees)
    highest_left = [-1] * len(trees)

    for a in range(len(trees)):
        for b in range(len(trees)):
            rev_a = len(trees) - a - 1

            if trees[a][b] > highest_down[b]:
                highest_down[b] = trees[a][b]

                if not visible[a][b]:
                    visible[a][b] = True
                    res += 1

            if trees[rev_a][b] > highest_up[b]:
                highest_up[b] = trees[rev_a][b]
                
                if not visible[rev_a][b]:
                    visible[rev_a][b] = True
                    res += 1

            if trees[b][a] > highest_right[b]:
                highest_right[b] = trees[b][a]

                if not visible[b][a]:
                    visible[b][a] = True
                    res += 1

            if trees[b][rev_a] > highest_left[b]:
                highest_left[b] = trees[b][rev_a]

                if not visible[b][rev_a]:
                    visible[b][rev_a] = True
                    res += 1

    print(res)


if __name__ == "__main__":
    main()