import unittest

from scripts import codex_formal_audit


class CodexFormalAuditTests(unittest.TestCase):
    def test_tempo_index(self):
        self.assertAlmostEqual(codex_formal_audit.tempo_index(8.0), 3.0)
        self.assertAlmostEqual(codex_formal_audit.tempo_index(12.0), 2.0)

    def test_on_beat_release(self):
        gates = [12.0, 8.0, 6.0, 4.0, 3.0, 2.4, 2.0, 1.2, 1.0]
        self.assertTrue(codex_formal_audit.is_on_beat_release(2.35, gates, 0.1))
        self.assertFalse(codex_formal_audit.is_on_beat_release(2.75, gates, 0.1))

    def test_rarity_cumulative(self):
        table = [
            {"rarity": "common", "upper_cumulative_probability": 0.6},
            {"rarity": "rare", "upper_cumulative_probability": 1.0},
        ]
        self.assertEqual(codex_formal_audit.classify_rarity(0.2, table), "common")
        self.assertEqual(codex_formal_audit.classify_rarity(0.9, table), "rare")

    def test_run_audit(self):
        results = codex_formal_audit.run_audit()
        self.assertTrue(all(r.ok for r in results))
        checks = {r.check for r in results}
        self.assertIn("gamma-consistency", checks)


if __name__ == "__main__":
    unittest.main()
