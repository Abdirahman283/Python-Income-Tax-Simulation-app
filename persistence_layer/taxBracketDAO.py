from TP_Wise.data_layer.inMemoryRepository import InMemoryRepository
from TP_Wise.model.TaxBracket_model import TaxBracket
from TP_Wise.persistence_layer.iTaxBracketDAO import ITaxBracketDAO
from typing import List
import math


class TaxBracketDAO(ITaxBracketDAO):

    def __init__(self):
        super().__init__()
        self.__repository = InMemoryRepository()

    def get_repository(self):
        return self.__repository

    def findtaxbrackets_by_label(self, label)\
            -> List[TaxBracket]:
        for tax_authority in self.get_repository().get_TaxAuthorities():
            if tax_authority.get_label() == label:
                return tax_authority.get_taxBrackets()
        return []

    def find_applicable_brackets(self, label: str, amount: float) \
            -> List[TaxBracket]:
        applicable_brackets = []
        taxbrackets = self.findtaxbrackets_by_label(label)

        for bracket in taxbrackets:
            if amount >= bracket.get_maxIncome() :
                applicable_brackets.append(bracket)

            elif amount > bracket.get_minIncome() and amount < bracket.get_maxIncome():

                applicable_brackets.append(TaxBracket(bracket.get_minIncome(), amount, bracket.get_taxeRate()))

            elif (len(applicable_brackets) == (len(taxbrackets) - 1)
                  and (bracket.get_maxIncome() == math.inf)):

                applicable_brackets.append(TaxBracket(bracket.get_minIncome(), amount, bracket.get_taxeRate()))

        return applicable_brackets

    def create_tax_bracket(self, label: str, minIncome: float, maxIncome: float, taxRate: float)\
            -> [TaxBracket]:

        for tax_authority in self.get_repository().get_TaxAuthorities():

            if tax_authority.get_label() == label:
                tax_bracket = TaxBracket(minIncome, maxIncome, taxRate)
                tax_authority.add_tax_bracket(tax_bracket)

                return tax_bracket

    def update_tax_bracket(self, label: str, minIncome: float, maxIncome: float, new_taxRate: float) \
            -> List[TaxBracket]:

        for tax_authority in self.get_repository().get_TaxAuthorities():

            if tax_authority.get_label() == label:

                for tax_bracket in tax_authority.get_taxBrackets():

                    if tax_bracket.get_minIncome() == minIncome and tax_bracket.get_maxIncome() == maxIncome:
                        tax_bracket.set_taxeRate(new_taxRate)

                return tax_authority.get_taxBrackets()

    def delete_tax_bracket(self, label: str, minIncome: float, maxIncome: float):

        for tax_authority in self.get_repository().get_TaxAuthorities():

            if tax_authority.get_label() == label:

                for tax_bracket in tax_authority.get_taxBrackets():

                    if tax_bracket.get_minIncome() == minIncome and tax_bracket.get_maxIncome() == maxIncome:
                        tax_authority.remove_bracket( minIncome, maxIncome)

                return tax_authority



if __name__ == '__main__':
    r=TaxBracketDAO().findtaxbrackets_by_label('CA')
    for taxbracket in r:
        print(taxbracket)

    print('****************find_all_brackets_applicable*******')
    dao = TaxBracketDAO()
    result: List[TaxBracket] = dao.find_applicable_brackets('QC', 98540)
    for tax_bracket in result:
        print(tax_bracket)
    print('"*******************creat****************"')

    result=TaxBracketDAO().create_tax_bracket('CA', 5, 1,2)
    print(result)

    print('"******************update******************"')

    result=TaxBracketDAO().update_tax_bracket('QC', 98540, 119910,3)
    for taxbracket in result:
        print(taxbracket)
        print('*******************delete***********************')
    print( TaxBracketDAO().delete_tax_bracket('QC',98540, 119910))
