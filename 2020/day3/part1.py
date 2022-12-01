def main():
    f = open("input")
    m = [x.strip() for x in f]
    f.close()

    width = len(m[0])
    x = 0
    trees = 0
    
    for line in m:
        if line[x] == "#":
            trees += 1

        x = (x + 3) % width

    print(trees)

if __name__ == "__main__":
    main()
