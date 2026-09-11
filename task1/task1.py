import sys

def get_path(n, m):
    path = []
    current = 1
    while True:
        path.append(current)
        current = (current - 1 + m - 1) % n + 1
        if current == 1:
            break
    return path

def main():
    default = [6, 3, 5, 4]

    args = sys.argv[1:]
    if len(args) == 4:
        nums = list(map(int, args))
    else:
        print("Аргументы не переданы, используются значения по умолчанию:", *default)
        nums = default

    n1, m1, n2, m2 = nums
    path1 = get_path(n1, m1)
    path2 = get_path(n2, m2)
    print(''.join(map(str, path1 + path2)))

if __name__ == "__main__":
    main()
