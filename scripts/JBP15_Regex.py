# What is RegEx?
# - RegEx or also known as Regular Expression is a set of character that forms a seacrh pattern
# - We use RegEx to check for string that satisfied the search pattern
# - We use RegEx to look for specific string that satisfied the search pattern

import re

pattern = r"^[A-Z][a-z0-9]+T$"
pattern_obj = re.compile(r"^[A-Z][a-z0-9]+T$")
str1 = "alpha01"
str2 = "Alpha01"
str3 = "alpha01T"
str4 = "Alpha01T"
str5 = "Alpha0123T"

if re.match(pattern, str1):
    print("str1 matched with given pattern")
print(re.match(pattern, str2))
print(re.match(pattern, str3))
print(re.match(pattern, str4))
if pattern_obj.match(str5):
    print("str5 matched with the given pattern object!")


some_text = """There is several emails inside this text.
One of them is test@somemail.com. There is also cubaan@yey.com.
Lastly we have cubatest@mail.gov.my and of course all of this email is a fake one!"""

email_pattern = re.compile(r"\w+@\w+(?:\.[a-zA-Z]{2,})+")
x = email_pattern.findall(some_text)
print(x)
