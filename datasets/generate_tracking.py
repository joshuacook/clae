"""Generate the CLAE Estimator-arc dataset: a linear-Gaussian state-space track.

Modeled on the Georgia Tech "AI for Robotics" (Thrun, CS 7638) constant-velocity
tracking treatment. A target moves on a constant-velocity track in 2D; we observe
only its noisy position, with some measurements dropped (gaps). Ground truth is
known exactly, so a Kalman filter can be shown recovering the true track.

State and model (discrete white-noise-acceleration, "DWNA"):

    state x = [px, py, vx, vy]            position and velocity
    motion x_k = F x_{k-1} + w_k,   w_k ~ N(0, Q)
    meas   z_k = H x_k     + v_k,   v_k ~ N(0, R)      (position only)

    F = [[1,0,dt,0],[0,1,0,dt],[0,0,1,0],[0,0,0,1]]
    H = [[1,0,0,0],[0,1,0,0]]
    Q = q * DWNA(dt)   (couples acceleration noise into velocity and position)
    R = r * I_2

This one dataset serves the whole arc:
  - Ch 12 (static LMMSE): a single update step (estimate state from one z given a prior).
  - Ch 13 (recursive):    the 1D filter on the x-coordinate (px, vx).
  - Ch 14 (full Kalman):  the full 2D tracker, including estimation through the gaps.

Usage:
    python3 generate_tracking.py --out tracking.csv

Output columns: t, px, py, vx, vy (true state), zx, zy (measurements; empty on gaps).
The known model (F, H, Q, R, x0) is printed and written to tracking_model.txt.
"""

import argparse
import csv

import numpy as np


def dwna_Q(dt, q):
    """Discrete white-noise-acceleration process covariance for [px,py,vx,vy]."""
    a = dt**4 / 4.0
    b = dt**3 / 2.0
    c = dt**2
    return q * np.array(
        [
            [a, 0.0, b, 0.0],
            [0.0, a, 0.0, b],
            [b, 0.0, c, 0.0],
            [0.0, b, 0.0, c],
        ]
    )


def generate(n=200, dt=1.0, q=0.05, r=4.0, gap_frac=0.15, seed=42):
    """Simulate a constant-velocity track and noisy, partly-missing measurements.

    Returns (states, meas, observed) where states is (n,4), meas is (n,2), and
    observed is a length-n boolean mask (False where the measurement is dropped).
    """
    rng = np.random.default_rng(seed)

    F = np.array(
        [[1, 0, dt, 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=float
    )
    H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], dtype=float)
    Q = dwna_Q(dt, q)
    R = r * np.eye(2)

    x = np.array([0.0, 0.0, 1.0, 0.5])  # start at origin, constant-ish velocity
    states = np.empty((n, 4))
    meas = np.empty((n, 2))

    chol_Q = np.linalg.cholesky(Q + 1e-12 * np.eye(4))
    chol_R = np.linalg.cholesky(R)

    for k in range(n):
        x = F @ x + chol_Q @ rng.standard_normal(4)
        states[k] = x
        meas[k] = H @ x + chol_R @ rng.standard_normal(2)

    observed = rng.random(n) >= gap_frac
    observed[0] = True  # always see the first measurement

    return states, meas, observed, dict(F=F, H=H, Q=Q, R=R, x0=states[0])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="tracking.csv")
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--dt", type=float, default=1.0)
    ap.add_argument("--q", type=float, default=0.05, help="process-noise scale")
    ap.add_argument("--r", type=float, default=4.0, help="measurement-noise variance")
    ap.add_argument("--gap-frac", type=float, default=0.15)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    states, meas, observed, model = generate(
        n=args.n, dt=args.dt, q=args.q, r=args.r, gap_frac=args.gap_frac, seed=args.seed
    )

    with open(args.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["t", "px", "py", "vx", "vy", "zx", "zy"])
        for k in range(len(states)):
            px, py, vx, vy = states[k]
            if observed[k]:
                zx, zy = meas[k]
                w.writerow([k, px, py, vx, vy, zx, zy])
            else:
                w.writerow([k, px, py, vx, vy, "", ""])  # gap: no measurement

    model_path = args.out.rsplit(".", 1)[0] + "_model.txt"
    with open(model_path, "w") as f:
        np.set_printoptions(precision=4, suppress=True)
        f.write("Known linear-Gaussian state-space model (ground truth)\n\n")
        for k in ("F", "H", "Q", "R", "x0"):
            f.write(f"{k} =\n{model[k]}\n\n")
        f.write(f"dt={args.dt}, q={args.q}, r={args.r}, gap_frac={args.gap_frac}, seed={args.seed}\n")

    n_obs = int(observed.sum())
    print(f"wrote {args.out}: {len(states)} steps, {n_obs} measurements, "
          f"{len(states) - n_obs} gaps")
    print(f"wrote {model_path} (known F, H, Q, R, x0)")


if __name__ == "__main__":
    main()
