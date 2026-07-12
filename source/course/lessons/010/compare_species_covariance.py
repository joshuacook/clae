import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from matplotlib.patches import Ellipse
import matplotlib
from scipy import stats
matplotlib.use('Agg')  # Use non-interactive backend

def plot_species_covariance_comparison():
    # Load iris data
    iris = load_iris()
    X = iris.data[:, :2]  # sepal length and width
    species = iris.target
    
    # Create figure
    plt.figure(figsize=(10, 8))
    species_names = ['Setosa', 'Versicolor', 'Virginica']
    colors = ['blue', 'orange', 'green']
    
    # Store covariance matrices and sample sizes for F-test
    covs = []
    ns = []
    
    for i in range(3):
        # Get data for this species
        mask = species == i
        X_species = X[mask]
        n = len(X_species)
        ns.append(n)
        
        # Compute mean and covariance
        mean = np.mean(X_species, axis=0)
        cov = np.cov(X_species.T)
        covs.append(cov)
        
        # Compute eigenvalues and eigenvectors for ellipse
        eigenvals, eigenvecs = np.linalg.eigh(cov)
        
        # Plot data points
        plt.scatter(X_species[:, 0], X_species[:, 1], alpha=0.5, 
                   color=colors[i], label=f'{species_names[i]}')
        
        # Plot mean point
        plt.scatter(mean[0], mean[1], color=colors[i], s=100, marker='*',
                   label=f'{species_names[i]} mean')
        
        # Add 95% confidence ellipse
        chi2_val = 5.991  # 95% confidence for 2 degrees of freedom
        angle = np.degrees(np.arctan2(eigenvecs[1, 0], eigenvecs[0, 0]))
        ellipse = Ellipse(xy=mean, 
                         width=2*np.sqrt(chi2_val*eigenvals[0]), 
                         height=2*np.sqrt(chi2_val*eigenvals[1]),
                         angle=angle,
                         fill=False,
                         color=colors[i],
                         label=f'{species_names[i]} 95% Confidence')
        plt.gca().add_patch(ellipse)
    
    # Customize plot
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.title('Iris Species Comparison with Covariance Structure')
    plt.legend()
    plt.grid(True)
    
    # Perform univariate F-test on sepal width
    print("\nUnvariate F-test for sepal width:")
    setosa_width = X[species == 0, 1]
    versicolor_width = X[species == 1, 1]
    virginica_width = X[species == 2, 1]
    
    F_stat, p_val = stats.f_oneway(setosa_width, 
                                  versicolor_width, 
                                  virginica_width)
    print(f"F-statistic: {F_stat:.4f}")
    print(f"p-value: {p_val:.4f}")
    
    # Perform F-tests between species for full covariance:
    print("\nF-tests for equality of covariance matrices:")
    for i in range(3):
        for j in range(i+1, 3):
            # Box's M test statistic
            det_i = np.linalg.det(covs[i])
            det_j = np.linalg.det(covs[j])
            F_stat = det_i / det_j
            
            # Degrees of freedom
            df1 = (ns[i] - 1)
            df2 = (ns[j] - 1)
            
            # Compute p-value
            p_value = 2 * min(
                stats.f.cdf(F_stat, df1, df2),
                1 - stats.f.cdf(F_stat, df1, df2)
            )
            
            print(f"\n{species_names[i]} vs {species_names[j]}:")
            print(f"F statistic: {F_stat:.4f}")
            print(f"p-value: {p_value:.4f}")
            print(f"Determinant ratio: {det_i/det_j:.4f}")
    
    # Save plot
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), 
                              'templates', 
                              'linalg_010_iris_species_comparison.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Change to script directory
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    plot_species_covariance_comparison()
