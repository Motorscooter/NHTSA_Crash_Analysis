import pandas as pd
import numpy as np
import scipy.integrate as integrate


# Calculate the head injury criterion (HIC) for a given crash with the given acceleration, time, and delta t
def calculate_hic(acceleration, time, delta_t):
    # Calculate the integral of the acceleration
    integral = integrate.cumtrapz(acceleration, time, initial=0)
    # Calculate the maximum value of the integral
    max_integral = max(integral)
    # Calculate the HIC
    hic = (delta_t / 1000) * (max_integral / 9.81) ** 2.5
    return hic

