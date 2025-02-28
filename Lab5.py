# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                result += "*"
            else:
                result += " "    

        result += "\n"       
    
    return result.strip()

# 1
# 12
# 123
# 1234
def number_pattern(n):
    pattern = '\n' .join([''.join([str(j) for j in range(1, i+1)]) for i in range(1, n+1)])

    return(pattern)
    

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    sum_of_natural_numbers = 0
    current_number = 1

    while current_number <= n:
        sum_of_natural_numbers += current_number
        current_number += 1

    
    return sum_of_natural_numbers

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    for i in range(1, n + 1):
        result += '*' * (2 * i - 1)
        result += ' ' * (n - 1)
        
    result += "\n"

    return (result.strip())