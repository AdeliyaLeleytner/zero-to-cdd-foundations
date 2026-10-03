# Exercise Discussions

Use this page to check your work after making your own attempt. Open-ended questions include one possible line of reasoning. Other answers are valid when the assumptions are clear and the conclusions follow from the evidence.

## Chapter 1

**1.** For example: reducing the activity of enzyme X in cells Y will reduce the production of Z, whose excess contributes to the process being studied. This is a teaching hypothesis; its components still need testing.

**2.** Possible explanations include inadequate access to the target inside the cell and an incorrect hypothesis linking the protein's function to the chosen phenotype. For the first, intracellular exposure and target engagement are informative; for the second, an independent intervention in protein function, with appropriate controls on its consequences, can help. A single negative cellular result does not distinguish these explanations.

**3.** Activity is one characteristic. Another hit may have more useful solubility, selectivity, synthetic accessibility, or an initial chemical series. The choice depends on the next task.

**4.** A phenotypic observation alone does not establish the target. Target deconvolution and mechanism testing come next.

**5.** For A, check actual solubility and cellular assay conditions. For B, investigate direct interaction and the connection between the proposed target and phenotype. For C, check signal reproducibility and suitable assay controls. When seeking a tool for a particular protein, mechanism and selectivity are especially important. Any compound selection should be tied to a specific question.

## Chapter 2

**1–2.** Ethanol and dimethyl ether both have composition C₂H₆O but different bonds. Ethanol has O–H; the ether does not, so their usual donor capabilities differ. Both neutral oxygens can act as acceptors under suitable conditions.

**3–4.** Changing a dihedral angle by rotating about a bond can change conformation without changing configuration. For stereoisomers, check the spatial labels and whether the structures can be superimposed. A protein environment is chiral and can distinguish these forms.

**5.** At pKa = 6: pH 5 → 9.09% A⁻; pH 6 → 50%; pH 7 → 90.91%. Use $f_{A^-}=1/(1+10^{pK_a-\mathrm{pH}})$.

**6.** $[B]/[BH^+]=10^{7-8}=0.1$. The fraction of B is $0.1/1.1\approx9.09\%$; BH⁺ predominates.

**7.** Atom counts do not preserve connectivity, stereochemistry, conformation, or charge state if the latter is not separately encoded. An element-and-bond-order graph adds connectivity, but without further features it does not fully resolve the other questions.

**8.** Renumbering ethanol gives an equivalent graph; the ether differs in the labels on neighboring vertices. Replacing every label with X removes the distinction. A four-vertex chain and a star differ in their vertex degrees.

**★.** From $r=[A^-]/[HA]=10^{\mathrm{pH}-pK_a}$, we obtain $f=r/(1+r)$. The model assumes one acidic group and two forms under a suitable concentration approximation.

## Chapter 3

**1.** Sequence tells us which residues occur and in which order; structure describes where atoms are in the represented state; function describes what the protein does under specified conditions.

**2.** Final coordinates do not contain the complete trajectory, rates, or probabilities of intermediate states.

**3.** Affinity describes binding; efficacy describes the ability to produce a chosen response. Binding alone is insufficient to assign the same action to two ligands.

**4.** States of different protein regions can be coupled. Binding in one place can change the distribution of states and function elsewhere; this must be tested for the particular system.

**5.** 1IEP: X-ray diffraction; Mus musculus; c-ABL kinase domain; ligand STI, imatinib. This is not full-length human BCR–ABL. When checking the entry again, account for its version.

**6.** Missing coordinates can indicate insufficient structural information for a flexible region. Check the construct sequence, modeled residues, and experimental description.

**7.** Ask whether the relevant state is represented in the starting model, how accessible it is, and whether the selected method can account for the necessary rearrangements. A successful pose alone does not determine the kinetic binding pathway.

**★.** For example, the molecule may not reach the protein inside cells, or lowering protein activity may not change the chosen phenotype because of context or compensation. The tests should distinguish these explanations.

## Chapter 4

**1–4.** At equilibrium, opposing rates are equal. Kd has units s⁻¹/(M⁻¹s⁻¹) = M. Free ligand is available for binding, so consumption into complexes must be accounted for. koff provides dissociation-rate information that is absent from the ratio koff/kon alone.

**5.** At Kd = 20 nM: 2 nM → 9.09%; 20 nM → 50%; 180 nM → 90%.

**6.** Rearranging $\theta=[L]/(K_d+[L])$ gives $[L]=\theta K_d/(1-\theta)$. For 95% occupancy, 19Kd = 380 nM free ligand is needed.

**7.** 50 nM = $5\times10^{-8}$ M; pKd ≈ 7.301. A tenfold decrease in Kd increases pKd by one.

**8.** Kd = $10^{-8}$ M. In the first case, koff = 0.002 s⁻¹ and τ = 500 s; in the second, koff = 0.02 s⁻¹ and τ = 50 s. Faster association at the same Kd is accompanied by faster dissociation in this model.

**9.** For P_total = L_total = 100 nM and Kd = 10 nM: PL ≈ 72.9844 nM and P_free = L_free ≈ 27.0156 nM. Substitution gives Kd ≈ 10 nM. At P_total = 1 nM, less than 1 nM ligand is consumed, so free concentration remains close to 100 nM; occupancy is close to 90.9%.

**★.** At constant free [L], $d\theta/dt=k_{on}[L](1-\theta)-k_{off}\theta$. The deviation from equilibrium therefore decays as $\exp[-(k_{on}[L]+k_{off})t]$. If incubation is too short, observed occupancy depends on time, and applying an equilibrium model can give an incorrect estimate.

The numerical results can be reproduced with [binding.py](../../course-material/eng/part2/code/binding.py). A complete answer should also explain the units, assumptions, and chosen equation.
