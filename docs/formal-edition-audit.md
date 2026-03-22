# EVOLVERSE Formal Edition (Axioms / Rules / Meanings / Contradictions)

This edition separates creative architecture from strict mathematical claims.

| Layer | Definition Style | Example |
|---|---|---|
| **AXIOM** | world-defined invariant | `Γ := 8.142886` as calibrated constant |
| **FORMAL RULE** | executable equation/algorithm | `R = min(24 / seconds_used, 3.0)` |
| **SYMBOLIC MEANING** | narrative/ceremonial interpretation | “XX as double-density reciprocity” |
| **DETECTED CONTRADICTION** | mismatch found by audit | symbolic Γ expressions not equal calibrated Γ |

## A) Axioms

1. **Calibrated Gamma**: `Γ := 8.142886`.
2. **Cycle Base**: 24-second possession baseline.
3. **Dual Alphabet Mode**: 24 active letters plus 2 sovereign boundary letters.

## B) Formal Rules

1. Tempo: `R = min(24 / seconds_used, 3.0)`.
2. On-beat gate: hit when `|release - gate| <= tolerance`.
3. Rarity classifier uses cumulative probability ranges ending at 1.0.

## C) Symbolic Meanings

1. XX (`φ²`) symbolizes stricter reciprocity density.
2. Sovereign letters represent boundary/authentication semantics.
3. Gate harmonics represent rhythm-lock intent rather than physical law.

## D) Detected contradictions and fixes

1. **Alphabet count drift**
   - Fix: explicit declaration of active vs sovereign letters in `formal_spec.yaml`.
2. **Gamma derivation mismatch**
   - Fix: treat symbolic forms as narrative descriptors; calibrated value is canonical.
3. **Single-point gate disputes**
   - Fix: tolerance window rule.
4. **Rarity logic collapse risk**
   - Fix: cumulative range classifier.

## E) Tooling

Run:

```bash
python scripts/codex_formal_audit.py
```

The command emits pass/fail by check and returns non-zero if any contradiction remains unresolved.
