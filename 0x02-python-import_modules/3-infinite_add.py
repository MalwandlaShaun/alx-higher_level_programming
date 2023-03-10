#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    length = len(argv) - 1
    total = 0
    for i in range(length):
        total += int(argv[i + 1])
    print("{}".format(total))
