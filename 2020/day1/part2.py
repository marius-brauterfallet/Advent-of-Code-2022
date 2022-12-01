def main():
    f = open("input")
    s = {int(x) for x in f}
    f.close()

    for x in s:
        for y in s:
            if y != x:
                z = 2020 - x - y

                if z in s:
                    print(x * y * z)
                    return

if __name__ == "__main__":
    main()
