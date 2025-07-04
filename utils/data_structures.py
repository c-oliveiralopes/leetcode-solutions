"""
Estrutura de dados padronizadas para resolução de problemas algorítmicos.

Este módulo fornece implementações otimizadas de estruturas de dados comumente utilizadas em múltiplos problemas LeetCode, garantindo consistência e confiabilidade.
"""

from typing import List, Optional, Any
from abc import ABC, abstractmethod

class ListNode:
    """
    Implementação de nó de lista simplesmente ligada.
    
    Fornece interface padrão para operações de lista ligada com capacidades aprimoradas de depuração.
    """
    
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f"ListNode(val={self.val})"
    
    def __repr__(self) -> str:
        return self.__str__()

class TreeNode:
    """
    Implementação de nó de árvore binária.
    
    Estrutura padrão de árvore binária com funcionalidade aprimorada para operações de traversal e manipulação de árvores.
    """
    
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return f"TreeNode(val={self.val})"
    
    def __repr__(self) -> str:
        return self.__str__()

class GraphNode:
    """
    Implementação de nó de grafo para representação de lista de adjacência.
    
    Suporta operações de grafo dirigido e não-dirigido com gerenciamento flexível de vizinhos.
    """
    
    def __init__(self, val: int = 0, neighbors: List['GraphNode'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def add_neighbor(self, neighbor: 'GraphNode') -> None:
        # Adiciona um vizinho ao nó atual
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
    
    def __str__(self) -> str:
        return f"GraphNode(val={self.val}, neighbors={len(self.neighbors)})"

class DataStructureInterface(ABC):
    """
    Classe base abstrata para implementações de estruturas de dados customizadas.
    
    Garante interface consistente entre todas as estruturas de dados customizadas utilizadas em soluções algorítmicas.
    """
    
    @abstractmethod
    def size(self) -> int:
        # Retorna o número de elementos na estrutura de dados
        pass
    
    @abstractmethod
    def is_empty(self) -> bool:
        # Verifica se a estrutura de dados está vazia
        pass
    
    @abstractmethod
    def clear(self) -> None:
        # Remove todos os elementos da estrutura de dados
        pass