def main():
    f = open("input")
    data = [x.strip() for x in f.read().split("\n\n")]
    f.close()

    reqs = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    res = 0

    for passport in data:
        fields = {x.split(":")[0] for x in passport.split()}

        for req in reqs:
            if req not in fields:
                break
        else:   # Tvilsom bruk av else ;)
            res += 1

    print(res)


if __name__ == "__main__":
    main()
