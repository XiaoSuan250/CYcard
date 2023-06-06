'''
declare a "soldier" unit for testing
'''
from unit import UnitBase

class Soldier(UnitBase):
    '''"soldier" unit'''
    def __init__(self, health: int, attackVal: int) -> None:
        '''init "soldier" unit'''
        super().__init__(health)
        self.attackVal = attackVal
        
    def attack(self, obj: UnitBase) -> None:
        obj.ReduceHealth(self.attackVal)