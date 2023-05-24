# Format string attack
# This is our super secret key:
SECRET = 'this-secret-string-is-hacked'

class Error:
    def __init__(self):
        pass

# A malicious user can craft a format string that
# can read data from the global namespace:
# user_input = '{error.__init__.__globals__[SECRET]}'
user_input = input("Enter input: ")

# This allows them to exfiltrate sensitive information,
# like the secret key:
# err = Error()
temp = user_input.format(error=Error())
print(temp)


## BELOW IS SAFER ALTERNATIVE
from string import Template
temp = Template(user_input).substitute(error=Error())
print(temp)

## TEMPLATE USAGE EXAMPLE
# test = "Prithivi"
# print(Template(user_input).substitute(name=test))
