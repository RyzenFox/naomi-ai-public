import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from app_naomi_public_demo import DemoRoute, NaomiPublicDemo  # noqa: E402


class NaomiPublicDemoTests(unittest.TestCase):
    def setUp(self) -> None:
        self.demo = NaomiPublicDemo()

    def test_rejects_empty_input(self) -> None:
        self.assertEqual(self.demo.process("  ").route, DemoRoute.INVALID)

    def test_routes_help(self) -> None:
        self.assertEqual(self.demo.process("Ajuda").route, DemoRoute.HELP)

    def test_routes_status(self) -> None:
        self.assertEqual(self.demo.process(" status ").route, DemoRoute.STATUS)

    def test_routes_generic_message_without_external_side_effects(self) -> None:
        result = self.demo.process("Olá, Naomi")
        self.assertEqual(result.route, DemoRoute.CONVERSATION)
        self.assertIn("conceitual", result.message)


if __name__ == "__main__":
    unittest.main()
