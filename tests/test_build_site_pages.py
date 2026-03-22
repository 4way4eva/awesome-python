import unittest

from scripts import build_site


class BuildSitePagesTests(unittest.TestCase):
    def test_bleu_day_page_registered(self):
        sources = [str(src) for _, src, _ in build_site.PAGES]
        self.assertTrue(any(path.endswith('docs/bleu-day-of-thanks.md') for path in sources))


    def test_evol_decoded_insights_registered(self):
        sources = [str(src) for _, src, _ in build_site.PAGES]
        self.assertTrue(any(path.endswith('docs/evol-codex-decoded-insights.md') for path in sources))


if __name__ == '__main__':
    unittest.main()
