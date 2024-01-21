from validate_docbr import CPF


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
            validator = CPF()
            return validator.validate(document)
        else:
            raise ValueError("Number of digits invalid!")

    def format_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)
