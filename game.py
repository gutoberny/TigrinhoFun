from dataclasses import dataclass
from typing import List 
from utils import random_slot

@dataclass
class Game:
    slots: List[List[str]] 

    def girar_roleta(self):
        self.slots = [
            [random_slot(), random_slot(), random_slot()],
            [random_slot(), random_slot(), random_slot()],
            [random_slot(), random_slot(), random_slot()],
        ]

    def desenhar(self):
        for l in self.slots:
            for c in l:
                print(f"[ {c} ]", end="")
            print()

    def verificar(self):
        result_slug = False

        #verificar horizontais
        count_horizontal = 0
        for l in self.slots:
            if l[0] == l[1] and l[0] == l[2]:
                result_slug = f"horizontal-{count_horizontal}"
            count_horizontal += 1

        #verificar diagonal cima pra baixo
        count_diagonal = 0
        d_list = []
        for l in self.slots:
            d_list.append(l[count_diagonal])
            count_diagonal += 1

        if d_list[0] == d_list[1] and d_list[0] == d_list[2]:
            result_slug = f"diagonal-t-b"


        #verificar diagonal baixo pra cima
        count_diagonal = 2
        d_list = []
        for l in self.slots:
            d_list.append(l[count_diagonal])
            count_diagonal -= 1

        if d_list[0] == d_list[1] and d_list[0] == d_list[2]:
            result_slug = f"diagonal-b-t"

        return result_slug
