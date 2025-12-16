import numpy as np
import matplotlib.pyplot as plt

def solve_heat_equation(L=1.0, T=0.1, nx=50, nt=1000, alpha=1.0):
    dx = L / (nx - 1)
    dt = T / nt
    x = np.linspace(0, L, nx)
    u = np.sin(np.pi * x)

    r = alpha * dt / dx**2

    for _ in range(nt):
        u[1:-1] = u[1:-1] + r * (u[2:] - 2*u[1:-1] + u[:-2])
        u[0] = 0
        u[-1] = 0

    return x, u

if __name__ == "__main__":
    x, u = solve_heat_equation()
    plt.plot(x, u)
    plt.xlabel("x")
    plt.ylabel("Temperature")
    plt.title("1D Heat Equation Solution")
    plt.show()
