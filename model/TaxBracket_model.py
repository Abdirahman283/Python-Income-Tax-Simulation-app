
class TaxBracket:
    def __init__(self,minIncome:float,maxIncome:float,taxeRate:float):
        self.__minIncome = minIncome
        self.__maxIncome = maxIncome
        self.__taxeRate = taxeRate

    def get_minIncome(self):
        return self.__minIncome

    def set_minIncome(self, value:float):
        self.__minIncome = value

    def get_maxIncome(self):
        return self.__maxIncome

    def set_maxIncome(self, value:float):
        self.__maxIncome = value

    def get_taxeRate(self):
        return self.__taxeRate

    def set_taxeRate(self, value:float):
        self.__taxeRate = value

    def __str__(self):
        return f'     from  {self.__minIncome} to {self.__maxIncome},  {self.__taxeRate} is applied'


if __name__=='__main__':
    TaxBracket1 = TaxBracket(minIncome=53.359, maxIncome=106.717, taxeRate=0.205)
    TaxBracket2 = TaxBracket(minIncome=53.359, maxIncome=106.717, taxeRate=0.25)
    print('TaxBracket1:',TaxBracket1)
    print('TaxBracket2:',TaxBracket2)


