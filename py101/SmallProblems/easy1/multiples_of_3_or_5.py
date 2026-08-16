def is_divisible_by_any(value, a_list):
    for number in a_list:
        if value % number == 0:
            return True
    return False

def multisum(target_num):
    return sum([val for val in range(3, target_num + 1) if is_divisible_by_any(val, divisors)])
    
divisors = [3, 5]

print(multisum(3))
print(multisum(5))
print(multisum(10))
print(multisum(1000))
