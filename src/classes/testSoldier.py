'''
declare a "soldier" unit for testing
'''
from __future__ import annotations
from unit import UnitBase

class Soldier(UnitBase):
    '''"soldier" unit'''
    def __init__(self, health: int, attackVal: int) -> None:
        '''init "soldier" unit'''
        super().__init__()
        self.attackVal = attackVal
        self.health = health