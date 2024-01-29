from acess_cep import AddressSearch
import requests


cep = "01001000"
obj_cep = AddressSearch(cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(type(r.text)

a = obj_cep.cep_access()

print(a.text)
print(a.json())
