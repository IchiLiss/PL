import sys

def read_circle(path):
    with open(path) as f:
        cx, cy = map(float, f.readline().split())
        a, b = map(float, f.readline().split())
    return cx, cy, a, b

def read_dot(path):
    dot = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = map(float, line.split())
                dot.append((x, y))
    return dot

def classify(px, py, cx, cy, a, b):
    val = ((px - cx) ** 2) / (a ** 2) + ((py - cy) ** 2) / (b ** 2)
    eps = 1e-12
    if abs(val - 1) < eps:
        return 0
    elif val < 1:
        return 1
    else:
        return 2

def main():
    if len(sys.argv) != 3:
        print("Usage: task2.py circle.txt dot.txt")
        return
    cx, cy, a, b = read_circle(sys.argv[1])
    points = read_dot(sys.argv[2])
    for px, py in dot:
        print(classify(px, py, cx, cy, a, b))

if __name__ == "__main__":
    main()
