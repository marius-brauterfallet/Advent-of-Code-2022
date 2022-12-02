def main():
    f = open("input")
    data = [x.strip() for x in f.read().split("\n\n")]
    f.close()

    reqs = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    res = 0

    for passport in data:
        fields = {field: value for field, value in [x.split(":") for x in passport.split()]}

        for req in reqs:
            if req not in fields:
                break

            val = fields[req]

            if req == "byr" and not (1920 <= int(val) <= 2002):
                break

            elif req == "iyr" and not (2010 <= int(val) <= 2020):
                break

            elif req == "eyr" and not (2020 <= int(val) <= 2030):
                break

            elif req == "hgt":
                unit = val[len(val) - 2:]
                hgt = int(val[0:len(val) - 2])

                if not ((unit == "cm" and 150 <= hgt <= 193) or (unit == "in" and 59 <= hgt <= 76)):
                    break

            elif req == "hcl":
                if val[0] != "#":
                    break

                for c in val[1:]:
                    if c not in "0123456789abcdef":
                        break
                else:
                    continue

                break
            
            elif req == "ecl" and val not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                break

            elif req == "pid":
                if len(val) != 9:
                    break

                for c in val:
                    if c not in "0123456789":
                        break
                else:
                    continue

                break

        else:   # Tvilsom bruk av else ;)
            res += 1

    print(res)


if __name__ == "__main__":
    main()
