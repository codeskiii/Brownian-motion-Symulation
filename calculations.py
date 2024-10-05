import math
import random
#from scipy.constants import Boltzmann

def get_n() -> float:
    return random.random()

def movement_equation(d_t: float , diffusion_coeficient: float, n: float) -> float:
    return math.sqrt(2 * diffusion_coeficient * d_t) * n

def velocity_langevin_equation(v: float, d_t: float, y: float, T: float, n: float, m: float) -> None:

    #v(t) = v to prędkość cząsteczki w chwili t,
    #γ = y to współczynnik oporu (tłumienia),
    #kB​ to stała Boltzmanna,
    #T to temperatura (w kelwinach),
    #m to masa cząsteczki,
    #Δt = d_t to mały krok czasowy,
    #N(0,1) = n to losowa wartość z rozkładu normalnego (środek 0, odchylenie standardowe 1).

    term_1 = v
    term_2 = -1 * y * d_t * v
    term_3 = math.sqrt(2 * 1.38e-23 * T * y * d_t )/m * n

    return term_1 + term_2 + term_3

def stokes_einstein_d() -> None:
    pass