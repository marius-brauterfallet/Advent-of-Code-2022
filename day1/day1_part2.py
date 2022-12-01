def main():
    f = open("input")

    m = list()
    s = 0
    
    for line in f:
        if line.strip() == "":
            m.append(s)
            s = 0

        else:
            s += int(line)

    print(sum(sorted(m, reverse = True)[0:3]))
    f.close()

if __name__ == "__main__":
    main()
