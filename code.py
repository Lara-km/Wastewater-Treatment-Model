"""
Pollutant-Chlorine optimisation and analyis

Authors:
   Katie Cornish
   Lara Mason
   James Hodgkiss
   Bodong
   
Description:
Simulates pollutant decay in a reactor with chlorine dosing.
Uses Euler’s method for ODEs and the bisection method to find 
optimal chlorine input.

After finding the optimal chlorine dosage, calculates the
time required to reach the target pollutant concentration
if a secondary internal decay term is added.
"""
"""
Inputs:
    - None (all parameters are set within the script)
    
Dependencies:
    - numpy
    - scipy
    - matplotlib
    
Outputs:
    - Optimal chlorine dosage
    - Residual verification report
    - Plots:
        - Bisection convergence
        - Pollutant and chlorine concentration over time
        - Regression fit for pollutant decay
        - Pollutant decay with internal secondary decay
"""

#imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#defining parameters
C0 = 100          # Initial pollutant concentration (mg/L)
Cin = 20          # Influent concentration (mg/L)
Q = 12_500_000    # Flow rate (L/hr)
k0 = 0.05         # Natural decay rate (hr^-1)
alpha = 0.05      # Chlorine effectiveness (hr⁻¹ per mg/L)
t_target = 12     # Target contact time (hr)
C_target = 10     # Target pollutant concentration (mg/L)
V = Q * t_target  # Reactor volume (L)
k_chl = 0.14      # Chlorine decay constant (hr^-1)
u_limit = 5       # Safety limit for chlorine mg/L
dt = 0.01         # Time step for Eulers

# Coupled ODE Solver (Euler Method)

def solve_coupled_ode(u_in, t_end, dt = 0.01):
    
    """
    Simulate the coupled dynamics of pollutant and chlorine concentrations 
    in a continuous-flow reactor using Euler's method.

    The pollutant concentration decreases due to natural decay and chlorine 
    disinfection, while chlorine concentration decreases due to its own decay 
    and the reactor outflow. The system is integrated forward in time using 
    a simple Euler step.

    Args:
        u_in (float): Initial chlorine dosage [mg/L].
        t_end (float): Total simulation time [hr].
        dt (float, optional): Integration time step [hr]. Default is 0.01.

    Returns:
        tuple of np.ndarray:
            t_vals (array): Time points from 0 to t_end [hr].
            C_vals (array): Pollutant concentrations over time [mg/L].
            u_vals (array): Chlorine concentrations over time [mg/L].

    Notes:
        - Concentrations are clamped to non-negative values to avoid 
          numerical artifacts.
        - This solver uses a fixed time step; smaller dt increases accuracy.
    """

    C, u, t= C0, u_in, 0.0
    t_vals, C_vals, u_vals= [t], [C], [u]
 
    while t < t_end:
        # Effective decay rate
        k_eff = k0 + alpha * u
        # Pollutant ODE: influent - decay
        dCdt = (Q / V) * (Cin - C) - k_eff * C
        # Chlorine ODE: input - decay
        dudt = (Q / V) * (u_in - u) - k_chl * u
        C += dCdt * dt
        u += dudt * dt
        t += dt

         # Clamp to avoid tiny negative concentrations
        C = max(C, 0.0)
        u = max(u, 0.0)
       
        t_vals.append(t)
        C_vals.append(C)
        u_vals.append(u)
 
    return np.array(t_vals), np.array(C_vals), np.array(u_vals)

# Define a pollutant residual function

 def pollutant_residual(u_in):
    
    """
    Compute residual between final pollutant and target.
    
    Args:
        u_in (float): Chlorine input
    
    Returns:
        residual (float): C_final - C_target
    """
    
    t_vals, C_vals, u_vals = solve_coupled_ode(u_in, t_target)
    return C_vals[-1] - C_target


# Root Finding (Bisection Method)
 
def bisection_method(f, a, b, tol=1e-6, max_iter=50):
    
    """
    Find root using bisection method.
    
    Args:
        f (callable): Function to find root for
        a, b (float): Search interval
        tol (float): Tolerance
        max_iter (int): Maximum iterations
    
    Returns:
        root (float), mids (list): Root estimate and midpoints per iteration
    """
    
    mids = []
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs for bisection.")
        
    for _ in range(max_iter):
        c = (a + b) / 2
        f_c = f(c)
        mids.append(c)
        
        if abs(f_c) < tol:
            return c, mids
        
        elif f(c) * f(a) < 0:
            b = c
            
        else:           
            a = c
            
    return (a + b) / 2 , mids # Approximate root



# Plots / visualisation

def plot_bisection_convergence(mids, u_opt):
  
   """
   Plot bisection iteration convergence.
   """
    plt.figure(figsize=(8, 5))
    plt.plot(mids, 'o-', label='Midpoint per iteration')
    plt.axhline(y=u_opt, color='r', linestyle='--', label=f'Final solution = {u_opt:.2f}')
    plt.xlabel('Iteration')
    plt.ylabel('Midpoint value')
    plt.title('Bisection Method Convergence')
    plt.legend()
    plt.grid(True)
    plt.show()
 
def plot_concentrations (t_vals, C_vals, u_vals, u_opt):
   
    """
    Plot pollutant and chlorine concentrations over time.
    """ 
    #pollutant
    plt.figure(figsize=(8,5))
    plt.plot(t_vals, C_vals, label='Pollutant concentration C(t)')
    plt.axhline(C_target, color='r', linestyle='--', label='C_target')
    plt.axvline(t_target, color='g', linestyle='--', label='t_target')
    plt.xlabel('Time (hr)')
    plt.xticks(np.arange(0, 25, 2))
    plt.ylabel('Pollutant concentration [mg/L]')
    plt.title(f'Pollutant Decay (u_in={u_opt:.2f} mg/L)')
    plt.legend() 
    plt.grid(True) 
    plt.show()
    
    #Chlorine
    plt.figure(figsize=(8,5))
    plt.plot(t_vals, u_vals, color='orange', label='Chlorine concentration u(t)')
    plt.axhline(u_limit, color='r', linestyle='--', label='u_limit')
    plt.xlabel('Time (hr)')
    plt.xticks(np.arange(0, 25, 2))
    plt.ylabel('Chlorine concentration [mg/L]')
    plt.title('Chlorine Dynamics')
    plt.legend() 
    plt.grid(True) 
    plt.show()
# Secondary Analysis including internal decay: Newton-Raphson

# regression

# Define regression model (exponential decay)
def fit_exponential_decay(t_vals, C_vals):
    
    """
    Fit exponential decay model to pollutant data.
    
    Parameters:
        t_vals (array): Time points [hr]
        C_vals (array): Pollutant concentrations [mg/L]
    
    skip: Plot every nth point to reduce clutter (default=50)
    """
   
    def exp_decay_prediction(t, a, b, c):
        return a * np.exp(-b * t) + c

    # Fit to simulated data (e.g. first 12 hrs)
    params, cov = curve_fit(exp_decay_prediction, t_vals, C_vals, p0=(100, 0.1, 0))
    a, b, c = params
    print(f"Fitted parameters: a={a:.3f}, b={b:.4f}, c={c:.3f}")

    skip = 50 # plot every 50th point
    t_plot = t_vals[::skip]
    C_plot = C_vals[::skip]
    C_fit_plot = exp_decay_prediction(t_plot, a, b, c)

    plt.figure(figsize=(8,5))
    plt.plot(t_plot, C_plot, 'ro', label='Simulated data' , markersize=4)
    plt.plot(t_plot, C_fit_plot, linewidth=2, label=f'Fitted curve (b={b:.3f})')
    plt.xlabel('Time (hr)')
    plt.ylabel('Pollutant concentration [mg/L]')
    plt.legend()
    plt.grid(True)
    plt.title('Regression Fit for Pollutant Decay')
    plt.tight_layout()
    plt.show()

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    
    """
    Solve f(x)=0 using Newton-Raphson method.
   
    Args:
       f: Function
       df: Derivative
       x0: Initial guess
       tol: Tolerance
       max_iter: Maximum iterations
    Returns:
       x: Root estimate
       i+1: Iterations used
    """
    
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivative is zero. No convergence possible.")
        
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tol:
            print(f"Converged after {i+1} iterations.")
            return x_new, i+1
        
        x = x_new

    print("Warning: Newton–Raphson did not converge.")
    return x, max_iter

def time_to_target_with_internal_decay(u_in, D_int=0.01, V_new_factor=12):
    
    """
    Compute time to reach target with secondary internal decay.
    """
    
    V_new = Q * V_new_factor     
    u_new  = u_in

    r = Q / V_new
    k_eff = k0 + alpha * u_new
    A = r * Cin / (r + k_eff)
    B = C0 - A
    k = r + k_eff

    def f(t_new):
        return A + B * np.exp(-k * t_new) - D_int * t_new**2 - C_target
    
    def df(t_new):
        return -B * k * np.exp(-k * t_new) - 2 * D_int * t_new
    
    t0 = 10
        
    t_new, iters = newton_raphson(f, df, t0)
    print(f"Time to reach C_target with internal decay (Newton–Raphson): {t_new:.4f} hr")

    # Plot concentration curve
    t_vals = np.linspace(0, 30, 500)
    C_vals = A + B * np.exp(-k * t_vals) - D_int * t_vals**2
    C_vals = np.maximum(C_vals, 0)
    
    return t_new, t_vals, C_vals

def plot_internal_decay(t_new, t_vals, C_vals):
    
    #Plot pollutant concentration with internal decay
    plt.figure(figsize=(10,6))
    plt.plot(t_vals, C_vals, label='C(t) with internal 2nd rate Decay')
    plt.axhline(C_target, color='r', linestyle='--', label='C_target')
    plt.axvline(t_new, color='g', linestyle='--', label=f't ≈ {t_new:.2f} hr')
    plt.xlabel('Time (hr)')
    plt.xticks(np.arange(0, 30, 2))
    plt.ylabel('Pollutant Concentration (mg/L)')
    plt.yticks(np.arange(0, 100, 10))
    plt.title('Pollutant Decay with Internal Growth')
    plt.legend()
    plt.grid(True)
    plt.show()

# Wastewater-Treatment-Model
def waste_water_treatment_system():
    
    # Step 1: Find optimal chlorine input using bisection
    u_in_opt, mids = bisection_method(pollutant_residual, 0, 20)
    print(f"Optimal chlorine dosage for target {t_target} hr: {u_in_opt:.4f} mg/L")

    # Step 2: Verify residuals around root
    final_residual = pollutant_residual(u_in_opt)
    C_minus = pollutant_residual(u_in_opt - 0.1)
    C_plus  = pollutant_residual(u_in_opt + 0.1)
    print(f"Verification: residual at u_in_opt = {final_residual:.3e}")
    print(f"Residual just below root: {C_minus:.3e}, above root: {C_plus:.3e}")
    
    # Step3: Verify a sign change occurs
    if C_minus * C_plus > 0:
        print("Warning: sign change not detected — check initial bounds or tolerance.")

    # Solve for full 24 hr
    t_vals, C_vals, u_vals = solve_coupled_ode(u_in_opt, 24)

    # Plots
    plot_bisection_convergence(mids, u_in_opt)
    plot_concentrations(t_vals, C_vals, u_vals, u_in_opt)
    fit_exponential_decay(t_vals, C_vals)

    # Secondary internal decay analysis
    t_new, t_vals_internal, C_vals_internal = time_to_target_with_internal_decay(u_in_opt)
    plot_internal_decay(t_new, t_vals_internal, C_vals_internal)


if __name__ == "__main__":
    
    waste_water_treatment_system()

