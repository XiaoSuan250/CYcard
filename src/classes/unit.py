'''declare the base class of unit'''
from __future__ import annotations

class UnitBase:
    '''unit base class'''
    def __init__(self, health : int) -> None:
        '''Unit init'''
        super().__init__()
        self.health = health
        
    def ReduceHealth(self, ReduceVal : int) -> None:
        '''reduce the health of the unit'''
        self.health -= ReduceVal