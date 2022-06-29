def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
print ('Type a number')
try:
    n = int(input())
except ValueError:
    print('You have to put integer in')
    input ('press enter')

while n != 1:
    n = collatz(n)



input ('press enter')
