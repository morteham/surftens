"""Module for plotting surface tension.
A. Mulero, I. Cachadiña and M. I. Parra
Recommended Correlations for the Surface Tension of Common Fluids
Journal of Physical and Chemical Reference Data
2012
doi: 10.1063/1.4768782
"""
import numpy as np
import os
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
NIST_PATH = os.path.join(ROOT_DIR, "data/nist.json")
def surftens(name, Tr):
    """
    Calculate pure fluid surface tension
    Args:
        name (str): Component name
        Tr (np.ndarray): Reduced temperature
    Returns:
        sigma (np.ndarray): Surface tension (mN/m)
    """
    ff = open(NIST_PATH, "r")
    complist = json.load(ff)
    ff.close()
    sigma = np.zeros_like(Tr)
    for i in range(len(complist[name]["sigma"])):
        sigma[:] += complist[name]["sigma"][i] * \
            (1-Tr[:])**complist[name]["n"][i]
    return sigma
