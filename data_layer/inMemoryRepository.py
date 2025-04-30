from TP_Wise.model.TaxBracket_model import TaxBracket
from TP_Wise.model.TaxAuthority_model import TaxAuthority
from typing import List
import math

class InMemoryRepository:

    def __init__(self):
        self.__TaxAuthorities: List[TaxAuthority] = []
        self.__populate()

    def get_TaxAuthorities(self):
        return self.__TaxAuthorities

    def add_tax_authority(self, tax_authority: TaxAuthority):
        self.__TaxAuthorities.append(tax_authority)

    def __populate(self):
        tax_authority_CA = TaxAuthority('CA', 15000)
        tax_authority_CA.add_tax_bracket(TaxBracket(15000, 53359, 0.15))
        tax_authority_CA.add_tax_bracket(TaxBracket(53359, 106717, 0.205))
        tax_authority_CA.add_tax_bracket(TaxBracket(106717, 165430, 0.26))
        tax_authority_CA.add_tax_bracket(TaxBracket(165430, 235675, 0.29))
        tax_authority_CA.add_tax_bracket(TaxBracket(235675, math.inf, 0.33))
        self.__TaxAuthorities.append(tax_authority_CA)

        tax_authority_QC = TaxAuthority('QC', 17183)
        tax_authority_QC.add_tax_bracket(TaxBracket(17183, 49275, 0.14))
        tax_authority_QC.add_tax_bracket(TaxBracket(49275, 98540, 0.19))
        tax_authority_QC.add_tax_bracket(TaxBracket(98540, 119910, 0.24))
        tax_authority_QC.add_tax_bracket(TaxBracket(119910, math.inf, 0.2575))
        self.__TaxAuthorities.append(tax_authority_QC)

    def __str__(self):
        tax_authorities_str = ','.join(str(ta) for ta in self.__TaxAuthorities)
        return f'InMemoryRepository(TaxAuthorities:\n   {tax_authorities_str})'

if __name__ == '__main__':
    repository = InMemoryRepository()
    print(repository)
    print("Repository is ok!")
