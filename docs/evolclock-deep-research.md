# EV0LClock Hoops — Deep Research (Formalized)

This page converts the EV0LClock concept into an implementation-ready rules profile.

## 1) Core timing model

- Base shot clock: **24s**
- Cycle size: **2 minutes**
- 24-cycle regulation map:
  - quarter = 6 cycles
  - half = 12 cycles
  - regulation = 24 cycles

## 2) Reciprocal tempo index

- Formula: `R = min(24 / seconds_used, 3.0)`
- Recommendation: treat `seconds_used` as a **possession segment** value that restarts after shot-clock resets.

## 3) On-beat release gates

Canonical gate times (seconds left):

`12.0, 8.0, 6.0, 4.0, 3.0, 2.4, 2.0, 1.2, 1.0`

Implementation rule:

- gate hit if `abs(release_time - gate_time) <= tolerance`
- default tolerance: `0.2s`

This resolves display precision disputes and makes officiating auditable.

## 4) EV Points accounting guidance

For production operations, keep EV Points as a **parallel payout ledger** unless the league intentionally defines a new competitive scoring system.

## 5) Data schema minimum

- possession id / team / player
- period and clock boundaries
- shot clock start / release
- seconds_used and R
- assist/make flags
- gate hit + nearest gate
- CleanOps deltas
- timeout sync flags

## 6) Auditability

Use `scripts/codex_formal_audit.py` to enforce consistency checks for:

- alphabet cardinality declarations
- calibrated constants vs symbolic forms
- cumulative rarity table logic
