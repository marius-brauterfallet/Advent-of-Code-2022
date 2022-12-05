def main():
    f = open("input")

    score = 0
    rock, paper, scissors = "A", "B", "C"
    r, p, s = 1, 2, 3
    lose, draw, win = "X", "Y", "Z"

    for line in f:
        him, outcome = line.split()

        if outcome == lose:
            if him == rock:
                score += s
            elif him == paper:
                score += r
            else:
                score += p

        elif outcome == draw:
            score += 3

            if him == rock:
                score += r

            elif him == paper:
                score += p

            else:
                score += s

        else:
            score += 6

            if him == rock:
                score += p

            elif him == paper:
                score += s

            else:
                score += r



    f.close()

    print(score)


if __name__ == "__main__":
    main()
