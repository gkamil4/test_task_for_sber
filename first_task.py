from typing import Callable, Union, List, Dict
import numpy as np

Tree = Union[int, List, Dict, np.ndarray]

def max_depth(tree: Tree) -> int:
    '''Вычисляет максимальную глубину дерева'''
    if isinstance(tree, (list, np.ndarray)):
        return 1 + max((max_depth(item) for item in tree), default=0) #default 0 нужен для случая когда у нас есть пустой список, такую ситуацию я определяю нулем
    elif isinstance(tree, dict):
        return 1 + max((max_depth(value) for value in tree.values()), default=0)
    return 0

def apply_to_leaves(tree: Tree, function: Callable, depth: int) -> Tree:
    '''Применяет функцию к листьям на заданной глубине'''
    if depth == 1:
        if isinstance(tree, list):
            return function(tree)
            
        elif isinstance(tree, np.ndarray):
            return function(tree.tolist())
        elif isinstance(tree, dict):
            return function(list(tree.values()))
    elif isinstance(tree, (list, np.ndarray)):
        return [apply_to_leaves(item, function, depth - 1) for item in tree] # мы спускаем по дереву сверху вниз, пока не дошли до части глубиной 1, то есть листа
    elif isinstance(tree, dict):
        return {k: apply_to_leaves(v, function, depth - 1) for k, v in tree.items()}
    return tree

def convolve(tree: Tree, function: Callable) -> Tree:
    '''Применяет заданную функцию к листьям'''
    depth = max_depth(tree)
    return apply_to_leaves(tree, function, depth)
