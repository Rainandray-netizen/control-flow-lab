# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

side_1 = input("Enter a Length: ")
side_2 = input("Enter a Length: ")
side_3 = input("Enter a Length: ")

if side_1 == side_2 == side_3:
  triangle_type = 'equalateral'
elif (side_1 == side_2 != side_3) or (side_1 != side_2 == side_3) or (side_1 == side_3 != side_2):
  triangle_type = 'isosceles'
else:
  triangle_type = 'scalene'


print(f"A triangle with sides of {side_1}, {side_2}, and {side_3} is a(n) {triangle_type} triangle")