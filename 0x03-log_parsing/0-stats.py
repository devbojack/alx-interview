#!/usr/bin/env python3
"""Reads stdin line by line and computes metrics"""
import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0

try:
    for line in sys.stdin:
        # Split the line into components
        parts = line.split()

        # Check if the line follows the specified format
        if len(parts) >= 9 and parts[8].isdigit():
            # Extract relevant information
            status_code = int(parts[8])
            file_size = int(parts[9])

            # Update metrics
            total_size += file_size
            status_codes[status_code] += 1
            lines_processed += 1

        # Print statistics every 10 lines
        if lines_processed % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    # Handle keyboard interruption and print final statistics
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
