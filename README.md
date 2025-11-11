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

