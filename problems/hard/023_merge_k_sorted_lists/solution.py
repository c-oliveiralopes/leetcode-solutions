from utils import ListNode
from typing import Optional, List


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Mescla k listas ligadas ordenadas em uma única lista ligada ordenada.
        
        Utiliza um min-heap para sempre selecionar o menor elemento entre as
        cabeças das listas restantes. Esta abordagem garante que a lista
        resultante esteja sempre ordenada.
        
        Args:
            lists (List[Optional[ListNode]]): Lista de k listas ligadas ordenadas
            
        Returns:
            Optional[ListNode]: Cabeça da lista ligada mesclada e ordenada
        """
        if not lists or len(lists) == 0:
            return None
        
        min_heap = []
    
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))
        
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            val, list_idx, node = heapq.heappop(min_heap)
            
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, list_idx, node.next))
        
        return dummy.next
