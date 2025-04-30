from TP_Wise.persistence_layer.iTaxBracketDAO import ITaxBracketDAO
from abc import ABC, abstractmethod


class TaxCalculator(ABC):

    def __init__(self, dao: ITaxBracketDAO):
        self._dao = dao
        pass

    @abstractmethod
    def calculate_tax(self,amount: float) -> float:
        pass

    @abstractmethod
    def brackets_by_state(self, label) -> str:
        pass





