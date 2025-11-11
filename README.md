# Wastewater-Treatment-Model
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
