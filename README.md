# Grey Wolf Optimizer (GWO) Implementation

##  Description
Implementation of the Grey Wolf Optimizer algorithm with animated visualization for optimization problems.

##  Links
- **GitHub Repository**: [https://github.com/eyahadjabdallah/GWO](https://github.com/eyahadjabdallah/GWO)
- **Google Colab Notebook** (with results): [Open in Colab](https://colab.research.google.com/drive/1wfEhDgoEm6Zw9xCs0lQU3WkzGSBrmJIO?usp=sharing)

##  Installation
```bash
pip install -r requirements.txt
```

##  Usage
```python
from gwo_algorithm import gwo_with_tracking, sphere

# Run optimization
history = gwo_with_tracking(sphere, dim=2, num_wolves=25, max_iter=60)

# Get best solution
final_positions = history[-1]
fitnesses = [sphere(p) for p in final_positions]
best_solution = final_positions[min(range(len(fitnesses)), key=lambda i: fitnesses[i])]
print(f"Best solution: {best_solution}")
```

##  Features
- Grey Wolf Optimizer implementation
- Animated visualization of wolf movements
- Convergence tracking
- Customizable parameters

##  Example
Run `example.py` to see a basic optimization example, or check the **Google Colab notebook** for interactive results.

##  AI Tools Used
- **Claude (Anthropic)** - Code development and documentation
- **Google Colab** - Code execution and visualization
- [Add other AI tools you'll use for PPT/images/videos]

##  References
Grey Wolf Optimizer algorithm based on the paper by Mirjalili et al. (2014)
```
__pycache__/
*.pyc
.ipynb_checkpoints/
*.egg-info/
dist/
build/
.DS_Store
