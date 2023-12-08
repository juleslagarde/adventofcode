import sys


grid = [line[:-1] for line in sys.stdin]
maxX = len(grid[0])-1
maxY = len(grid)-1

for line in grid:
    print(line)


def issymbol(c):
    return c != "." and not '0' <= c <= '9'


def isdigit(c):
    return '0' <= c <= '9'


def part1():
    def isvalid(x, y, length):
        for i in range(max(0, y-1), min(maxY, y+1)+1):  # 3 lines
            for j in range(max(0, x-length), min(maxX, x+1)+1):  # 3 columns + length-1
                c = grid[i][j]
                if issymbol(c):
                    print(f"({x},{y},{length}) {i} {j} : {c}")
                    return True
        return False

    sum = 0
    num = ""
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if not isdigit(c):
                continue
            num += c
            if (x == maxX or not isdigit(line[x+1])):
                if isvalid(x, y, len(num)):
                    print(f"valid: {num}")
                    sum += int(num)
                num = ""
    print(sum)


def part2():
    def get_char(x, y):
        try:
            return grid[y][x]
        except IndexError:
            return '.'

    def get_num(x, y):
        c = get_char(x, y)
        if not isdigit(c):
            return None
        num = c
        for dir in [-1, 1]:
            dx = dir
            while isdigit(c := get_char(x + dx, y)):
                num = c + num if dir == -1 else num + c
                dx += dir
        return int(num)

    def adjacents_numbers(x, y):
        nums = []
        for dy in [-1, 0, 1]:
            if isdigit(get_char(x, y+dy)):
                # if middle char is a digit there can only be one number on the line
                nums.append(get_num(x, y+dy))
            else:
                # else there can be a maximum of 2 numbers
                if (num := get_num(x-1, y+dy)):
                    nums.append(num)
                if (num := get_num(x+1, y+dy)):
                    nums.append(num)
        return nums

    sum = 0
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c != "*":
                continue
            nums = adjacents_numbers(x, y)
            if len(nums) == 2:
                a, b = nums
                sum += a*b
    print(f"sum: {sum}")




part2()


