import importlib.util
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
def module(name, language='ru'):
    spec = importlib.util.spec_from_file_location(name, ROOT/'course-material'/language/'part2/code'/f'{name}.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class ScienceChecks(unittest.TestCase):
    b = module('binding')
    g = module('identity')
    def test_mass_balance_and_reconstructed_kd(self):
        for p,l,k in [(100,100,10),(1,100,10),(100,1,10),(1e-9,2e-9,1e-8),(1,1,1e-6)]:
            x=self.b.complex_concentration(p,l,k)
            self.assertTrue(0 <= x <= min(p,l))
            self.assertAlmostEqual((p-x)*(l-x)/x/k,1,places=8)
        self.assertEqual(self.b.complex_concentration(0,10,1),0)
        self.assertEqual(self.b.complex_concentration(10,0,1),0)

    def test_quadratic_symmetric_and_units(self):
        x=self.b.complex_concentration(100,70,10)
        self.assertAlmostEqual(x,self.b.complex_concentration(70,100,10))
        self.assertAlmostEqual(x,self.b.complex_concentration(100e-9,70e-9,10e-9)*1e9)
        self.assertAlmostEqual(self.b.complex_concentration(100,100,10),72.9843788128,places=8)

    def test_energy_and_occupancy(self):
        self.assertAlmostEqual(self.b.free_energy(1.0),0)
        self.assertAlmostEqual(self.b.free_energy(1e-8)-self.b.free_energy(1e-7),-self.b.R*298*math.log(10)/1000)
        self.assertEqual(self.b.occupancy(180,20),0.9)
        self.assertAlmostEqual(self.b.occupancy(380,20),0.95)

    def test_invalid_physical_parameters(self):
        for x in [-1,float('nan'),float('inf')]:
            with self.assertRaises(ValueError): self.b.occupancy(x,10)
        with self.assertRaises(ValueError): self.b.free_energy(0)

    def test_graph_semantics(self):
        path=[(0,1),(1,2)]
        self.assertTrue(self.g.equivalent('CCO',path,'OCC',path))
        self.assertFalse(self.g.equivalent('CCO',path,'COC',path))
        self.assertFalse(self.g.equivalent('CCCC',[(0,1),(1,2),(2,3)],'CCCC',[(0,1),(0,2),(0,3)]))

class EnglishScienceChecks(ScienceChecks):
    b = module('binding', 'eng')
    g = module('identity', 'eng')

if __name__=='__main__': unittest.main()
