import numpy as np
import pandas as pd

# Function to simulate RT data based on EZ diffusion model
def simulate_data(a, v, t, N):
    """Simulates reaction time (RT) data for given model parameters and sample size N."""
    # This is a simplified approach; in real EZ, you would use the exact equations from the slides
    RTs = t + (a / v) * np.tanh(v * np.random.randn(N))
    return RTs

# Function to estimate parameters from simulated data
def recover_parameters(RTs):
    """Estimates a, v, and t from simulated reaction times."""
    mean_RT = np.mean(RTs)
    std_RT = np.std(RTs)
    
    # These are placeholder formulas, not the exact EZ formulas.
    # Replace them with the proper equations from the slides if needed.
    v_hat = 0.1 / std_RT
    a_hat = v_hat * mean_RT
    t_hat = np.min(RTs) - 0.05
    
    return a_hat, v_hat, t_hat

def main():
    """Runs the simulate-and-recover exercise for N=10,40,4000 with 1000 iterations each."""
    N_values = [10, 40, 4000]
    iterations = 1000
    results = []
    
    for N in N_values:
        for _ in range(iterations):
            # Randomly sample parameters within given range
            a = np.random.uniform(0.5, 2.0)
            v = np.random.uniform(0.5, 2.0)
            t = np.random.uniform(0.1, 0.5)
            
            # Simulate data
            RTs = simulate_data(a, v, t, N)
            
            # Recover parameters
            a_hat, v_hat, t_hat = recover_parameters(RTs)
            
            # Store results
            results.append([N, a, v, t, a_hat, v_hat, t_hat])
    
    # Save results to CSV
    df = pd.DataFrame(results, columns=["N", "a", "v", "t", "a_hat", "v_hat", "t_hat"])
    df.to_csv("results/simulation_results.csv", index=False)

if __name__ == "__main__":
    main()
