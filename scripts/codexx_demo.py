#!/usr/bin/env python3
"""CODEXX demo: phi-squared computational helpers and CLI showcase.

This module keeps the math reusable (for import/tests) while still providing
an executable demo script for command-line use.
"""

from __future__ import annotations

import argparse
import math
from typing import Iterable


def phi() -> float:
    """Return the golden ratio φ."""
    return (1 + math.sqrt(5)) / 2


def xx_factor() -> float:
    """Return XX = φ²."""
    return phi() ** 2


def codexx_yield(turns: int, factor: float | None = None) -> list[float]:
    """Return a spiral yield sequence of ``factor ** n`` for ``turns`` turns."""
    if turns < 0:
        raise ValueError("turns must be non-negative")
    base = xx_factor() if factor is None else factor
    return [base**n for n in range(turns)]


def baba_reciprocal_check(given: float, received: float, factor: float | None = None) -> bool:
    """Return whether received value satisfies XX-fold reciprocity."""
    if given < 0 or received < 0:
        raise ValueError("given/received must be non-negative")
    base = xx_factor() if factor is None else factor
    return received >= given * base


def xx_overscale_pressure(extraction: float, reciprocation: float = 0.0, factor: float | None = None) -> tuple[float, float]:
    """Compute overscale pressure ratio and deficit under XX standards."""
    if extraction < 0 or reciprocation < 0:
        raise ValueError("extraction/reciprocation must be non-negative")
    if extraction == 0:
        return 0.0, 0.0

    base = xx_factor() if factor is None else factor
    expected = extraction * base
    deficit = expected - reciprocation
    pressure_ratio = deficit / extraction
    return pressure_ratio, deficit


def format_sequence(values: Iterable[float]) -> str:
    """Format sequence with compact decimals for terminal output."""
    return "[" + ", ".join(f"{v:.6f}" for v in values) + "]"


def demo(turns: int, given: float, received: float, extraction: float, reciprocation: float) -> str:
    """Return a full CODEXX demonstration report as text."""
    p = phi()
    xx = xx_factor()
    seq_xx = codexx_yield(turns, xx)
    seq_phi = codexx_yield(turns, p)
    pressure_ratio, deficit = xx_overscale_pressure(extraction, reciprocation, xx)

    lines = [
        "=" * 60,
        "CODEXX — Double-X Engine Demo",
        "=" * 60,
        f"φ = {p:.10f}",
        f"XX (φ²) = {xx:.10f}",
        "",
        f"XX sequence ({turns} turns): {format_sequence(seq_xx)}",
        f"φ sequence  ({turns} turns): {format_sequence(seq_phi)}",
        "",
        f"BABA reciprocity check: given={given:.2f}, received={received:.2f}, "
        f"XX-whole={baba_reciprocal_check(given, received, xx)}",
        f"Overscale pressure: extraction={extraction:.2f}, reciprocation={reciprocation:.2f}",
        f"  pressure_ratio={pressure_ratio:.6f}, deficit={deficit:.2f}",
        "",
        "BABA Font ASCII",
        "╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔═╗ ╔═╗ ╔═╗",
        "║     ║   ║ ║   ║ ║     ╚═╗ ╚═╗ ╚═╗",
        "║     ║   ║ ║   ║ ║═══   ╔═╝ ╔═╝ ╔═╝",
        "╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝",
    ]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run CODEXX phi-squared demo")
    parser.add_argument("--turns", type=int, default=5, help="number of sequence turns")
    parser.add_argument("--given", type=float, default=1000, help="value given")
    parser.add_argument("--received", type=float, default=2620, help="value received")
    parser.add_argument("--extraction", type=float, default=51e12, help="extraction value")
    parser.add_argument("--reciprocation", type=float, default=0.0, help="reciprocation value")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(demo(args.turns, args.given, args.received, args.extraction, args.reciprocation))


if __name__ == "__main__":
    main()
