import re
string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
test_string = "chercher@tech"

if(string_check.search(test_string) == None):
    print("Contains NO Special Characters.")
else:
    print("Contains Special Characters.")
    print(string_check.search(test_string)) 