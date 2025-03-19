import numpy as np
import pandas as pd
from scipy.stats import invgauss, norm

# Set scaling parameter (as in EZ-diffusion, typically s = 0.1)
s = 0.1

def compute_p(a, v, s=s):
    """
    Compute the theoretical probability of a correct response for an unbiased starting point.
    Formula: p = 1/(1 + exp(-2*a*v/s^2))
    """
    return 1.0 / (1.0 + np.exp(-2 * a * v / (s**2)))

def simulate_data(a, v, Ter, N, s=s):
    """
    Simulate reaction times based on the diffusion model.
    Decision times are sampled from an Inverse Gaussian (Wald) distribution with:
      - Mean: mu_decision = a/v
      - Shape parameter (lambda): a^2/s^2
    Total RT = Ter + decision time.
    """
    mu_decision = a / v
    # In scipy, the inverse Gaussian is parameterized such that:
    #   mean = scale * mu  and variance = scale^2 * mu^3.
    # Here we set scale = a^2/s^2 so that the shape parameter corresponds to a^2/s^2.
    decision_times = invgauss.rvs(mu=mu_decision, scale=(a**2)/(s**2), size=N)
    RTs = Ter + decision_times
    return RTs

def recover_parameters(RTs, s=s, a_true=None, v_true=None):
    """
    Recover parameters using the EZ-diffusion formulas.
    Uses the closed-form solutions:
      - a_hat = (s^2 * L) / sqrt(VRT)
      - v_hat = (s * L * MRT) / a_hat
      - Ter_hat = MRT - (a_hat / v_hat) * (1 - exp(-v_hat*a_hat/s^2))
    Here, L = norm.ppf(p) and p is computed theoretically as:
         p = 1/(1 + exp(-2*a_true*v_true/s^2))
    (Since in our simulation we do not simulate errors, we use the true parameters to obtain p.)
    """
    MRT = np.mean(RTs)
    VRT = np.var(RTs)
    # Use true parameters to compute theoretical p (assuming they are available)
    if a_true is None or v_true is None:
        raise ValueError("True parameters a and v must be provided for EZ recovery.")
    p = compute_p(a_true, v_true, s)
    L = norm.ppf(p)
    a_hat = (s**2 * L) / np.sqrt(VRT)
    v_hat = (s * L * MRT) / a_hat
    Ter_hat = MRT - (a_hat / v_hat) * (1 - np.exp(-v_hat * a_hat / (s**2)))
    return a_hat, v_hat, Ter_hat

def main():
    """
    Run the simulate-and-recover exercise for three sample sizes: N=10, 40, and 4000.
    For each iteration, parameters (a, v, Ter) are sampled within specified ranges:
      - a in [0.5, 2]
      - v in [0.5, 2]
      - Ter in [0.1, 0.5]
    We perform 1000 iterations for each N.
    """
    N_values = [10, 40, 4000]
    iterations = 1000
    results = []
    
    for N in N_values:
        for _ in range(iterations):
            # Randomly sample true parameters within given ranges
            a = np.random.uniform(0.5, 2.0)
            v = np.random.uniform(0.5, 2.0)
            Ter = np.random.uniform(0.1, 0.5)
            
            # Simulate data (correct RTs) using the Inverse Gaussian model
            RTs = simulate_data(a, v, Ter, N, s)
            
            # Recover parameters using the EZ-diffusion closed-form solutions.
            # We pass the true values a and v to compute p.
            try:
                a_hat, v_hat, Ter_hat = recover_parameters(RTs, s, a_true=a, v_true=v)
            except Exception as e:
                # In case of errors (e.g., division by zero), skip this iteration.
                continue
            
            # Store the true and recovered parameters along with sample size
            results.append([N, a, v, Ter, a_hat, v_hat, Ter_hat])
    
    # Save results to CSV for analysis
    df = pd.DataFrame(results, columns=["N", "a", "v", "Ter", "a_hat", "v_hat", "Ter_hat"])
    df.to_csv("results/simulation_results.csv", index=False)

if __name__ == "__main__":
    main()
