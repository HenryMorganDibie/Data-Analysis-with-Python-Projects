# queation 1 
from email.mime import base
from tokenize import Exponent


def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
result = multiplication_or_sum(20,30)
print("resultis", result)
    
result = multiplication_or_sum(40, 30)
print("The result is", result)
    
# queston 2
print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", previous_num + i)
    
    # set it to the current number
    previous_num = i

# question 3

word = input('Enter word ')
print("Original String:", word)

# using list slicing

x = list(word)
for i in x[0::2]:
    print(i)

# question 4 
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

# question 5 
def first_last_same(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))

# question 6
# Given numberlist [10,20,34,87,58,30]
num_list = [10,20,34,87,58,30]
print('given numberlist:', num_list)
print('divisible by 5')
for num in num_list: 
    if num % 5 == 0:
        print(num)
 
# question 7
# str_x: 'Emma is good developer. Emma is a writer'
def count_emma(statement):
     print('given string', statement)    
     count = 0
     for i in range(len(statement) - 1):
            count += statement[i: i + 4] == 'Emma'
            return count

count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")

# question 8
for num in range(10):
    for i in range(num):
        print (num, end=" ") 
    print("\n")
    
# queston 9
def palindrome(number):
    print("original number", number)
    original_num = number
    
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)

#question 10
def merge_list(list1, list2):
    result_list = []
    
    for num in list1:
        if num % 2 != 0:
            
            result_list.append(num)
    
    for num in list2:
        
        if num % 2 == 0:
            
            result_list.append(num)
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))


# question 11
number = 7536
print("Given number", number)
while number > 0:
    digit = number % 10
    number = number // 10
    print(digit, end=" ")
    
#question 12
income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    tax_payable = 0

    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)

# question 13
for i in range(1,11):
  for j in range(1,11):
      print(i * j, end='')
      print()
  
  # question 14
  for i in range(6, 0, -1):
        for j in range(0, i - 1):
    print("*", end=' ')
print(" ")
  
 #question 15
# base = 2 exponent = 5.   2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)
# base = 5  exponent = 4.   5 raises to the power of 4 is: 625 i.e. (5 *5 * 5 *5 = 625)
def = exponent(base, exponent)
num = exp 
result = 1
while num > 0:
      result = result * base
      num = num - 1
      print(base,'raises to the power of', exp, 'is', result)
exponent (5, 4)
