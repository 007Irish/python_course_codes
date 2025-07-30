# two Types of modules in Python
# - built in modules
# - External modules
import math

import my_modules
import requests #we have to install requests module first because it's an external module (pip install requests)
print(math.sqrt(333))
my_modules.hello()
a = requests.get("https://www.instagram.com/accounts/login/?hl=en")
print(a.text)