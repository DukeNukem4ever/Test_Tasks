import sys

numbers = []

with open(sys.argv[1], "r", encoding="utf-8") as num_file:
    nums = num_file.readlines()
    for n in nums:
        numbers.append(int(n))

    numbers.sort()
    median = numbers[len(numbers) // 2]
    print(sum(abs(number - median) for number in numbers))
