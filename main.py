from document import Document


ex_cnpj = "35379838000112"
ex_cpf = "32007832062"
document = Document.make_document(ex_cpf)
document2 = Document.make_document(ex_cnpj)

print(document)
print(document2)
