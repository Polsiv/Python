import re

text = "My cat is on the roof and the cother cat is at the garden"
matches = re.findall("cat", text)
print(matches)

# /-----------------------------------------------------------------------

text2 = "today is 11/11/2024, tomorrow is 12/11/2024"
# \d{2} Finds a digit of lenght 2
# \/ means / (have to scape it)
print(re.findall(r"\d{2}\/\d{2}\/\d{4}", text2))

# /-----------------------------------------------------------------------

text3 = "Users can find support at soporte@hack4u.io or info@hack4u.io"
# We want to print 2 tuples [('soporte', 'hack4u.io), (info, hack@u.io)]
#\w+ alphanumeric characters, + <- this means repeatable
# \. means .
# \w{2, } alphanumeric characters from length 2 to ...
# () @ () separates the tuples
print(re.findall(r"(\w+)@(\w+\.\w{2,})", text3))

# /-----------------------------------------------------------------------

text4 = "My cat is on the roof and my dog is at the garden"
new_text4 = re.sub("cat", "dog", text4)
print(new_text4)

# /-----------------------------------------------------------------------

text5 = "Field1,Field2,Field3,Field4,Field5"
new_text5 = re.split(",", text5)
print(new_text5)


# /-----------------------------------------------------------------------


# \b starts with and ends with
text6 = "car, cart, masticar y magicartp"
print(re.findall(r"\bcar\b", text6))


# /-----------------------------------------------------------------------
text7 = "today is 13/11/2024, tomorrow is 14/11/2024"
pattern = r"\b(\d{2}\/\d{2}\/\d{4})\b"

for match in re.finditer(pattern, text7):
    print(match)
    print(match.group(0))
    print(f"starts at: {match.start()}")
    print(f"ends at: {match.end()}")
    print(f"bounds: {match.span()}")