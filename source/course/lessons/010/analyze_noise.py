import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from matplotlib.patches import Ellipse
import matplotlib
from scipy import stats
matplotlib.use('Agg')  # Use non-interactive backend

def analyze_measurement_noise():
    # Load iris data
    iris = load_iris()
    X = iris.data[:, :2]  # sepal length and width
    species = iris.target
    
    # Parameters for noise simulation
    n_simulations = 1000
    measurement_noise = 0.039  # Set to match smaller eigenvalue
    
    # Store results
    F_stats = []
    
    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Plot variance comparison
    variances = []
    labels = []
    for i, name in enumerate(['Setosa', 'Versicolor', 'Virginica']):
        mask = species == i
        X_species = X[mask]
        cov = np.cov(X_species.T)
        var_total = np.trace(cov)  # Total variance for species
        variances.extend([var_total, measurement_noise**2])
        labels.extend([f'{name}\nTotal Variance', f'{name}\nMeasurement\nNoise'])
    
    # Add population variance
    cov_all = np.cov(X.T)
    var_total = np.trace(cov_all)
    variances.extend([var_total, measurement_noise**2])
    labels.extend(['All Species\nTotal Variance', 'Measurement\nNoise'])
    
    # Create bar plot
    bars = ax1.bar(range(len(variances)), variances)
    ax1.set_xticks(range(len(labels)))
    ax1.set_xticklabels(labels, rotation=45, ha='right')
    ax1.set_title('Variance Comparison')
    ax1.set_ylabel('Variance (cm²)')
    
    # Add horizontal line for measurement noise
    ax1.axhline(y=measurement_noise**2, color='r', linestyle='--', 
                label='Measurement Noise Level')
    ax1.legend()
    ax1.grid(True)
    
    # Simulate noisy measurements
    for _ in range(n_simulations):
        # Add random noise to measurements
        X_noisy = X + np.random.normal(0, measurement_noise, X.shape)
        
        # Compute F-statistic between species
        F_stats_sim = []
        for i in range(3):
            for j in range(i+1, 3):
                mask_i = species == i
                mask_j = species == j
                
                # Compute covariance matrices
                cov_i = np.cov(X_noisy[mask_i].T)
                cov_j = np.cov(X_noisy[mask_j].T)
                
                # Compute F-statistic
                F_stat = np.linalg.det(cov_i) / np.linalg.det(cov_j)
                F_stats_sim.append(F_stat)
        
        F_stats.append(F_stats_sim)
    
    # Plot F-statistic distributions
    F_stats = np.array(F_stats)
    labels = ['Setosa vs Versicolor', 
              'Setosa vs Virginica', 
              'Versicolor vs Virginica']
    
    for i in range(3):
        ax2.hist(F_stats[:, i], bins=30, alpha=0.3, 
                label=labels[i])
    
    ax2.set_title('F-statistic Distribution\nwith Measurement Noise')
    ax2.set_xlabel('F-statistic')
    ax2.set_ylabel('Frequency')
    ax2.legend()
    ax2.grid(True)
    
    # Save plot
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), 
                              'templates', 
                              'linalg_010_noise_analysis.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    # Compute eigenvalues of original data
    eigenvals, _ = np.linalg.eigh(np.cov(X.T))
    print("\nOriginal Data Analysis:")
    print(f"Larger eigenvalue: {eigenvals[1]:.4f}")
    print(f"Smaller eigenvalue: {eigenvals[0]:.4f}")
    print(f"Ratio: {eigenvals[1]/eigenvals[0]:.4f}")
    
    # Print noise simulation statistics
    print("\nNoise Analysis Results:")
    for i, label in enumerate(labels):
        mean_F = np.mean(F_stats[:, i])
        std_F = np.std(F_stats[:, i])
        print(f"\n{label}:")
        print(f"Mean F-statistic: {mean_F:.4f}")
        print(f"Std F-statistic: {std_F:.4f}")
        print(f"95% CI: ({np.percentile(F_stats[:, i], 2.5):.4f}, "
              f"{np.percentile(F_stats[:, i], 97.5):.4f})")
        
    # Compare noise level to smaller eigenvalue
    print(f"\nMeasurement noise ({measurement_noise:.4f}) compared to smaller eigenvalue ({eigenvals[0]:.4f})")
    print(f"Ratio: {eigenvals[0]/measurement_noise:.4f}")

if __name__ == "__main__":
    # Change to script directory
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    analyze_measurement_noise()
