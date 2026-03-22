# CODEXX Demo Script

This repository now includes an executable `CODEXX` demonstration script:

- File: `scripts/codexx_demo.py`
- Run: `python scripts/codexx_demo.py`

## What it implements

- φ and XX (φ²) helpers
- reusable spiral sequence generation
- XX-fold reciprocity checks
- overscale pressure calculation
- BABA-style ASCII section for terminal output

## Example

```bash
python scripts/codexx_demo.py --turns 6 --given 1000 --received 3000
```

The script is structured as reusable functions and a CLI `main()` so it can be
imported in tests or run directly from the command line.
