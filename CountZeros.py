n = int(input("Enter a number: "))
target = int(input("Enter a target variable: ")) # 0 in this case

def numberCount(n, target):
    count = 0
    while (n > 0):
        if (n % 10 == target):
            count = count + 1
        n = n // 10
    return count

print("Count of {}".format(target),":",numberCount(n, target))




