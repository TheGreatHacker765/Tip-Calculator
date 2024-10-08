import math
var_meal_cost = int(input("How much was the meal?"))
choices = ["excelent", "good", "poor"]
choice = False
while not choice:
  var_service = input("Was the service good, excelent, or poor?").lower
  if var_service in choices:
    choice = True
  else:
    choice = false
