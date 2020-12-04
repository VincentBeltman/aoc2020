import re


def parse_passports(blob):
    result = []
    for blob_item in blob.split("\n\n"):
        passport_split = []
        for line in blob_item.split("\n"):
            passport_split.extend(line.split(" "))
        passport_parsed = {}
        for item in passport_split:
            key, value = item.split(":")
            passport_parsed[key] = value
        result.append(passport_parsed)
    return result


def passport_is_valid(passport_to_validate):
    valid = True
    if valid:
        valid = "byr" in passport_to_validate and len(passport_to_validate["byr"]) == 4 and 1920 <= int(passport_to_validate["byr"]) <= 2002

    if valid:
        valid = "iyr" in passport_to_validate and len(passport_to_validate["iyr"]) == 4 and 2010 <= int(passport_to_validate["iyr"]) <= 2020

    if valid:
        valid = "eyr" in passport_to_validate and len(passport_to_validate["eyr"]) == 4 and 2020 <= int(passport_to_validate["eyr"]) <= 2030

    if valid:
        valid = "hgt" in passport_to_validate
        if valid:
            height_matched = re.match(r"(\d+)(cm|in)", passport_to_validate["hgt"])
            valid = (height_matched is not None and
                     ((height_matched.group(2) == "in" and 59 <= int(height_matched.group(1)) <= 76) or
                      (height_matched.group(2) == "cm" and 150 <= int(height_matched.group(1)) <= 193)))

    if valid:
        valid = "hcl" in passport_to_validate and re.match("^#[0-9a-f]{6}$", passport_to_validate["hcl"]) is not None

    if valid:
        valid = "ecl" in passport_to_validate and re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", passport_to_validate["ecl"]) is not None

    if valid:
        valid = "pid" in passport_to_validate and re.match("^[0-9]{9}$", passport_to_validate["pid"]) is not None

    return valid


if __name__ == "__main__":
    with open("test2.txt") as file:
        passports = parse_passports(file.read())
        nrOfValidPassports = 0
        for passport in passports:
            if passport_is_valid(passport):
                nrOfValidPassports += 1
        print(nrOfValidPassports)
