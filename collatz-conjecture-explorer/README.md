# Collatz Conjecture Analysis
This project explores the behavior of the Collatz Conjecture through various modifications using Python. The goal of this project is to analyze the path lengths of the Collatz sequence under different rules and probabilities, and visualize the results with statistical analysis.

## Overview
The project includes multiple variations of the Collatz Conjecture, each with its own method of calculating the next number in the sequence. The main variations are:

- Original Collatz Conjecture: For any odd number, apply the rule n = 3n + 1; for even numbers, apply n = n / 2. This variation is the traditional form of the conjecture.

- Modified Collatz Conjecture: This version introduces an additional rule where odd numbers have a chance of following either n = 3n + 1 or n = 3n - 1, adding complexity to the sequence.

- Probabilistic Collatz Conjecture: This variant introduces a probabilistic element where odd numbers have a probability (p) of applying either n = 3n + 1 or n = 3n - 1. The effect of different values of p on the path lengths is explored.

