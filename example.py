from gwo_algorithm import gwo_with_tracking, sphere, animate_gwo

# Run GWO
history = gwo_with_tracking(sphere, dim=2, num_wolves=25, max_iter=60)

# Get best solution
final_positions = history[-1]
fitnesses = [sphere(p) for p in final_positions]
best_idx = min(range(len(fitnesses)), key=lambda i: fitnesses[i])
best_solution = final_positions[best_idx]

print(f"Best solution found: {best_solution}")
print(f"Best fitness: {sphere(best_solution)}")

# Animate (in Jupyter notebook)
# animate_gwo(history)