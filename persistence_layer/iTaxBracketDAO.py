from abc import ABC, abstractmethod
from TP_Wise.model.TaxBracket_model import TaxBracket
from typing import List


class ITaxBracketDAO(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def find_applicable_brackets(self, authority: str, amount: float) -> List[TaxBracket]:
        pass


    @abstractmethod
    def findtaxbrackets_by_label(self, label):
        pass

