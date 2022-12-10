def main():
    crt = ""
    i = 0
    x = 0
    res = 0

    with open("input") as f:
        for line in f:
            data = line.split()

            if data[0] == "noop":
                if i in (x, x + 1, x + 2):
                    crt += "#"

                else:
                    crt += "."

                i = (i + 1) % 40

            else:
                if i in (x, x + 1, x + 2):
                    crt += "#"

                else:
                    crt += "."

                i = (i + 1) % 40

                if i in (x, x + 1, x + 2):
                    crt += "#"

                else:
                    crt += "."

                i = (i + 1) % 40

                x += int(data[1])

    i = 0

    while i < len(crt):
        print(crt[i: i + 40])
        i += 40

if __name__ == "__main__":
    main()
