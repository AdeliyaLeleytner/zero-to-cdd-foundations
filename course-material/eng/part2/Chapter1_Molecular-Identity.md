# Chapter 1. Molecular Identity: A Practical Exercise

In the [chapter on molecules](../part1/Chapter2_Reading-Molecules.md), we identified two requirements for a representation: retain important chemical differences and avoid artificial differences caused by the order of writing. We will now examine both in a small implementation.

## 1. Learning Objectives

- Compare graphs while accounting for atom labels.
- Explain why renumbering should not change the result.
- Recognize the limits of a representation.

## 2. From Molecule to a Learning Graph

We will represent only heavy atoms. Hydrogens, charges, bond orders, and stereochemistry are omitted. The program therefore checks equivalence of these graphs, not complete chemical identity.

Ethanol is represented by C–C–O and dimethyl ether by C–O–C. Erasing the element labels leaves identical three-vertex paths. Renumbering ethanol alone still allows labels and bonds to be matched without losing information.

## 3. Read and Run the Code

Open [identity.py](code/identity.py). The `equivalent` function enumerates vertex correspondences, checks labels, and then compares edges. For small learning graphs, this approach makes the entire algorithm visible.

```sh
python3 course-material/eng/part2/code/identity.py
```

The results for ethanol with reversed numbering, ethanol versus ether, and graphs without labels should be `True`, `False`, and `True`, respectively. Explain each result in terms of the information retained by the representation.

## 4. Summary and Exercises

### 4.1 Summary

Identity is defined relative to the chosen features. Vertex numbering is arbitrary; chemical labels carry meaning.

### 4.2 Exercises

1. Add two graphs of four identically labeled atoms: a chain and a star with three edges. Why do the same composition and number of bonds not make them equivalent?
2. Change the order of ethanol's vertices and edges. Which result should remain unchanged?
3. Which differences between molecules can this code never detect?
4. **★** How would including bond order change the edge representation and correspondence check? Why is exhaustive enumeration inconvenient for large graphs?

## References and Further Reading

- [Part I, Chapter 2](../part1/Chapter2_Reading-Molecules.md): the chemistry behind the example.
- [RDKit: Getting Started](https://www.rdkit.org/docs/GettingStartedInPython.html): the next step toward full molecular objects.
