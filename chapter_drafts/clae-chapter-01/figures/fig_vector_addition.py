"""Figure: vector addition, tip-to-tail.

Reproduce with:
    clae-py chapter_drafts/clae-chapter-01/figures/fig_vector_addition.py
"""
import os

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def plot_vector(v, color="blue", label=None, **kw):
    plt.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1,
               color=color, label=label, **kw)


def main():
    v1 = np.array([1, 2])
    v2 = np.array([3, 1])

    plt.figure(figsize=(6, 6))
    plt.axhline(0, color="k", lw=0.5)
    plt.axvline(0, color="k", lw=0.5)
    plot_vector(v1, "tab:blue", "v1")
    plot_vector(v2, "tab:red", "v2")
    plot_vector(v1 + v2, "tab:green", "v1 + v2")
    # the second leg of the walk: v2 carried to the tip of v1
    plt.quiver(v1[0], v1[1], v2[0], v2[1], angles="xy", scale_units="xy",
               scale=1, color="tab:red", alpha=0.35)
    plt.xlim(-1, 5)
    plt.ylim(-1, 4)
    plt.gca().set_aspect("equal")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.title("Vector addition: tip to tail")
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fig_vector_addition.png")
    plt.savefig(out, dpi=150, bbox_inches="tight")
    print("wrote", out)


if __name__ == "__main__":
    main()
