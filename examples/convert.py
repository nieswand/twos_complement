#!/usr/bin/env python3

from twos_complement import to_signed, to_unsigned

bit_width = 8
x = 170 # 0b10101010
pattern = f"{x:b}"

y = to_signed(value=x, bit_width=bit_width)
print(f"Interpreting {pattern} as {bit_width}-bit two's complement: {y}")

z = to_unsigned(value=y, bit_width=bit_width)
print(f"Interpreting {pattern} as {bit_width}-bit unsigned integer: {z}")

assert x == z
