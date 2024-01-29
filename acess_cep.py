import requests


class AddressSearch:

    def __init__(self, cep):
        cep = str(cep)
        if self.valid_cep(cep):
            self.cep = cep
        else:
            raise ValueError("INVALID CEP")

    def __str__(self):
        return self.format_cep()

    @staticmethod
    def valid_cep(cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def cep_access(self):
        url = f"https://viacep.com.br/ws/{self.cep}/jason/"
        r = requests.get(url)
        date = r.json()
        return (

        )
