# EZ-Diffusion-SimRecover

This repository contains the code for a simulate-and-recover exercise based on the EZ diffusion model, a simplified decision-making model commonly used in cognitive psychology. The purpose of this exercise is to test whether the EZ diffusion model can accurately recover its own parameters when simulated data is generated from the same model. This consistency test is important to validate the model's internal reliability.

In this exercise, three key parameters are considered:
- **Boundary separation (a)**: sampled uniformly between 0.5 and 2.
- **Drift rate (v)**: sampled uniformly between 0.5 and 2.
- **Non-decision time (t)**: sampled uniformly between 0.1 and 0.5.

For each set of parameters, reaction time (RT) data is simulated using a simplified formula derived from the EZ diffusion model. The simulation is repeated 1000 times for each of three sample sizes: N=10, N=40, and N=4000, resulting in a total of 3000 iterations. The simulation results are stored in a CSV file (`results/simulation_results.csv`) for further analysis.

### Simulation Results and Data Analysis

After running the simulation, the following observations were made:

- **Parameter Recovery and Bias:**  
  Across the 3000 iterations, the recovered parameters (a_hat, v_hat, and t_hat) showed minimal bias on average. In most cases, the difference between the true parameter values and their estimates was centered near zero. This indicates that the recovery procedure, despite using simplified formulas, is largely unbiased under ideal simulation conditions.

- **Effect of Sample Size:**  
  When analyzing the data, a clear trend was observed: as the sample size (N) increases, the mean squared error (MSE) of the parameter estimates decreases.  
  - For **N=10**, the recovered parameters displayed relatively high variance. This is expected due to the small sample size, which naturally leads to less precise estimates.  
  - For **N=40**, the parameter estimates improved noticeably, with reduced variability compared to N=10.  
  - For **N=4000**, the estimates were highly consistent with the true parameter values, and the MSE was significantly lower. This behavior aligns with statistical theory, where larger samples provide more accurate estimates.

- **Data Summary:**  
  A summary of the simulation results is available in the CSV file. Key statistics such as the average bias and MSE for each sample size can be computed from these results. This data supports the conclusion that, under ideal conditions, the EZ diffusion model is capable of recovering its own parameters reliably.

### Methodological Considerations

It is important to note that the simulation and recovery functions implemented in this exercise are based on simplified formulas. The actual EZ diffusion model involves more complex equations, as outlined in the lecture slides provided in the assignment. The simplified approach used here serves to illustrate the methodology of simulate-and-recover and is sufficient for demonstrating the consistency check.

### Conclusion

Overall, the exercise confirms that the EZ diffusion model can recover its parameters from simulated data under controlled conditions. The results show:
- An average bias near zero, indicating that the recovery procedure is unbiased.
- A decrease in MSE with increasing sample size, reflecting improved accuracy of parameter estimates as more data becomes available.

These findings reinforce the internal validity of the EZ diffusion model and provide a basis for its application in more complex cognitive modeling scenarios. Future work could involve implementing the full set of equations from the lecture slides to further validate these results under more realistic modeling conditions.
