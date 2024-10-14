#
# This file is part of libprovola Python library (https://github.com/io-no/libprovola).
# Copyright (c) 2024 Gabriele Digregorio. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for details.
#


def xor(first: bytes, second: bytes) -> bytes:
    """XOR two byte strings.

    Args:
        first: The first byte string.
        second: The second byte string.

    Returns:
        The XOR of the two byte strings
    """
    if len(first) > len(second):
        second = second * (len(first) // len(second)) + second[: len(first) % len(second)]
    elif len(second) > len(first):
        first = first * (len(second) // len(first)) + first[: len(second) % len(first)]
        
    return bytes([a ^ b for a, b in zip(first, second)])
