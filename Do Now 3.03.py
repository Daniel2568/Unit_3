'''
###############
Do Now 3.03
###############
1.  In script mode
Type the following code
import random
# inputs:  x (int), y (int)
# outputs: int
# 50% returns sum of x and y, 50% returns product of x and y
​
def mystery_function(x, y):
    random_number = random.randint(0,1)
    if random_number > 0:
        z = x + y
    else:
        z = x * y
    return z

mystery_function(1, 2)

2.  In your Notebook
Answer the following questions
What happens when your run this code? How do you know what the result was? Nothing happens, the result was sytax error because it says return z not print z

Keeping the function the same, rewrite the code to print out the value that the function returns.
'''
import random
# inputs:  x (int), y (int)
# outputs: int
# 50% returns sum of x and y, 50% returns product of x and y

def mystery_function(x, y):
    random_number = random.randint(0,1)
    if random_number > 0:
        z = x + y
    else:
        z = x * y
    return z

result = mystery_function(3, 10)
print(result)