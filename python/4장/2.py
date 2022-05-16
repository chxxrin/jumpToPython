def avg_numbers(*args):
    result = 0
    for i in args:
        result = result + i
    return result/len(args)

result1 = avg_numbers(1,2)
result2 = avg_numbers(1,2,3,4,5)

print(result1)
print(result2)

