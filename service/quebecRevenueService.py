from TP_Wise.service.taxCalculator import TaxCalculator
from TP_Wise.persistence_layer.iTaxBracketDAO import ITaxBracketDAO
from TP_Wise.persistence_layer.taxBracketDAO import TaxBracketDAO


class QuebecService(TaxCalculator):

    def __init__(self, dao: ITaxBracketDAO):

        super().__init__(dao)

    def calculate_tax(self, amount: float) -> float:
        brackets = self._dao.find_applicable_brackets("QC", amount)
        tax = 0.0

        for bracket in brackets:

            tax += ((bracket.get_maxIncome() - bracket.get_minIncome())
                    * bracket.get_taxeRate())

        return tax

    def brackets_by_state(self, label) -> str:

        tax_brackets = self._dao.findtaxbrackets_by_label("QC")
        formatted_brackets = ' \n'.join(str(bracket) for bracket in tax_brackets)

        return formatted_brackets


if __name__ == '__main__':
    dao = TaxBracketDAO()
    cs = QuebecService(dao)
    tax1 = cs.calculate_tax(98540)
    print(tax1)
    t = cs.brackets_by_state('QC')
    print(t)
