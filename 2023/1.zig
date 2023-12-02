const std = @import("std");
const io = std.io;
const ArrayList = std.ArrayList;

// step1 result with STEP2=false, step2 result with STEP2=true
const STEP2 = true;

const digits = [_][]const u8{ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

fn match(haystack: []const u8, needle: []const u8) bool {
    var i: usize = 0;
    while (i < haystack.len and i < needle.len and haystack[i] == needle[i]) {
        i += 1;
    }
    return i == needle.len; //if we reached the end of the needle that means match
}

fn getDigit(i: usize, line: []const u8) ?u8 {
    if (line[i] >= '1' and line[i] <= '9') {
        return line[i] - '0';
    } else {
        if (!STEP2) return null;
        for (digits, 0..) |digit, j| {
            if (match(line[i..], digit)) {
                return @as(u8, @intCast(j + 1));
            }
        }
        return null;
    }
}

pub fn main() anyerror!void {
    var buffer: [128]u8 = undefined;
    const stdin = io.getStdIn().reader();
    var sum: u32 = 0;
    while (true) {
        const maybeLine = try stdin.readUntilDelimiterOrEof(&buffer, '\n');
        if (maybeLine == null) break;
        const line = maybeLine.?;

        var first: u8 = 0;
        var last: u8 = 0;

        var i: usize = 0;
        while (i < line.len and first == 0) : (i += 1) {
            if (getDigit(i, line)) |d| {
                first = d;
                break;
            }
        }

        i = line.len;
        while (i > 0 and last == 0) : (i -= 1) {
            if (getDigit(i - 1, line)) |d| {
                last = d;
                break;
            }
        }
        sum += first * 10 + last;
    }
    std.debug.print("sum : {}\n", .{sum});
}
