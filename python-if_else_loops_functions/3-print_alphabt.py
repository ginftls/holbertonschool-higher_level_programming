#!/usr/bin/python3
for char in range(97, 123):
    if char != 101 and char != 113:  # 101 is 'e', 113 is 'q'
        print(chr(char), end="")
