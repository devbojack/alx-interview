#!/usr/bin/env python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """

    def is_start_of_char(byte):
        return (byte & 0b10000000) == 0b00000000

    def is_valid_continuation_bytes(num_bytes):
        nonlocal data_index
        for _ in range(num_bytes):
            data_index += 1
            if data_index >= len(data) or \
                    not ((data[data_index] & 0b11000000) == 0b10000000):
                return False
        return True

    data_index = 0
    while data_index < len(data):
        current_byte = data[data_index]

        # Single-byte character
        if is_start_of_char(current_byte):
            data_index += 1

        # Multi-byte character
        else:
            # Determine the no. of bytes in the current character
            num_bytes = 0
            mask = 0b10000000
            while (current_byte & mask) == mask:
                num_bytes += 1
                mask >>= 1

            # Check if the no. of following bytes is valid
            if num_bytes < 2 or num_bytes > 4 or \
                    not is_valid_continuation_bytes(num_bytes - 1):
                return False

            data_index += 1

    return True
