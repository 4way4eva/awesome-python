import math
import unittest

from scripts import codexx_demo


class CodexxDemoTests(unittest.TestCase):
    def test_phi_and_xx(self):
        p = codexx_demo.phi()
        self.assertAlmostEqual(p, (1 + math.sqrt(5)) / 2)
        self.assertAlmostEqual(codexx_demo.xx_factor(), p ** 2)

    def test_yield(self):
        seq = codexx_demo.codexx_yield(4, factor=2.0)
        self.assertEqual(seq, [1.0, 2.0, 4.0, 8.0])

    def test_reciprocal(self):
        self.assertTrue(codexx_demo.baba_reciprocal_check(100, 262, factor=2.618))
        self.assertFalse(codexx_demo.baba_reciprocal_check(100, 200, factor=2.618))

    def test_pressure(self):
        ratio, deficit = codexx_demo.xx_overscale_pressure(100, 50, factor=2.0)
        self.assertAlmostEqual(ratio, 1.5)
        self.assertAlmostEqual(deficit, 150)

    def test_validation(self):
        with self.assertRaises(ValueError):
            codexx_demo.codexx_yield(-1)


if __name__ == "__main__":
    unittest.main()
