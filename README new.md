"1.0 Introduction"

This ReadMe file explains the corrsesponding python code found in the code.py file. To do this the below will outline how to run the code, the numerical methods applied and the design choices. 
The code, models the teriatry stage of a wastewater treatment plant to determine the optimal chlorine dosage to produce effleuent with low pollutant concentration. In this, mutiple ODEs show the behavoir of the system, rootfinding numerical methods are applied, and regression modelling shows trend results. Code.py can be found as a file in this repository. 

2.0 Numerical Methods 

3. Numerical Methods Implemented

3.1 Method 1 — Coupled ODE

Function: solve_coupled_ode()
Purpose: This function is used to model how the concentrations of wastewater and chlorine change over the contact time in the tank.

3.2 Method 2 — Bisection Method

Function: bisection_method()
Purpose: This method uses the solution from the ODE to find the optimal chlorine dosage for the tank within the given time limit.

3.3 Method 3 — Newton–Raphson Method

Function: newton_raphson()
Purpose: A new ODE is created with different assumptions from the original model, and the Newton–Raphson method is used to solve for the change in the target time when the original optimised chlorine dosage is applied.

3.4 Method 4 — Regression Model

Function: fit_exponential_decay()
Purpose: Using data points from the ODE, the least squares regression method is used to calculate an exponential decay curve that simplifies the model and shows the overall trend.

3.0 How to Run the Code 




4.0 Design and Modularity 



5.0 Assumptions and Limitations




6.0 Authors 

Lara Mason

James Hodgkiss

Katie Cornish 

Bondong Zhang

The Univerisity of Edinburgh

7.0 License

CMM 10
