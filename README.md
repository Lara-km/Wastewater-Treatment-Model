# Secondary Analysis including internal decay: Newton-Raphson

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
    
    """
    Plot pollutant concentration with internal decay.
    """

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

