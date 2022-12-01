def main():
    f = open("input")

    max = 0
    sum = 0
    
    for line in f:
        if line.strip() == "":
            if sum > max:
                max = sum

            sum = 0

        else:
            sum += int(line)

    print(max)
    f.close()

if __name__ == "__main__":
    main()
