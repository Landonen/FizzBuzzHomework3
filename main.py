# 0-100
# Если число делится на 3 без остатка - написать число и Fizz
# Если число делится на 5 без остатка - написать число и Buzz
# Если число делится на 3 и на 5 без остатка - написать число и FizzBuzz

for FizzBuzz in range(101):
    if FizzBuzz % 3 == 0 and FizzBuzz % 5 == 0:
        print(FizzBuzz, 'Fizz')
    elif FizzBuzz % 3 == 0:
        print(FizzBuzz, 'Buzz')
    elif FizzBuzz % 5 == 0:
        print(FizzBuzz, 'FizzBuzz')
