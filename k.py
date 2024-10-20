import numpy as np
import matplotlib.pyplot as plt

def initialize_centroids(data, k):
    """Randomly select k data points as initial centroids."""
    indices = np.random.choice(data.shape[0], size=k, replace=False)
    return data[indices]

def assign_clusters(data, centroids):
    """Assign each data point to the nearest centroid."""
    distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)

def update_centroids(data, clusters, k):
    """Update centroids as the mean of the assigned clusters."""
    return np.array([data[clusters == i].mean(axis=0) for i in range(k)])

def kmeans(data, k, max_iterations=100):
    """Run the K-means clustering algorithm."""
    centroids = initialize_centroids(data, k)
    
    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(data, clusters, k)
        
        # Check for convergence (if centroids do not change)
        if np.all(centroids == new_centroids):
            break
        
        centroids = new_centroids

    return clusters, centroids

# Example usage
if __name__ == "__main__":
    # Sample data: 2D points
    data = np.array([
        [1, 2],
        [1, 4],
        [1, 0],
        [4, 2],
        [4, 4],
        [4, 0]
    ])
    
    # Number of clusters
    k = 2
    
    # Perform K-means clustering
    clusters, centroids = kmeans(data, k)

    # Print the results
    print("Cluster assignments:", clusters)
    print("Centroids:", centroids)

    # Plotting the results
    plt.scatter(data[:, 0], data[:, 1], c=clusters, s=50, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, marker='X')
    plt.title('K-means Clustering')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

