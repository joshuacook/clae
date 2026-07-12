import numpy as np
import matplotlib.pyplot as plt
import os

# Create directories if they don't exist
os.makedirs('templates/012', exist_ok=True)
os.makedirs('../../web/public/templates/012', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

def plot_diagonalization_example():
    """Create visualization of diagonalization steps"""
    # Create a simple 2x2 symmetric matrix
    A = np.array([[4, -1], 
                  [-1, 4]])
    
    # Get eigendecomposition
    eigvals, eigvecs = np.linalg.eigh(A)
    
    # Create key vectors
    vectors = np.array([
        [1, 0],    # unit vector along x
        [0, 1],    # unit vector along y
        [1, 1],    # diagonal vector
        [-1, 1],   # other diagonal
        [2, 1],    # arbitrary vector
        [-1, 2],   # another arbitrary vector
    ])
    
    # Transform vectors
    transformed = vectors @ A
    diagonalized = vectors @ eigvecs @ np.diag(eigvals)
    
    # Plot
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    # Colors for matching vectors  
    colors = ['red', 'blue', 'green', 'purple',
             'orange', 'brown']
    
    # Labels for vectors
    labels = ['x', 'y', 'diag1', 'diag2',
             'v1', 'v2']
    
    # Create grid points
    x = np.linspace(-3, 3, 80)  # Quadrupled density
    y = np.linspace(-3, 3, 80)
    X, Y = np.meshgrid(x, y)
    points = np.column_stack([X.ravel(), Y.ravel()])
    
    # Transform grid points
    transformed_points = points @ A
    diagonalized_points = points @ eigvecs @ np.diag(eigvals)
    
    # Original vectors and grid
    ax1.scatter(X.flatten(), Y.flatten(), color='lightblue', alpha=0.7, s=1)
    for i, (vector, color) in enumerate(zip(vectors, colors)):
        ax1.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', 
                  scale=1, color=color, label=labels[i])
    ax1.set_title('Original Vectors')
    ax1.axis('equal')
    ax1.grid(True)
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax1.legend()
    
    # After A transformation
    transformed_grid = transformed_points.reshape(80, 80, 2)
    ax2.scatter(transformed_grid[:, :, 0].flatten(), 
                transformed_grid[:, :, 1].flatten(), 
                color='lightblue', alpha=0.7, s=1)
    for i, (vector, color) in enumerate(zip(transformed, colors)):
        ax2.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', 
                  scale=1, color=color, label=f'A{labels[i]}')
    ax2.set_title('After A Transformation')
    ax2.axis('equal')
    ax2.grid(True)
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-3, 3)
    ax2.legend()
    
    # After diagonalization
    diagonalized_grid = diagonalized_points.reshape(80, 80, 2)
    ax3.scatter(diagonalized_grid[:, :, 0].flatten(),
                diagonalized_grid[:, :, 1].flatten(),
                color='lightblue', alpha=0.7, s=1)
    for i, (vector, color) in enumerate(zip(diagonalized, colors)):
        ax3.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', 
                  scale=1, color=color, label=f'D{labels[i]}')
    ax3.set_title('After Diagonalization')
    ax3.axis('equal')
    ax3.grid(True)
    ax3.set_xlim(-3, 3)
    ax3.set_ylim(-3, 3)
    ax3.legend()
    
    plt.tight_layout()
    plt.savefig('templates/012/diagonalization_steps.png', dpi=300, bbox_inches='tight')
    plt.savefig('../../web/public/templates/012/diagonalization_steps.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_svd_example():
    """Create visualization of SVD steps with rectangular matrix"""
    # Create a 3x2 matrix mapping from R² to R³
    A = np.array([[2, 1],    # First output component
                  [1, 2],    # Second output component
                  [1, 0]])   # Third output component
    
    # Get SVD components
    U, s, Vh = np.linalg.svd(A)
    
    # Create key vectors
    vectors = np.array([
        [1, 0],    # unit vector along x
        [0, 1],    # unit vector along y
        [1, 1],    # diagonal vector
        [-1, 1],   # other diagonal
        [2, 1],    # arbitrary vector
        [-1, 2],   # another arbitrary vector
    ])
    
    # Transform vectors through SVD steps
    rotated = vectors @ Vh.T  # First rotation in R² (2x2)
    
    # Create full rectangular Σ matrix (3×2)
    Sigma = np.zeros((3, 2))
    Sigma[:2, :2] = np.diag(s)
    
    scaled = rotated @ Sigma.T  # Scaling and mapping to R³ (2x2 -> 3x2)
    final = scaled @ U  # Final rotation in R³ (3x3)
    
    # Plot with 5 subplots - 2D, 3D, 2D, 2D, 3D
    fig = plt.figure(figsize=(25, 5))
    ax1 = fig.add_subplot(151)  # Original in R²
    ax2 = fig.add_subplot(152, projection='3d')  # After A in R³
    ax3 = fig.add_subplot(153)  # After V^T in R²
    ax4 = fig.add_subplot(154, projection='3d')  # After Σ in R³
    ax5 = fig.add_subplot(155, projection='3d')  # After U in R³
    
    # Colors for matching vectors  
    colors = ['red', 'blue', 'green', 'purple',
             'orange', 'brown']
    
    # Labels for vectors
    labels = ['x', 'y', 'diag1', 'diag2',
             'v1', 'v2']
    
    # Create grid points
    x = np.linspace(-3, 3, 80)
    y = np.linspace(-3, 3, 80)
    X, Y = np.meshgrid(x, y)
    points = np.column_stack([X.ravel(), Y.ravel()])
    
    # Transform grid points
    rotated_points = points @ Vh.T  # In R²
    scaled_points = rotated_points @ Sigma.T  # Map to R³
    final_points = scaled_points @ U  # Rotate in R³
    
    # Original vectors and grid
    ax1.scatter(X.flatten(), Y.flatten(), color='lightblue', alpha=0.7, s=1)
    for i, (vector, color) in enumerate(zip(vectors, colors)):
        ax1.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', 
                  scale=1, color=color, label=labels[i])
    ax1.set_title('Original Space')
    ax1.axis('equal')
    ax1.grid(True)
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax1.legend()
    
    # After A transformation (in R³)
    transformed = A @ vectors.T  # Direct transformation by A (3×2 × 2×n = 3×n)
    transformed_grid = (A @ points.T).T.reshape(80, 80, 3)  # Transform to R³

    # After V^T transformation (in R²)
    rotated_grid = rotated_points.reshape(80, 80, 2)
    ax3.scatter(rotated_grid[:, :, 0].flatten(),
                rotated_grid[:, :, 1].flatten(),
                color='lightblue', alpha=0.7, s=1)
    for i, (vector, color) in enumerate(zip(rotated, colors)):
        ax3.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', 
                  scale=1, color=color, label=f'V^T{labels[i]}')
    ax3.set_title('After V^T (First Rotation)')
    ax3.axis('equal')
    ax3.grid(True)
    ax3.set_xlim(-3, 3)
    ax3.set_ylim(-3, 3)
    ax3.legend()
    
    # After Σ transformation (in R³)
    scaled_grid = scaled_points.reshape(80, 80, 3)
    ax4.scatter(scaled_grid[:, :, 0].flatten(),
                scaled_grid[:, :, 1].flatten(),
                scaled_grid[:, :, 2].flatten(),
                color='lightblue', alpha=0.7)
    for i, (vector, color) in enumerate(zip(scaled, colors)):
        ax4.quiver(0, 0, 0,  # Start at origin
                  vector[0], vector[1], vector[2],  # 3D vector
                  color=color, label=f'Σ{labels[i]}')
    ax4.set_title('After Σ (R³)')
    ax4.set_xlim(-3, 3)
    ax4.set_ylim(-3, 3)
    ax4.set_zlim(-3, 3)
    ax4.legend()
    ax2.scatter(transformed_grid[:, :, 0].flatten(),
                transformed_grid[:, :, 1].flatten(),
                transformed_grid[:, :, 2].flatten(),
                color='lightblue', alpha=0.7)
    for i, (vector, color) in enumerate(zip(transformed, colors)):
        ax2.quiver(0, 0, 0,  # Start at origin
                  vector[0], vector[1], vector[2],  # 3D vector components
                  color=color, label=f'A{labels[i]}')
    ax2.set_title('After A (R³)')
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-3, 3)
    ax2.set_zlim(-3, 3)
    ax2.legend()

    # After U transformation (in R³)
    final_grid = final_points.reshape(80, 80, 3)
    ax5.scatter(final_grid[:, :, 0].flatten(),
                final_grid[:, :, 1].flatten(),
                final_grid[:, :, 2].flatten(),
                color='lightblue', alpha=0.7)
    for i, (vector, color) in enumerate(zip(final, colors)):
        ax5.quiver(0, 0, 0,  # Start at origin
                  vector[0], vector[1], vector[2],  # 3D vector
                  color=color, label=f'U{labels[i]}')
    ax5.set_title('After U (R³)')
    ax5.set_xlim(-3, 3)
    ax5.set_ylim(-3, 3)
    ax5.set_zlim(-3, 3)
    ax5.legend()
    
    plt.tight_layout()
    plt.savefig('templates/012/svd_example.png', dpi=300, bbox_inches='tight')
    plt.savefig('../../web/public/templates/012/svd_example.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Ensure we're using the right Python environment
    import sys
    print(f"Using Python: /opt/miniconda3/envs/la-goose/bin/python")
    
    # Verify we can import required packages
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting
    print("Required packages imported successfully")
    
    plot_diagonalization_example()
    plot_svd_example()
