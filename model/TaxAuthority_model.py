from TP_Wise.model.TaxBracket_model import TaxBracket
from typing import List
class TaxAuthority:
    def __init__(self,label:str, taxFreeThreshold:float):
        self.__label = label
        self.__taxFreeThreshold = taxFreeThreshold
        self.__taxBrackets: List[TaxBracket] = []

    def get_label(self):
        return self.__label

    def set_label(self,value:str):
        self.__label = value

    def get_taxFreeThreshold(self):
        return self.__taxFreeThreshold

    def set_taxFreeThreshold(self, value:float):
        self.__taxFreeThreshold = value

    def get_taxBrackets(self) -> List[TaxBracket] :
        return self.__taxBrackets

    def set_taxBrackets(self, value: List[TaxBracket]):
        self.__taxBrackets = value

    def add_tax_bracket(self, tax_bracket: TaxBracket):
        self.__taxBrackets.append(tax_bracket)

    def get_tax_bracket(self, minIncome, maxIncome):
        for bracket in self.__taxBrackets:
            if (bracket.get_minIncome() == minIncome and
                    bracket.get_maxIncome() == maxIncome):
                return bracket
        return None

    def remove_bracket(self, minIncome, maxIncome):
        for bracket in self.__taxBrackets:
            if (bracket.get_minIncome() == minIncome
                    and bracket.get_maxIncome() == maxIncome):
                self.__taxBrackets.remove(bracket)
                return True  # Bracket removed successfully
        return False  # Bracket not found

    def __str__(self):
        taxBrackets_str = '\n'.join (str(bracket) for bracket in self.__taxBrackets)
        return f'TaxAuthority(Label={self.__label}, TaxFreeThreshold={self.__taxFreeThreshold},Tax Brackets:\n [{taxBrackets_str}])'


if __name__ == '__main__':
    TaxBracket1 = TaxBracket(minIncome=53.359, maxIncome=106.717, taxeRate=0.205)
    TaxBracket2 = TaxBracket(minIncome=52.359, maxIncome=106.717, taxeRate=0.25)
    TaxBracket3 = TaxBracket(minIncome=1, maxIncome=2, taxeRate=0)
    QC = TaxAuthority('QC', 0.1)
    QC.add_tax_bracket(TaxBracket1)
    QC.add_tax_bracket(TaxBracket2)
    QC.add_tax_bracket(TaxBracket3)
    print(QC)
    print('all-ok!')





