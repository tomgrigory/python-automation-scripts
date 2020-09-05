import re
def check_web_address(text):
  pattern = "^[a-zA-Z.]+[A-Z0-9._]+[enter code hereA-Za-z0-9-]+[.com|.info|.edu|.org|.US]+"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True
