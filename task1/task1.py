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
    if len(sys.argv) != 5:
        print("Usage: task1.py n1 m1 n2 m2")
        return
    n1, m1, n2, m2 = map(int, sys.argv[1:5])
    path1 = get_path(n1, m1)
    path2 = get_path(n2, m2)
    result = ''.join(map(str, path1 + path2))
    print(result)

if __name__ == "__main__":
    main()
