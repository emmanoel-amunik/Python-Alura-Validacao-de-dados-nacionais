import re


class CellphonesBR:
    def __init__(self, cell_number):
        if self.valid_cellphone_number(cell_number):
            self.number = cell_number
        else:
            raise ValueError("Invalid Cellphone Number!")

    def __str__(self):
        return self.format_number()

    @staticmethod
    def valid_cellphone_number(cell_number):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.findall(pattern, cell_number)
        if answer:
            return True
        else:
            return False

    def format_number(self):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.search(pattern, self.number)
        formatted = (f"+{answer.group(1)}({answer.group(2)})"
                     f"{answer.group(3)}-{answer.group(4)}")
        return formatted
