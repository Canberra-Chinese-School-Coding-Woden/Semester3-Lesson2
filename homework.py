# Homework: this program gives a new list containing numbers based on numbers in the old_list.
# Change the expression, so that the sum of all the numbers in new_list is 10.
# You can try a lot of things, like i*2, i-3, i*i..., but only one will work!
# After you change the expression, run this script in a compiler. A good online compiler is
# https://www.w3schools.com/python/trypython.asp?filename=demo_compiler
# todo: change "expression" to something

old_list = [12, 6, 9, 3]
new_list = [expression for i in old_list]

print(new_list)

# don't make changes to the following code
if (sum(new_list)==10):
    print("Awesome! We got a sum of 10.")
else:
    print("The sum of our new list isn't 10... maybe try something else")



