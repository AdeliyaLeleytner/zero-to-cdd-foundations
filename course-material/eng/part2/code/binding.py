"""Chapter 4 calculations. All parameters are hypothetical. Python standard library."""
import math

R = 8.31446261815324  # J mol^-1 K^-1


def _finite(value, name, positive=False):
    if not math.isfinite(value) or (value <= 0 if positive else value < 0):
        raise ValueError(f'{name} must be finite and {"positive" if positive else "non-negative"}')


def occupancy(ligand_free, kd):
    """Both concentrations must be in the same units; one-site equilibrium."""
    _finite(ligand_free, 'ligand_free')
    _finite(kd, 'kd', positive=True)
    return ligand_free / (kd + ligand_free)


def complex_concentration(protein_total, ligand_total, kd):
    """Physical root of the 1:1 mass-balance quadratic, all units identical.

    Rationalized expression avoids subtracting two nearly equal numbers.
    Scaling concentrations keeps the discriminant safe at extreme units.
    """
    _finite(protein_total, 'protein_total')
    _finite(ligand_total, 'ligand_total')
    _finite(kd, 'kd', positive=True)
    scale = max(protein_total, ligand_total, kd)
    p, l, k = protein_total/scale, ligand_total/scale, kd/scale
    if p == 0 or l == 0:
        return 0.0
    total = p+l+k
    discriminant = (p-l)**2 + k*k + 2*k*(p+l)
    return scale * (2*p*l / (total + math.sqrt(discriminant)))


def free_energy(kd_molar, temperature=298.0):
    """Standard binding Gibbs energy in kJ/mol, concentration standard 1 M."""
    _finite(kd_molar, 'kd_molar', positive=True)
    _finite(temperature, 'temperature', positive=True)
    return R * temperature * math.log(kd_molar / 1.0) / 1000


def main():
    print('Teaching model: one independent site, reversible binding.')
    print('Kd = 10 nM; FREE concentrations are used:')
    for ligand in [1, 10, 90, 990]:
        print(f'  L = {ligand:>3} nM -> occupancy {100*occupancy(ligand, 10):6.2f}%')
    bound = complex_concentration(100, 100, 10)
    print(f'Mass balance: P_total=L_total=100 nM, Kd=10 nM -> PL={bound:.4f} nM')
    print(f'  P_free=L_free={100-bound:.4f} nM, occupancy={bound:.4f}%')
    print(f'Delta G standard, Kd=10 nM, T=298 K: {free_energy(10e-9):.4f} kJ/mol')
    print(f'Delta Delta G, 100 -> 10 nM: {free_energy(10e-9)-free_energy(100e-9):.4f} kJ/mol')
    for koff in [0.01, 0.001]:
        print(f'koff={koff} /s: tau={1/koff:g} s, half-life={math.log(2)/koff:.2f} s')


if __name__ == '__main__':
    main()
