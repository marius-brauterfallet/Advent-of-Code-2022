def main():
    x = 1
    res = 0
    cycle = 1

    with open("input") as f:
        for line in f:
            data = line.split()
            mod = cycle % 40

            if data[0] == "noop":
                if mod == 20:
                    res += (cycle * x)

                cycle += 1

            else:
                if mod == 20:
                    res += (cycle * x)

                elif mod == 19:
                    res += ((cycle + 1) * x)

                cycle += 2
                x += int(data[1])
    
    print(res)


if __name__ == "__main__":
    main()
