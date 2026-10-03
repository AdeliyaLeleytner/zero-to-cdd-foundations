# Chapter 2. A Binding Model: A Practical Exercise

In the [binding chapter](../part1/Chapter4_Molecular-Binding.md), we derived occupancy and saw why free concentration can differ from added concentration. We will now reproduce the numbers and check mass balance.

## 1. Learning Objectives

- Apply the model using consistent units.
- Check the result through conservation of matter.
- Distinguish a model calculation from an experimental measurement.

## 2. Read the Model

Open [binding.py](code/binding.py). `occupancy` uses free concentration. `complex_concentration` solves the mass balance for one P–L complex. `free_energy` accepts Kd in M and returns standard free energy in kJ/mol.

All parameters are hypothetical. The model assumes one independent site and reversible binding at equilibrium.

## 3. Reproduce the Calculation

```sh
python3 course-material/eng/part2/code/binding.py
```

At Kd = 10 nM, free concentrations of 1, 10, 90, and 990 nM give occupancies of about 9.1%, 50%, 90%, and 99%. If total protein and total ligand are each 100 nM, about 72.98 nM complex forms. The remaining free concentrations are about 27.02 nM.

Substitute these values into the definition of Kd. Then check both balances: free protein plus complex equals total added protein, and free ligand plus complex equals total added ligand.

## 4. Change the Conditions

Reduce total protein concentration to 1 nM while retaining L_total = 100 nM and Kd = 10 nM. Before running the code, predict whether the approximation using added concentration will become more accurate. After calculating, compare the exact occupancy, `[PL]/[P]_total`, with the approximation from the chapter.

## 5. Summary and Exercises

### 5.1 Summary

Checking mass balance and units connects a numerical result with its physical meaning. Correct code execution does not by itself establish that the model fits a particular experiment.

### 5.2 Exercises

1. Repeat the calculation after converting all concentrations from nM to M. How should the complex concentration and occupancy change?
2. Set one partner's total concentration to zero. Which result is physically possible?
3. What happens to mean complex lifetime if koff decreases tenfold?
4. **★** Derive the rationalized expression for the smaller quadratic root used in the code. Why can subtracting nearly equal numbers lose precision?

## References and Further Reading

- [Part I, Chapter 4](../part1/Chapter4_Molecular-Binding.md): derivations and assumptions.
- [Jarmoskaite et al., 2020](https://doi.org/10.7554/eLife.57264): conditions for measuring equilibrium affinities.
