import sys
import re

step2 = True

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = {d: i+1 for i, d in enumerate(digits)}
digit_pattern = re.compile("("+"|".join(digits.keys())+")")


def get_digit(i, line):
    if '0' <= c <= '9':
        return c
    elif step2 and (m := digit_pattern.match(line, i)):
        return digits[m.group(1)]
    return None


sum = 0
for line in sys.stdin:
    first = None
    last = None
    # searching from the start
    for i, c in enumerate(line):
        if (first := get_digit(i, line)) is not None:
            break
    # searching from the end
    for i, c in reversed(list(enumerate(line))):
        if (last := get_digit(i, line)) is not None:
            break
    print(str(first)+str(last))
    sum += int(first)*10+int(last)

print(f"sum: {sum}")
