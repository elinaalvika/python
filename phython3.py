print("Hello")
def reizinajums_summa_(skaitlis1,skaitlis2): #1.uzd
    if skaitlis1 * skaitlis2 <= 1000:
        rezultats = skaitlis1 * skaitlis2
        return "reizinajums ir: " + str(rezultats)
    else:
        rezultats = skaitlis1 + skaitlis2
        return "summa ir: " + str(rezultats)
print(reizinajums_summa_(20,30))
print(reizinajums_summa_(40,30))

def drukat_summas(skaits): #2.uzd
    ieprieksejais = 0
    for esosais in range(skaits):
        summa = esosais + ieprieksejais
        print("esosais skaitlis: " + str(esosais) + "ieprieksejais:" +str(ieprieksejais) + "summa: " +str(summa))
        ieprieksejais = esosais
    return

drukat_summas(10)

def drukat_burtus(teksts): #3.uzd
    rezultats = ""
    for indekss in range(0,len(teksts),2):
        rezultats += teksts[indekss]
    return rezultats

print(drukat_burtus("Agnese"))


def nonemtBurtus(teksts, cikBurti):  #4.uzd
    jaunaisTeksts = teksts[cikBurti:]
    return jaunaisTeksts

print(nonemtBurtus("mani sauc elīna",1))

def check_first_last(numbers):           #5.uzd
    if numbers[0] == numbers[-1]:
        return True
    else:
        return False

number_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

result_x = check_first_last(number_x)
result_y = check_first_last(numbers_y)

print("Given list:", number_x)
print("Result is", result_x)

print("Given list:", numbers_y)
print("Result is", result_y)

def find_divisible_by_5(numbers):          #6.uzd
    divisible_numbers = [num for num in numbers if num % 5 == 0]
    return divisible_numbers

given_list = [10, 20, 33, 46, 55]
divisible_numbers = find_divisible_by_5(given_list)

print("Given list is:", given_list)
print("Divisible by 5:", ', '.join(map(str, divisible_numbers)))

rows = 5          #8.uzd

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()


def check_palindrome(number):           #9.uzd
    original_number = number
    reverse_number = 0

    while number > 0:
        remainder = number % 10
        reverse_number = reverse_number * 10 + remainder
        number = number // 10

    if original_number == reverse_number:
        return True
    else:
        return False

number1 = 121
number2 = 125

is_palindrome1 = check_palindrome(number1)
is_palindrome2 = check_palindrome(number2)

print("Original number:", number1)
print("Yes. Given number is a palindrome number." if is_palindrome1 else "No. Given number is not a palindrome number.")

print("Original number:", number2)
print("Yes. Given number is a palindrome number." if is_palindrome2 else "No. Given number is not a palindrome number.")

list1 = [10, 20, 25, 30, 35]     #10.uzd
list2 = [40, 45, 60, 75, 90]

result_list = [element for element in list1 if element in list2]

print("Result list:", result_list)

rows = 5    #14.uzd

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

