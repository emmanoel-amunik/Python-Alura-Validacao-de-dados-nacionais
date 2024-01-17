class Cpf:

    def __init__(self, document):
        document = str(document)

        if self.valid_cpf(document):
            self.cpf = document
        else:
            raise ValueError('"Invalid CPF"')

    def __str__(self):
        return self.format_cpf()

    @staticmethod
    def valid_cpf(document):

        if len(document) == 11:
            return True
        elif len(document) != 11:
            return False

    def format_cpf(self):
        slice_one = self.cpf[:3]
        slice_two = self.cpf[3:6]
        slice_three = self.cpf[6:9]
        slice_four = self.cpf[9:]
        return f"{slice_one}.{slice_two}.{slice_three}-{slice_four}"
