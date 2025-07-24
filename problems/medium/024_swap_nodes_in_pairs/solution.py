from typing import Optional, List
from utils import ListNode  

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Troca cada dois nós adjacentes em uma lista ligada e retorna sua cabeça.
        
        Resolve o problema sem modificar valores nos nós da lista, apenas
        reorganizando os ponteiros dos nós. Utiliza abordagem iterativa com
        nó dummy para facilitar o gerenciamento dos ponteiros.
        
        Args:
            head (Optional[ListNode]): Cabeça da lista ligada original
            
        Returns:
            Optional[ListNode]: Cabeça da lista ligada com nós trocados em pares
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
        
        return dummy.next