import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'utils'))

from typing import Optional
from data_structures import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problema 2: Add Two Numbers (https://leetcode.com/problems/add-two-numbers/)
        Dificuldade: Médio
        Tópicos: Lista ligada, matemática, recursão
        
        Estratégia: Simulação da soma manual com carry
        - Percorremos ambas as listas simultaneamente
        - Somamos dígitos correspondentes + carry anterior
        - Criamos novo nó com o resultado módulo 10
        - Propagamos o carry (divisão por 10)
        Complexidade temporal: O(Max(N, M)) | Complexidade espacial: O(Max(N, M))
        """
        dummy = ListNode(0)  # Nó auxiliar para simplificar a lógica
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Extrai valores dos nós atuais (0 se None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calcula soma total e novos valores
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Cria novo nó e avança ponteiros
            current.next = ListNode(digit)
            current = current.next
            
            # Avança nas listas originais
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next