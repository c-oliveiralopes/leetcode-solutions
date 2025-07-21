from typing import Optional
from utils import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Mescla duas listas ligadas ordenadas em uma única lista ordenada.
        
        Args:
            list1: Cabeça da primeira lista ligada ordenada
            list2: Cabeça da segunda lista ligada ordenada
            
        Returns:
            Cabeça da nova lista ligada mesclada e ordenada
        """
        # Cria um nó dummy para facilitar a manipulação da lista
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Conecta o restante da lista que ainda não foi percorrida
        if list1:       
            current.next = list1
        elif list2:
            current.next = list2

        # Retorna a lista mesclada, ignorando o nó dummy
        return dummy.next