from validate_docbr import CPF
from validate_docbr import CNPJ


class Document:

    @staticmethod
    def make_document(document):
        if len(document) == 11:
            return DocCpf(document)

        elif len(document) == 14:
            return DocCnpj(document)

        else:
            raise ValueError('"Number of digits invalid!"')


class DocCpf:

    def __init__(self, document):
        if self.valid_cpf(document):
            self.cpf = document

        else:
            raise ValueError('"Invalid CPF"')

    def __str__(self):
        return self.format_cpf()

    @staticmethod
    def valid_cpf(doc_number):
        validator = CPF()
        return validator.validate(doc_number)

    def format_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)


class DocCnpj:

    def __init__(self, document):
        if self.valid_cnpj(document):
            self.cnpj = document

        else:
            raise ValueError('"Invalid CNPJ"')

    def __str__(self):
        return self.format_cnpj()

    @staticmethod
    def valid_cnpj(doc_number):
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(doc_number)

    def format_cnpj(self):
        cnpj_mark = CNPJ()
        return cnpj_mark.mask(self.cnpj)
