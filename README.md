# Hooke's Law analysis (simulated data)

A beginner Python project that estimates a spring constant, k,
from force and extension data.

## What it does
- Creates simulated spring readings with k = 200 N/m and small
  random errors (up to 0.3 N).
- Estimates k from two points and from a best-fit line (NumPy).
- Plots the true line, the simulated readings and the best fit.

## Results
- k from two points: 205.4 N/m
- k from best fit: 200.8 N/m

## Notes
The data is simulated, not measured. This project was inspired by
the Hooke's Law apparatus I built in my Workshop Practice course.
I wrote the code while learning Python, with explanations from an
AI assistant (Claude).

## Run it
pip install numpy matplotlib
python hookes_law_analysis.py