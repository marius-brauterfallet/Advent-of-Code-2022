def main():
    ids = list()

    with open("input") as f:
        highest_id = 0

        for line in f:
            low, high = 0, 127

            for c in line[0: 7]:
                if c == "F":
                    high = low + (high - low) // 2

                else:
                    low = high - (high - low) // 2

            row = low
            low, high = 0, 7

            for c in line[7:]:
                if c == "L":
                    high = low + (high - low) // 2

                else:
                    low = high - (high - low) // 2

            column = low
            seat_id = row * 8 + column

            ids.append(seat_id)


        print(highest_id)
        ids.sort()
        prev = 0

        for i in ids:
            if prev == i - 2:
                print(i - 1)

            prev = i



if __name__ == "__main__":
    main()
