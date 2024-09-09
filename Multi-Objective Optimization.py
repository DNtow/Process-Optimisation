# multi_objective_optimization.py
from scipy.optimize import differential_evolution


def objective_function(params, data):
    param1, param2 = params
    # Example objective function
    return np.sum((data.mean() - param1 * param2) ** 2)


def optimize_process(data):
    bounds = [(0, 10), (0, 10)]
    result = differential_evolution(objective_function, bounds, args=(data,))

    if result.success:
        print("Optimal parameters found:")
        print(f"Parameter 1: {result.x[0]}")
        print(f"Parameter 2: {result.x[1]}")
    else:
        print("Optimization failed.")
