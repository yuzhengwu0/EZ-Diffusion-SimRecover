#!/bin/bash
# This script runs the test suite for the simulate-and-recover exercise.

echo "Running tests..."
python3 -m pytest test/test_simulate.py
