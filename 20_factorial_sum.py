# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

# Solution:

n = 1
for i in range(1, 101):
    n *= i
n = str(n)
sum = 0
for l in n:
    sum += int(l)
print(sum)

# Answer: 