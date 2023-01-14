#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = 0
    if len(sys.argv) < 2:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print(f"{len(sys.argv) - 1} argument:")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
    for i in sys.argv:
        if num > 0:
            print(f"{num}: {i}")
        num += 1
