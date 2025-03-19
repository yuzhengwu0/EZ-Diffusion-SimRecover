#!/bin/bash
# This script runs the complete 3000-iteration simulate-and-recover exercise.

echo "Running simulate-and-recover..."
python3 src/simulate_recover.py
echo "Simulation completed. Results saved to results/simulation_results.csv"
