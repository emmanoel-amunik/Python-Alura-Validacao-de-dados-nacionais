import re
from cellphonesBR import CellphonesBR


cellphone = "552126481234"

# pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
# answer = re.search(pattern, cellphone)
# print(answer.group())

cellphone_object = CellphonesBR(cellphone)
print(cellphone_object)
