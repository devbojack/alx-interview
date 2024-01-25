#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys

if __name__ == '__main__':

    total_size, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, total_size: int) -> None:
        print("File size: {:d}".format(total_size))
        for code, count in sorted(stats.items()):
            if count:
                print("{}: {}".format(code, count))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()

            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                pass

            try:
                total_size += int(data[-1])
            except (ValueError, IndexError):
                pass

            if count % 10 == 0:
                print_stats(stats, total_size)

        print_stats(stats, total_size)

    except KeyboardInterrupt:
        print_stats(stats, total_size)
        raise
