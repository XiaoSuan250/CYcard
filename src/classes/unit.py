"""_summary_
writen by admin1lin2
2023_6_5
declare the base class of unit
please dont refence it for any commercial reason
"""
from __future__ import annotations

__all__ = [
    "UnitBase"
]

class UnitBase:
    '''unit base class'''
    def __init__(self) -> None:
        '''Unit init'''
        super().__init__()
    
    def onAttack(self):
        '''call it when unit attack something'''
        pass
    
    def onHurt(self):
        '''call it when unit be hurted'''
        pass

    def onSkill(self):
        '''call it when unit use its skill'''
        pass
    
    def onPlace(self):
        '''call it when unit be placed'''
        pass
    
    def onDie(self):
        '''call it when unit die'''
        pass
    
    def onBeTreated(self):
        '''call it when unit be treated'''
        pass
    
    def onTreat(self):
        '''call it when unit treat something'''
        pass