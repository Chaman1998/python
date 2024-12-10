def sum_all(*args):
    
    # print(*args)
    # print(args)

    for i in args:
        print(i * 2)
    return sum(args)

print("Sum: ", sum_all(1,2))

# print("Sum: ", sum_all(1,2,3))
# print("Sum: ", sum_all(1,2,3,4))