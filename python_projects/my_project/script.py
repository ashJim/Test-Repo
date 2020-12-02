import math
import sys
from os import rename

import requests


# print(sys.version)
print(sys.executable)


r = requests.get("https://learneo.co")
print(r.status_code)
