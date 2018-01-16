import random

def quickSort(nums):
    l = len(nums)
    if l <= 1:
        return nums
    left = []
    right = []
    rd = random.randint(0, l-1)
    base = nums.pop(rd)
    for i in nums:
        if i < base:
            left.append(i)
        else:
            right.append(i)

    return quickSort(left) + [base] + quickSort(right)


def main():
    print quickSort([21,3,1,2,4,56,2])

if __name__ == '__main__':
    main()
