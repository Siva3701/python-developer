# 1. Variables and Data Types
integer_variable = 10
float_variable = 20.5
string_variable = "Hello, Python!"
boolean_variable = True

# 2. Arithmetic Operations
def arithmetic_operations(a, b):
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    div_result = a / b
    return sum_result, diff_result, prod_result, div_result

a = 15
b = 5
sum_result, diff_result, prod_result, div_result = arithmetic_operations(a, b)
print(f"Sum: {sum_result}, Difference: {diff_result}, Product: {prod_result}, Division: {div_result}")


# 3. Conditional Statements
def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number_to_check = 42
result = check_even_or_odd(number_to_check)
print(f"The number {number_to_check} is {result}")

# 4. Loops
# For Loop
print("Using for loop:")
for i in range(5):
    print(i)

# While Loop
print("Using while loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# 5. Common Data Structures
# List
sample_list = [1, 2, 3, 4, 5]
sample_list.append(6)
print("List:", sample_list)

# Dictionary
sample_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
sample_dict['email'] = 'alice@example.com'
print("Dictionary:", sample_dict)

# Tuple
sample_tuple = (10, 20, 30, 40, 50)
print("Tuple:", sample_tuple)
