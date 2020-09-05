import re
def check_time(text):
  pattern = "(1[012]|[1-9]):[0-5][0-9](\\s)?(?i)(am|pm)"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
