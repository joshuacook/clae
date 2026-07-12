import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import os

# Create directories if they don't exist
os.makedirs('templates/011', exist_ok=True)
os.makedirs('../../web/public/templates/011', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic classification dataset with different scales
from sklearn.datasets import make_classification

# Create dataset with two informative features of different scales
X, y = make_classification(
    n_samples=1000,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=2,
    class_sep=2.0,
    weights=[0.8, 0.2],  # Make first feature more important
    flip_y=0.1,
    random_state=42
)

# Scale second feature to be much larger
X[:, 0] = X[:, 0] * 50  # Make first feature 100x larger to mask true importance

# Extract features for clarity
feature1 = X[:, 0]  # First feature (smaller scale)
feature2 = X[:, 1]  # Second feature (larger scale)

# Scale features to compare
feature1_scaled = (feature1 - feature1.mean()) / feature1.std()
feature2_scaled = (feature2 - feature2.mean()) / feature2.std()

# Create three subplots showing different scaling approaches
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Set common limits

# Plot 1: Original scales
ax1.scatter(feature1, feature2, c=y, alpha=0.5)
ax1.set_xlabel('Feature 1 (original)')
ax1.set_ylabel('Feature 2 (100x larger)')
ax1.set_title('Original Scales')

# Plot 2: Adjusted axes to same scale
ax2.scatter(feature1, feature2, c=y, alpha=0.5)
ax2.set_xlabel('Feature 1')
ax2.set_ylabel('Feature 2')
ax2.set_title('Same Plot Scale')

# Plot 3: Standardized variables
ax3.scatter(feature1_scaled, feature2_scaled, c=y, alpha=0.5)
ax3.set_xlabel('Feature 1 (standardized)')
ax3.set_ylabel('Feature 2 (standardized)')
ax3.set_title('Standardized Variables')

plt.tight_layout()

# Save in both locations
plt.savefig('templates/011/scaling_comparison.png', dpi=300, bbox_inches='tight')
plt.savefig('../../web/public/templates/011/scaling_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

# Fit logistic regression models
X_raw = np.column_stack([feature1, feature2])
X_scaled = np.column_stack([feature1_scaled, feature2_scaled])

model_raw = LogisticRegression()
model_scaled = LogisticRegression()

model_raw.fit(X_raw, y)
model_scaled.fit(X_scaled, y)

# Create coefficient comparison plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Raw coefficients
x = np.arange(2)
ax1.bar(x, model_raw.coef_[0])
ax1.set_ylabel('Coefficient Value')
ax1.set_title('Raw Coefficients\nFeature 2 Dominates')
ax1.set_xticks(x)
ax1.set_xticklabels(['Feature 1', 'Feature 2'])
# ax1.set_ylim(0, 4)

# Scaled coefficients
ax2.bar(x, model_scaled.coef_[0])
ax2.set_ylabel('Coefficient Value')
ax2.set_title('Scaled Coefficients\nEqual Importance')
ax2.set_xticks(x)
ax2.set_xticklabels(['Feature 1', 'Feature 2'])
# ax2.set_ylim(0, 4)
plt.tight_layout()
plt.savefig('templates/011/coefficient_comparison.png', dpi=300, bbox_inches='tight')
plt.savefig('../../web/public/templates/011/coefficient_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

# Create normalization visualization
np.random.seed(42)
n_samples = 1000
x = np.random.normal(5, 2, n_samples)  # mean=5, std=2
noise = np.random.normal(0, 0.1, n_samples)  # small noise

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Original distribution
ax1.hist(x + noise, bins=50, alpha=0.7)
ax1.axvline(x=5, color='r', linestyle='--', label='Mean')
ax1.set_title('Original Distribution\nμ=5, σ=2')
ax1.set_xlabel('Value')
ax1.set_ylabel('Count')
ax1.set_xlim(-5, 5)
ax1.legend()

# Zero mean
x_centered = x - np.mean(x)
ax2.hist(x_centered + noise, bins=50, alpha=0.7)
ax2.axvline(x=0, color='r', linestyle='--', label='Mean')
ax2.set_title('Centered Distribution\nμ=0, σ=2')
ax2.set_xlabel('Value')
ax2.set_ylabel('Count')
ax2.set_xlim(-5, 5)
ax2.legend()

# Standardized
x_standardized = x_centered / np.std(x)
ax3.hist(x_standardized + noise/2, bins=50, alpha=0.7)
ax3.axvline(x=0, color='r', linestyle='--', label='Mean')
ax3.set_title('Standardized Distribution\nμ=0, σ=1')
ax3.set_xlabel('Value')
ax3.set_ylabel('Count')
ax3.legend()
ax3.set_xlim(-5, 5)
plt.tight_layout()
plt.savefig('templates/011/normalization_steps.png', dpi=300, bbox_inches='tight')
plt.savefig('../../web/public/templates/011/normalization_steps.png', dpi=300, bbox_inches='tight')
plt.close()

# Create min-max scaling visualization
np.random.seed(42)
n_samples = 1000
x = np.random.beta(2, 5, n_samples) * 2 - 1  # skewed distribution
noise = np.random.normal(0, 0.1, n_samples)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Original distribution
ax1.hist(x + noise, bins=50, alpha=0.7)
ax1.axvline(x=np.min(x), color='g', linestyle='--', label='Min')
ax1.axvline(x=np.max(x), color='r', linestyle='--', label='Max')
ax1.set_title('Original Distribution\nmin=%.1f, max=%.1f' % (np.min(x), np.max(x)))
ax1.set_xlabel('Value')
ax1.set_ylabel('Count')
ax1.set_xlim(-2, 2)
ax1.legend()

# Shifted to start at 0
x_shifted = x - np.min(x)
ax2.hist(x_shifted + noise, bins=50, alpha=0.7)
ax2.axvline(x=0, color='g', linestyle='--', label='Min')
ax2.axvline(x=np.max(x_shifted), color='r', linestyle='--', label='Max')
ax2.set_title('Shifted Distribution\nmin=0, max=%.1f' % np.max(x_shifted))
ax2.set_xlabel('Value')
ax2.set_ylabel('Count')
ax2.set_xlim(-2, 2)
ax2.legend()

# Min-max scaled
x_minmax = x_shifted / np.max(x_shifted)
ax3.hist(x_minmax, bins=50, alpha=0.7)
ax3.axvline(x=0, color='g', linestyle='--', label='Min')
ax3.axvline(x=1, color='r', linestyle='--', label='Max')
ax3.set_title('Min-Max Scaled\nmin=0, max=1')
ax3.set_xlabel('Value')
ax3.set_ylabel('Count')
ax3.legend()
ax3.set_xlim(-2, 2)
# Set common y limits for comparison
ylim = plt.ylim()
for ax in [ax1, ax2, ax3]:
    ax.set_ylim(ylim)

plt.tight_layout()
plt.savefig('templates/011/minmax_steps.png', dpi=300, bbox_inches='tight')
plt.savefig('../../web/public/templates/011/minmax_steps.png', dpi=300, bbox_inches='tight')
plt.close()

# Create robust scaling visualization comparing with standard scaling
np.random.seed(42)
n_samples = 1000

# Generate highly skewed data with more outliers
main_data = np.random.lognormal(0, 1.2, n_samples-50)  # More skewed log-normal
outliers = np.random.uniform(5, 10, 50)  # More outliers, slightly less extreme
x = np.concatenate([main_data, outliers])
noise = np.random.normal(0, 0.1, n_samples)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Original distribution with outliers
ax1.hist(x, bins=50, alpha=0.7, color='skyblue')
ax1.axvline(x=np.median(x), color='r', linestyle='--', label='Median')
ax1.axvline(x=np.mean(x), color='g', linestyle='--', label='Mean')
ax1.set_title('Original Skewed Distribution\nMean vs Median')
ax1.set_xlabel('Value')
ax1.set_ylabel('Count')
ax1.set_xlim(-5, 10)
ax1.legend()

# Compare standard vs robust scaling
x_standard = (x - np.mean(x)) / np.std(x)
x_robust = (x - np.median(x)) / (np.percentile(x, 75) - np.percentile(x, 25))

# Plot both scalings
ax2.hist(x_standard, bins=50, alpha=0.5, color='red', label='Standard')
ax2.hist(x_robust, bins=50, alpha=0.5, color='blue', label='Robust')
ax2.axvline(x=0, color='k', linestyle='--', label='Center')
ax2.set_title('Standard vs Robust Scaling\nRobust Better Preserves Structure')
ax2.set_xlabel('Scaled Value')
ax2.set_ylabel('Count')
ax2.set_xlim(-5, 10)
ax2.legend()

# Zoomed version without outliers
ax3.hist(x_standard, bins=50, alpha=0.5, color='red', label='Standard')
ax3.hist(x_robust, bins=50, alpha=0.5, color='blue', label='Robust')
ax3.axvline(x=0, color='k', linestyle='--', label='Center')
ax3.set_title('Zoomed View of Central Region\nComparing Both Methods')
ax3.set_xlabel('Scaled Value')
ax3.set_ylabel('Count')
ax3.set_xlim(-2, 2)  # Zoom to central region
ax3.legend()

plt.tight_layout()
plt.savefig('templates/011/robust_steps.png', dpi=300, bbox_inches='tight')
plt.savefig('../../web/public/templates/011/robust_steps.png', dpi=300, bbox_inches='tight')
plt.close()

