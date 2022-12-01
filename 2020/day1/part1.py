def main():
    f = open("input")
    inp = {int(x) for x in f}
    f.close()

    for x in inp:
        y = 2020 - x
        if y in inp:
            print(x * y)
            return

if __name__ == "__main__":
    main()
