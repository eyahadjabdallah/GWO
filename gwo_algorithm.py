import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

def sphere(x):
    return np.sum(x**2)

def gwo_with_tracking(obj_function, dim=2, num_wolves=20, max_iter=50, lower=-10, upper=10):
    positions = np.random.uniform(lower, upper, (num_wolves, dim))
    
    alpha_pos = np.zeros(dim)
    alpha_score = float("inf")
    
    beta_pos = np.zeros(dim)
    beta_score = float("inf")
    
    delta_pos = np.zeros(dim)
    delta_score = float("inf")
    
    history = []
    
    for iteration in range(max_iter):
        for i in range(num_wolves):
            fitness = obj_function(positions[i])
            
            if fitness < alpha_score:
                delta_score, delta_pos = beta_score, beta_pos.copy()
                beta_score, beta_pos = alpha_score, alpha_pos.copy()
                alpha_score, alpha_pos = fitness, positions[i].copy()
            elif fitness < beta_score:
                delta_score, delta_pos = beta_score, beta_pos.copy()
                beta_score, beta_pos = fitness, positions[i].copy()
            elif fitness < delta_score:
                delta_score, delta_pos = fitness, positions[i].copy()
        
        a = 2 - iteration * (2 / max_iter)
        
        for i in range(num_wolves):
            for j in range(dim):
                r1, r2 = np.random.random(), np.random.random()
                A1 = 2 * a * r1 - a
                C1 = 2 * r2
                D_alpha = abs(C1 * alpha_pos[j] - positions[i,j])
                X1 = alpha_pos[j] - A1 * D_alpha
                
                r1, r2 = np.random.random(), np.random.random()
                A2 = 2 * a * r1 - a
                C2 = 2 * r2
                D_beta = abs(C2 * beta_pos[j] - positions[i,j])
                X2 = beta_pos[j] - A2 * D_beta
                
                r1, r2 = np.random.random(), np.random.random()
                A3 = 2 * a * r1 - a
                C3 = 2 * r2
                D_delta = abs(C3 * delta_pos[j] - positions[i,j])
                X3 = delta_pos[j] - A3 * D_delta
                
                positions[i,j] = (X1 + X2 + X3) / 3
            
            positions[i] = np.clip(positions[i], lower, upper)
        
        history.append(positions.copy())
    
    return history

def animate_gwo(history):
    fig, ax = plt.subplots(figsize=(6,6))
    
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_title("Grey Wolf Optimizer — Wolf Movement Animation")
    
    scat = ax.scatter([], [], s=40, color='blue')
    alpha_marker, = ax.plot([], [], 'ro', markersize=10, label="Alpha")
    
    def update(frame):
        positions = history[frame]
        scat.set_offsets(positions)
        
        fitnesses = [sphere(p) for p in positions]
        alpha_idx = np.argmin(fitnesses)
        alpha_pos = positions[alpha_idx]
        
        alpha_marker.set_data([alpha_pos[0]], [alpha_pos[1]])
        ax.set_xlabel(f"Iteration {frame+1}")
        return scat, alpha_marker
    
    ani = FuncAnimation(fig, update, frames=len(history), interval=200, blit=True)
    return HTML(ani.to_jshtml())

if __name__ == "__main__":
    history = gwo_with_tracking(sphere, dim=2, num_wolves=25, max_iter=60)
    print(f"Optimization completed with {len(history)} iterations")
```

**`requirements.txt`** :
```
numpy>=1.21.0
matplotlib>=3.4.0
ipython>=7.0.0