import sys

def min_moves(nums):
    nums_sorted = sorted(nums)
    median = nums_sorted[len(nums_sorted) // 2]
    return sum(abs(x - median) for x in nums)

def main():
    if len(sys.argv) != 2:
        print("Usage: task4.py numbers.txt")
        return
    with open(sys.argv[1]) as f:
        nums = [int(line.strip()) for line in f if line.strip()]
    moves = min_moves(nums)
    if moves <= 20:
        print(moves)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

if __name__ == "__main__":
    main()
