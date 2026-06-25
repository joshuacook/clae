# CLAE datasets

Book-authored datasets (distinct from the course/project-1 data documented in
`source/README.md`).

## `tracking` (Estimator-arc dataset, Ch 12-14)

A linear-Gaussian constant-velocity state-space track, modeled on the Georgia
Tech "AI for Robotics" (Thrun, CS 7638) treatment. A target moves on a
constant-velocity 2D track; we observe only noisy position, with some
measurements dropped. Ground truth is known exactly, so a Kalman filter can be
shown recovering the true track. Design rationale: `clae-book-decisions.md`.

Generate it (needs numpy; runs in Colab or any Python env, not on cc-host):

```bash
python3 generate_tracking.py --out tracking.csv
```

Outputs:

- `tracking.csv` — columns `t, px, py, vx, vy` (true state), `zx, zy`
  (measurements; empty on gap rows).
- `tracking_model.txt` — the known F, H, Q, R, x0 (ground truth for checking the filter).

One dataset serves the whole arc:

- **Ch 12** (static LMMSE): a single update step, estimate state from one `z` given a prior.
- **Ch 13** (recursive): the 1D filter on the x-coordinate `(px, vx)`.
- **Ch 14** (full Kalman): the 2D tracker, including estimation through the gaps.

Knobs: `--n` steps, `--dt`, `--q` process-noise scale, `--r` measurement-noise
variance, `--gap-frac` fraction of dropped measurements, `--seed`.
