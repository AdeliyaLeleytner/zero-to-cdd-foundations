"""Учебный граф тяжёлых атомов: связность, метки и нумерация.

Это перебор изоморфизмов для крошечных графов, не химический парсер.
Стереохимия, водороды, заряды и типы связей здесь не представлены.
"""
from itertools import permutations


def equivalent(labels_a, edges_a, labels_b, edges_b):
    """Check labelled undirected graph equivalence by exhaustive permutation."""
    if len(labels_a) != len(labels_b):
        return False
    a = {tuple(sorted(edge)) for edge in edges_a}
    b = {tuple(sorted(edge)) for edge in edges_b}
    for mapping in permutations(range(len(labels_a))):
        if any(labels_a[i] != labels_b[mapping[i]] for i in range(len(labels_a))):
            continue
        mapped = {tuple(sorted((mapping[i], mapping[j]))) for i, j in a}
        if mapped == b:
            return True
    return False


def main():
    path = [(0, 1), (1, 2)]
    ethanol = ('C', 'C', 'O')
    reverse_ethanol = ('O', 'C', 'C')
    ether = ('C', 'O', 'C')
    print('Этанол и его обратная нумерация:', equivalent(ethanol, path, reverse_ethanol, path))
    print('Этанол и диметиловый эфир:', equivalent(ethanol, path, ether, path))
    print('Если удалить метки элементов:', equivalent(('X',)*3, path, ('X',)*3, path))
    print('Ограничение: эта модель не различает стереоизомеры и состояния заряда.')


if __name__ == '__main__':
    main()
