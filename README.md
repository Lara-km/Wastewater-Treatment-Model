README

What each file does


File code.py is where the whole code is implemented. Brief description of the whole code including why and how Euler and bisection methods that were used, what to do if a secondary internal decay term is added. Below are inputs, dependencies and what the outputs will show.


How to run the code


Paste the code in file code.py in virtual environment. (eg. Spyder or VS-code) and click run button.


Three required numerical methods implementation


1.Euler method.


Euler method is used to numerically integrate the coupled dynamics of pollutant and chlorine concentrations ODE


Euler method is direct, efficient and accurate for smooth, first order kinetic systems when a small time interval(Δt=0.01hr) is used.
It is ideal for conceptual and educational models without adaptive step control and complex libraries needed.


2.Bisection method.


Bisection is used to find the chlorine concentration uin that reaches target pollutant level(C-target) after a series of contacting time.


Bisection is strong,non-derivative root-finding method that ensured to converge when the sign of residual function changes.
Because the nonlinearity and potential stiffness of the model, more complex methods(eg.Newton-Raphson) might fail without good inital guesses while bisection offers more reliable results at the expense of speed.


3.Newton-Raphson method for secondary decay.


Newton-Raphson method is used to find the requird time to meet the target pollutant level when a secondary internal decay was added.


It can find the time root effectively from a more complicated analytical expression with an internal decay that cannot be solved directly.
It converges faster than bisection method when the derivative is non-zero and known.


Other decisions:

1.Initial conditions


Decision: The reactor starts with the pollutant concentration 


C0=100mg/L and initial chlorine concentration 
𝑢0=uin or u0=0 depending on the test scenario.
These initial conditions show a newly dosed tank where chlorine is introduced at the start.


Starting at u0=0 allows examination of start-up transients and realistic dosing response times.


2.Time interval selections(Δt=0.01hr)


Decision: A small time interval (Δt=0.01hr, approximate 36s) is used.


Smaller time interval enhance the accuracy and prevent oscillations or negative concentration artefacts.


3.Model Validation — Exponential Regression


Decision: An exponential decay model C(t)=ae^(-bt) +c was fitted to simulation results using SciPy’s curve_fit.


A good fit shows the simulated kinetic are consistent with theoretical expectations.


This is aiming to test if pollutant decay in the simulation behaves similiar as a first-order kinetic process.


Implication:
This regression confirms that the simulated decay curve follows expected behaviour, validating the ODE structure and parameter scaling.


4.Internal Secondary Decay Term


Decision: Dintt^2 was added in a secondary analysis as an additional internal decay term,solved by Newton-Raphson method.


Newton-Raphson method effectively solved the corresponding time that meets the target pollutant concentration under this model.This was used to simulate potential slower,secondary removel mechanisms.


Implication:
This could help to estimate non-linear effect would extend or the time beyond the idealised first-order case.


5.Safety and realistic constraints


Decision: Chlorine limit=5mg/L.


This ensures the simulation is achievable and under safe dosing concentrations.


Implication:
This obeys the real-world constraint limits and gives practical operational insight rather than purely theoretical results.


6.
