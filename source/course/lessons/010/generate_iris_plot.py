import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from matplotlib.patches import Ellipse
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

def plot_iris_covariance():
    # Load iris data
    iris = load_iris()
    X = iris.data[:, :2]  # sepal length and width
    
    # Compute mean and covariance
    mean = np.mean(X, axis=0)
    cov = np.cov(X.T)
    
    # Compute eigenvalues and eigenvectors
    eigenvals, eigenvecs = np.linalg.eigh(cov)
    
    # Create figure
    plt.figure(figsize=(10, 8))
    
    # Plot data points
    plt.scatter(X[:, 0], X[:, 1], alpha=0.5, label='Iris measurements')
    
    # Plot mean point
    plt.scatter(mean[0], mean[1], color='red', s=100, label='Mean')
    
    # Add 95% confidence ellipse
    chi2_val = 5.991  # 95% confidence for 2 degrees of freedom
    angle = np.degrees(np.arctan2(eigenvecs[1, 0], eigenvecs[0, 0]))
    ellipse = Ellipse(xy=mean, 
                     width=2*np.sqrt(chi2_val*eigenvals[0]), 
                     height=2*np.sqrt(chi2_val*eigenvals[1]),
                     angle=angle,
                     fill=False,
                     color='red',
                     label='95% Confidence Region')
    plt.gca().add_patch(ellipse)
    
    # Add eigenvectors
    for i in range(2):
        # Scale eigenvectors by their eigenvalues for visualization
        scale = np.sqrt(eigenvals[i]) * 2
        eigvec = eigenvecs[:, i] * scale
        plt.arrow(mean[0], mean[1], 
                 eigvec[0], eigvec[1],
                 color='green', 
                 width=0.05,
                 head_width=0.15,
                 length_includes_head=True,
                 label=f'Eigenvector {i+1}')
    
    # Customize plot
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.title('Iris Sepal Measurements with Covariance Structure')
    plt.legend()
    plt.grid(True)
    
    # Save plot to templates directory with course and lesson IDs
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), 
                              'templates', 
                              'linalg_010_iris_covariance.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

def plot_petal_covariance():
    # Load iris data
    iris = load_iris()
    X = iris.data[:, 2:4]  # petal length and width
    
    # Compute mean and covariance
    mean = np.mean(X, axis=0)
    cov = np.cov(X.T)
    
    # Compute eigenvalues and eigenvectors
    eigenvals, eigenvecs = np.linalg.eigh(cov)
    
    # Create figure
    plt.figure(figsize=(10, 8))
    
    # Plot data points
    plt.scatter(X[:, 0], X[:, 1], alpha=0.5, label='Iris measurements')
    
    # Plot mean point
    plt.scatter(mean[0], mean[1], color='red', s=100, label='Mean')
    
    # Add 95% confidence ellipse
    chi2_val = 5.991  # 95% confidence for 2 degrees of freedom
    angle = np.degrees(np.arctan2(eigenvecs[1, 0], eigenvecs[0, 0]))
    ellipse = Ellipse(xy=mean, 
                     width=2*np.sqrt(chi2_val*eigenvals[0]), 
                     height=2*np.sqrt(chi2_val*eigenvals[1]),
                     angle=angle,
                     fill=False,
                     color='red',
                     label='95% Confidence Region')
    plt.gca().add_patch(ellipse)
    
    # Add eigenvectors
    for i in range(2):
        # Scale eigenvectors by their eigenvalues for visualization
        scale = np.sqrt(eigenvals[i]) * 2
        eigvec = eigenvecs[:, i] * scale
        plt.arrow(mean[0], mean[1], 
                 eigvec[0], eigvec[1],
                 color='green', 
                 width=0.05,
                 head_width=0.15,
                 length_includes_head=True,
                 label=f'Eigenvector {i+1}')
    
    # Customize plot
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Petal Width (cm)')
    plt.title('Iris Petal Measurements with Covariance Structure')
    plt.legend()
    plt.grid(True)
    
    # Save plot
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), 
                              'templates', 
                              'linalg_010_iris_petal_covariance.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

def plot_rotated_petal_covariance():
    # Load iris data
    iris = load_iris()
    X = iris.data[:, 2:4]  # petal length and width
    
    # Compute mean and covariance
    mean = np.mean(X, axis=0)
    X_centered = X - mean
    cov = np.cov(X_centered.T)
    
    # Compute eigenvalues and eigenvectors
    eigenvals, eigenvecs = np.linalg.eigh(cov)
    
    # Sort eigenvalues and eigenvectors in descending order
    idx = eigenvals.argsort()[::-1]
    eigenvals = eigenvals[idx]
    eigenvecs = eigenvecs[:, idx]
    
    # Rotate data to align with eigenvectors
    X_rotated = X_centered @ eigenvecs
    
    # Create figure
    plt.figure(figsize=(10, 8))
    
    # Plot rotated data points
    plt.scatter(X_rotated[:, 0], X_rotated[:, 1], alpha=0.5, label='Rotated measurements')
    
    # Plot mean point (should be at origin after centering)
    plt.scatter(0, 0, color='red', s=100, label='Mean')
    
    # Add 95% confidence ellipse
    chi2_val = 5.991  # 95% confidence for 2 degrees of freedom
    ellipse = Ellipse(xy=(0, 0), 
                     width=2*np.sqrt(chi2_val*eigenvals[0]), 
                     height=2*np.sqrt(chi2_val*eigenvals[1]),
                     angle=0,  # No rotation needed as data is already rotated
                     fill=False,
                     color='red',
                     label='95% Confidence Region')
    plt.gca().add_patch(ellipse)
    
    # Add standard basis vectors scaled by eigenvalues
    plt.arrow(0, 0, 
             np.sqrt(eigenvals[0])*2, 0,
             color='green', 
             width=0.05,
             head_width=0.15,
             length_includes_head=True,
             label='First Principal Component')
    plt.arrow(0, 0, 
             0, np.sqrt(eigenvals[1])*2,
             color='green', 
             width=0.05,
             head_width=0.15,
             length_includes_head=True,
             label='Second Principal Component')
    
    # Customize plot
    plt.xlabel('First Principal Component')
    plt.ylabel('Second Principal Component')
    plt.title('Rotated Iris Petal Measurements')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')  # Make sure aspect ratio is 1:1
    
    # Save plot
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), 
                              'templates', 
                              'linalg_010_iris_petal_rotated.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Change to script directory
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    plot_iris_covariance()
    plot_petal_covariance()
    plot_rotated_petal_covariance()
