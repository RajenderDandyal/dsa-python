# factorial

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num*factorial(num-1)


print(factorial(5))


def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return num + sum_of_digits(num-1)


print(sum_of_digits(5))


def power_of_num(num, pow):
    if pow == 0:
        return 1
    else:
        return num*power_of_num(num, pow-1)


print(power_of_num(122, 3))
arr = []


def decimal_to_binary(num):
    if num/2 <= 1:
        arr.append(1)
    elif num % 2 == 0:
        arr.append(0)
        decimal_to_binary(num/2)
    elif num % 2 != 0:
        arr.append(1)
        decimal_to_binary(num/2)


decimal_to_binary(112)
print(arr)


def twoSum(nums, target):
    ind = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                ind.append(i)
                ind.append(j)
                return ind

    # return ind


print('twoSum', twoSum([2, 7, 11, 15], 9))


def palindrome(num):
    num = str(num)
    rev_num = num[::-1]
    if rev_num == num:
        return True
    else:
        return False


print(palindrome(1213))


def isValid(str):
    arr = list(str)
    obj = {
        '(': ")",
        "{": "}",
        "[": ']'
    }

    for i in range(len(arr)):
        for j in obj:
            if arr[i] == j:
                if arr[i+1] == obj[j]:
                    obj[j] = True
                else:
                    obj[j] = False
    result = True
    print(obj)
    for value in obj.values():
        if not value:
            result = value

    return result


print(isValid('(]'))
