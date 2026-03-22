#!/usr/bin/env python3
"""Formal consistency checks for EVOLVERSE/CODEXX spec artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math
import random
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "configs/codex/formal_spec.yaml"


@dataclass
class AuditResult:
    check: str
    ok: bool
    detail: str


def load_spec() -> dict:
    with SPEC_PATH.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError("formal_spec.yaml must parse as object")
    return data


def eval_symbolic(expr: str) -> float:
    safe_globals = {"__builtins__": {}}
    safe_locals = {"phi": (1 + math.sqrt(5)) / 2, "pi": math.pi}
    return float(eval(expr, safe_globals, safe_locals))


def check_alphabet(spec: dict) -> AuditResult:
    alpha = spec["alphabet"]
    declared_total = int(alpha["declared_total"])
    active = alpha["active_letters"]
    sovereign = alpha.get("sovereign_letters", [])

    ok = len(active) == declared_total and len(set(active + sovereign)) == len(active) + len(sovereign)
    detail = (
        f"declared_total={declared_total}, active={len(active)}, "
        f"sovereign={len(sovereign)}, unique={len(set(active + sovereign))}"
    )
    return AuditResult("alphabet-cardinality", ok, detail)


def check_gamma(spec: dict, tolerance: float = 1e-6) -> AuditResult:
    consts = spec["constants"]
    calibrated = float(consts["gamma_calibrated"])
    forms = consts.get("gamma_symbolic_forms", [])
    deltas = []
    for form in forms:
        value = eval_symbolic(form["expression"])
        deltas.append((form["name"], value - calibrated))

    ok = all(abs(delta) <= tolerance for _, delta in deltas)
    detail = ", ".join([f"{name}:delta={delta:.6f}" for name, delta in deltas])
    return AuditResult("gamma-consistency", ok, detail)


def tempo_index(seconds_used: float, cap: float = 3.0) -> float:
    if seconds_used <= 0:
        raise ValueError("seconds_used must be > 0")
    return min(24.0 / seconds_used, cap)


def is_on_beat_release(seconds_left: float, gates: list[float], tolerance: float) -> bool:
    return any(abs(seconds_left - gate) <= tolerance for gate in gates)


def classify_rarity(roll: float, table: list[dict]) -> str:
    if not 0 <= roll <= 1:
        raise ValueError("roll must be in [0, 1]")
    for band in table:
        if roll <= float(band["upper_cumulative_probability"]):
            return str(band["rarity"])
    raise RuntimeError("rarity table must terminate at cumulative 1.0")


def check_rarity_table(spec: dict) -> AuditResult:
    table = spec["loot_rarity"]
    probs = [float(r["upper_cumulative_probability"]) for r in table]
    is_sorted = probs == sorted(probs)
    ends_one = abs(probs[-1] - 1.0) <= 1e-9
    ok = is_sorted and ends_one
    detail = f"sorted={is_sorted}, terminal={probs[-1]:.2f}"
    return AuditResult("rarity-cumulative-table", ok, detail)


def run_audit() -> list[AuditResult]:
    spec = load_spec()
    return [
        check_alphabet(spec),
        check_gamma(spec),
        check_rarity_table(spec),
    ]


def main() -> int:
    results = run_audit()
    for result in results:
        status = "PASS" if result.ok else "FAIL"
        print(f"[{status}] {result.check}: {result.detail}")

    # demo outputs for operational functions
    spec = load_spec()
    gates = [float(g) for g in spec["evolclock"]["release_gates_seconds_left"]]
    tolerance = float(spec["evolclock"]["gate_tolerance_seconds"])
    print(f"Tempo demo R(8.0s): {tempo_index(8.0):.3f}")
    print(f"On-beat demo @2.35s: {is_on_beat_release(2.35, gates, tolerance)}")
    print(f"Rarity demo roll=0.93: {classify_rarity(0.93, spec['loot_rarity'])}")

    return 0 if all(r.ok for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
