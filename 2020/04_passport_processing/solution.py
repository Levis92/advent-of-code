# Format data
from dataclasses import dataclass
from typing import Optional
import re


@dataclass
class PassPort:
    byr: Optional[int] = None  # Birth Year
    iyr: Optional[int] = None  # Issue Year
    eyr: Optional[int] = None  # Expiration Year
    hgt: Optional[str] = None  # Height
    hcl: Optional[str] = None  # Hair Color
    ecl: Optional[str] = None  # Eye Color
    pid: Optional[str] = None  # Passport ID
    cid: Optional[int] = None  # Country ID

    def is_valid(self):
        return all(
            field is not None
            for field in (
                self.byr,
                self.iyr,
                self.eyr,
                self.hgt,
                self.hcl,
                self.ecl,
                self.pid,
            )
        )

    def validate_hgt(self):
        val = int(val) if (val := str(self.hgt)[:-2]).isnumeric() else val
        unit = str(self.hgt)[-2:]
        if unit == "cm":
            return 150 <= val <= 193
        if unit == "in":
            return 59 <= val <= 76
        return False

    def validate_hcl(self):
        if not len(hcl := self.hcl) == 7:
            return False
        return hcl[0] == "#" and len(re.match("^[a-f0-9]*$", hcl[1:]).group(0)) == 6

    def strict_is_valid(self):
        if not self.is_valid():
            return False
        if not (1920 <= self.byr <= 2002):
            return False
        if not (2010 <= self.iyr <= 2020):
            return False
        if not (2020 <= self.eyr <= 2030):
            return False
        if not self.validate_hgt():
            return False
        if not self.validate_hcl():
            return False
        if not self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        if not (len(self.pid) == 9 and self.pid.isnumeric()):
            return False
        return True


with open("data.txt") as f:
    lines = (l.strip() for l in f.readlines())

passports = []
current_passport = PassPort()
for line in lines:
    if line == "":
        passports.append(current_passport)
        current_passport = PassPort()
    else:
        fields = (
            (key, val) for key, val in (pair.split(":") for pair in line.split(" "))
        )
        for key, val in fields:
            setattr(
                current_passport,
                key,
                int(val) if val.isnumeric() and key != "pid" else val,
            )
passports.append(current_passport)


"""
--- Part One ---
"""

print(sum(1 for p in passports if p.is_valid()))


"""
--- Part Two ---
"""
print(sum(1 for p in passports if p.strict_is_valid()))
