# Code by Thoriq AS

# TODO: Jaden Casing Strings
#Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

def toJadenCase(string):
    return ' '.join(i.capitalize() for i in string.split(" "))

# TODO: Find Uniq Numbers
# Examples [1,1,1,2,1,1,] = 2

def find_uniq(arr):
    # your code here
    arr.sort()

    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]
        print()

    return n

# TODO: Return Negative
def make_negative( number ):
    result = number
    if number > 0:
        result = -abs(number)
    elif number <0:
        pass
    elif number == 0:
        result = 0
    return result

print(make_negative(0))

# TODO:
def approx_equals(a, b):
    a = round(a, 2)
    b = round(b, 2)
    if a == b:
        return True
    else:
        return False

print(approx_equals(98.7655, 98.7654999))

# TODO: Check Same Case
# Write a function that will check if two given characters are the same case.

# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0

def same_case(a, b):
    if a.isalpha() and b.isalpha():
        if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
            return 1
        else:
            return 0
    else:
        return -1

# TODO: A Needle in the Haystack
# Can you find the needle in the haystack? Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle, so:
# Example(Input --> Output) # ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"

def find_needle(haystack):
    count=0
    for word in  haystack:
        if word == 'needle':
            print(f"found the needle at position {count}")
        count= count+1

find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])

def find_needle(haystack):
    return "found the needle at position {}".format(haystack.index("needle"))

def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'

# TODO: Beginner - Lost Without a Map
# Given an array of integers, return a new array with each value doubled.
# For example: [1, 2, 3] --> [2, 4, 6]

def maps(a):
    result = []
    for i in a:
        add = i * 2
        result.append(add)
    return result

def maps(a):
    return map(lambda x:2*x, a)

# TODO: Make UpperCase

def make_upper_case(s):
    return s.upper()

# TODO: Sum of two lowest positive integers

def sum_two_smallest_numbers(numbers):
    result = sorted(numbers)
    add = result[0] + result[1]
    return add

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# TODO: Grasshopper - Summation

def summation(num):
    result = 0
    for i in range(0, num+1):
        result += i
    return result

# TODO: Sum of Positive

def positive_sum(arr):
    result = 0
    for i in arr:
        if i > 0:
            result += i
    return (result)

positive_sum([1,-2,3,4,5]) # 13

# TODO: Find the smallest integer in the array
def find_smallest_int(arr):
    result = sorted(arr)
    return result[0]

print(find_smallest_int([78, 56, -2, 12, 8, -33]))

# TODO: Remove First and Last Characters

def remove_char(s):
    result1 = list(s)
    result1.pop(0)
    result1.pop(-1)

    str=""
    for i in result1:
        str +=i
    return str

remove_char("Split")

def remove_char(s):
    return s[1 : -1]

# TODO: Calculate Average
def find_average(numbers):
    if not numbers:
        return 0
    else:
        result =0
        for i in numbers:
            result += i
        return result//len(numbers)
        # return sum(numbers)/len(numbers)

print(find_average([1,2,3]))

# TODO: Strings to Number
def string_to_number(s):
    return int(s)

print(string_to_number("1234"))

# TODO: Beginner Series #1 School Paperwork
def paperwork(n, m):
    if n<0 or m<0:
        return 0
    else:
        return n * m

# TODO: Descending Order
def descending_order(num):
    print((str(num)[::-1]))

def Descending_Order(num):
    num_list = list(map(int,str(num)))
    num_list = sorted(num_list,reverse=True)
    output =  ''.join(map(str, num_list))
    return int(output)

print(descending_order(15))

# TODO: Convert number to reversed array of digits
def digitize(n):
    result = str(n)[::-1]
    return [int(i) for i in str(result)]

def digitize(n):
    return map(int, str(n)[::-1])

# TODO: Basic Mathematical Operations

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1/value2

def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))

# TODO: Calculate BMI
def bmi(weight, height):
    bmi=weight/height**2
    if bmi <= 18.5: return "Underweight"

    if bmi <= 25.0: return "Normal"

    if bmi <= 30.0: return "Overweight"

    if bmi > 30: return "Obese"

def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]

# TODO: DNA to RNA Conversion
def dna_to_rna(dna):
    result = dna.replace("T","U")
    return result

# TODO: Invert Value
def invert(lst):
    return [-x for x in lst]

# TODO: High And Low
def high_and_low(numbers):
    result = numbers.split(" ")
    result = sorted(result, key=int)
    return result[-1] + " " + result[0]

# TODO: L1 Set Alarm
def set_alarm(employed, vacation):
    if employed==True and vacation==False:
        return True
    else:
        return False

# TODO: Reverse Word
def reverse_words(text):
    words = text.split(' ')
    newWords = [word[::-1] for word in words]
    reverse_sentence = ' '.join(newWords)
    return reverse_sentence

# TODO: Find Maximum and Minimum Values of a List

def minimum(arr):
    result = sorted(arr)
    return result[-1]

def maximum(arr):
    result = sorted(arr)
    return result[0]

print(minimum([-52, 56, 30, 29, -54, 0, -110]))