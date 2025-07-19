from typing import Optional
from utils import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove o n-ésimo nó a partir do final da lista ligada.
        
        Esta solução utiliza a técnica de dois ponteiros (two pointers) para
        resolver o problema em uma única passada pela lista.
        
        Args:
            head (ListNode): O nó cabeça da lista ligada
            n (int): A posição do nó a ser removido contando do final (1-indexado)
        
        Returns:
            ListNode: O nó cabeça da lista modificada
        """
        # Cria um nó dummy para simplificar casos extremos
        # (como remover o primeiro nó da lista)
        dummy = ListNode(0)
        dummy.next = head
        
        # Inicializa os dois ponteiros no nó dummy
        primeiro = dummy
        segundo = dummy
        
        # Move o primeiro ponteiro n+1 posições à frente
        # Isso cria uma distância de n nós entre os ponteiros
        for i in range(n + 1):
            primeiro = primeiro.next
        
        # Move ambos os ponteiros até o primeiro chegar ao final
        # Quando primeiro chegar ao None, segundo estará no nó
        # anterior ao que deve ser removido
        while primeiro is not None:
            primeiro = primeiro.next
            segundo = segundo.next
        
        # Remove o nó fazendo segundo.next apontar para segundo.next.next
        segundo.next = segundo.next.next
        
        # Retorna a nova cabeça da lista (dummy.next)
        return dummy.next