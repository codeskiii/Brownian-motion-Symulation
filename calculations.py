import math
import random

# Constants
BOLTZMANN_CONSTANT = 1.38e-23  # Boltzmann constant in J/K

def get_random_normal() -> float:
    """
    Generate a random value from a standard normal distribution (mean=0, std=1).
    """
    return random.gauss(0, 1)

def movement_equation(d_t: float, diffusion_coefficient: float) -> float:
    """
    Calculate the displacement based on the diffusion equation.

    :param d_t: Time increment (in seconds)
    :param diffusion_coefficient: Diffusion coefficient (in m^2/s)
    :return: Displacement (in meters)
    """
    n = get_random_normal()  # Standard normal random variable
    return math.sqrt(2 * diffusion_coefficient * d_t) * n

def velocity_langevin_equation(v: float, d_t: float, y: float, T: float, m: float) -> float:
    """
    Calculate the new velocity of a particle using the Langevin equation.

    :param v: Current velocity (in m/s)
    :param d_t: Time increment (in seconds)
    :param y: Friction coefficient (in kg/s)
    :param T: Temperature (in Kelvin)
    :param m: Mass of the particle (in kg)
    :return: Updated velocity (in m/s)
    """
    n = get_random_normal()  # Get a random value from a normal distribution
    term_1 = v  # Current velocity
    term_2 = -y * v * d_t / m  # Damping term
    term_3 = math.sqrt(2 * BOLTZMANN_CONSTANT * T / m * y * d_t) * n  # Random force term

    return term_1 + term_2 + term_3

def stokes_einstein_d(T: float, mu: float) -> float:
    """
    Calculate the diffusion coefficient using the Stokes-Einstein equation.

    :param T: Temperature (in Kelvin)
    :param mu: Dynamic viscosity of the solvent (in Pa.s)
    :return: Diffusion coefficient (in m^2/s)
    """
    return BOLTZMANN_CONSTANT * T / (6 * math.pi * mu)