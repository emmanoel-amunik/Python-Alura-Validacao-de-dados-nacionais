from document import Document
import re


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
