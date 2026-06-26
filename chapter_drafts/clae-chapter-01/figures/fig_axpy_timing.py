"""Figure: axpy timing -- pure-Python list comprehension vs NumPy vectorized.

Reproduce with:
    clae-py chapter_drafts/clae-chapter-01/figures/fig_axpy_timing.py
"""
import os
import time

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

A = 2.5


def by_hand(a, x, y):       # pure Python, a list comprehension over the entries
    return [a * xi + yi for xi, yi in zip(x, y)]


def vectorized(a, x, y):    # NumPy, the whole array at once
    return a * x + y


def best(fn, *args, reps):
    times = []
    for _ in range(reps):
        t0 = time.perf_counter()
        fn(*args)
        times.append(time.perf_counter() - t0)
    return min(times)


def main():
    rng = np.random.default_rng(0)
    ns = np.logspace(3, 7, 9).astype(int)
    t_loop, t_vec = [], []
    for n in ns:
        x = rng.random(n)
        y = rng.random(n)
        t_loop.append(best(by_hand, A, x, y, reps=(1 if n > 1_000_000 else 3)))
        t_vec.append(best(vectorized, A, x, y, reps=7))

    t_loop = np.array(t_loop)
    t_vec = np.array(t_vec)
    print(f"n = {ns[-1]:,}:  by_hand {t_loop[-1]*1e3:.0f} ms   "
          f"vectorized {t_vec[-1]*1e3:.1f} ms   factor {t_loop[-1]/t_vec[-1]:.0f}x")

    plt.figure(figsize=(7, 5))
    plt.semilogx(ns, t_loop, "o-", label="by_hand (pure-Python list comprehension)")
    plt.semilogx(ns, t_vec, "s-", label="vectorized (NumPy)")
    plt.xlabel("n  (length of x and y)")
    plt.ylabel("wall-clock time (s)")
    plt.title("axpy: scale a vector and add another, loop vs vectorized")
    plt.legend()
    plt.grid(True, which="both", alpha=0.3)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fig_axpy_timing.png")
    plt.savefig(out, dpi=150, bbox_inches="tight")
    print("wrote", out)


if __name__ == "__main__":
    main()
