from document import Document
import re
from cellphonesBR import CellphonesBR


ex_cnpj = "35379838000112"
ex_cpf = "32007832062"
document = Document.make_document(ex_cpf)
document2 = Document.make_document(ex_cnpj)

print(document)
print(document2)


# email search


pattern = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"  # email
text = "aaabbbcc rodrigo123@gmail.com.br"
answer = re.search(pattern, text)

print(answer.group())


# cellphone search


cellphone = "552126481234"

# pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
# answer = re.search(pattern, cellphone)
# print(answer.group())

cellphone_object = CellphonesBR(cellphone)
print(cellphone_object)
