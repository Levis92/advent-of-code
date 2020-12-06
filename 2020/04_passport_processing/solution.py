# Format data
from dataclasses import dataclass
from typing import Optional, Union
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
        height = int(h) if (h := str(self.hgt)[:-2]).isnumeric() else h
        unit = str(self.hgt)[-2:]
        return (unit == "cm" and 150 <= height <= 193) or (
            unit == "in" and 59 <= height <= 76
        )

    def validate_hcl(self):
        match = re.match("^#[a-f0-9]*$", str(self.hcl))
        return match and len(match.group()) == 7

    def strict_is_valid(self):
        return all(
            [
                self.is_valid(),
                self.byr and 1920 <= self.byr <= 2002,
                self.iyr and 2010 <= self.iyr <= 2020,
                self.eyr and 2020 <= self.eyr <= 2030,
                self.validate_hgt(),
                self.validate_hcl(),
                self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                self.pid and len(self.pid) == 9 and self.pid.isnumeric(),
            ]
        )


with open("data.txt") as f:
    lines = (l.replace("\n", " ") for l in f.read().strip().split("\n\n"))


def get_value(key: str, val: str) -> Union[str, int]:
    return int(val) if val.isnumeric() and key != "pid" else val


def create_passport(line: str) -> PassPort:
    fields = ((key, val) for key, val in (pair.split(":") for pair in line.split(" ")))
    return PassPort(**{key: get_value(key, val) for key, val in fields})


passports = [create_passport(l) for l in lines]


"""
--- Part One ---
"""
print(sum(1 for p in passports if p.is_valid()))


"""
--- Part Two ---
"""
print(sum(1 for p in passports if p.strict_is_valid()))
