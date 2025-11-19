# Water Treatment Model
## 1.0 Introduction

This ReadMe file explains the corrsesponding python code found in the code.py file. To do this the below will outline how to run the code, the numerical methods applied and the design choices. 

The code, models the teriatry stage of a wastewater treatment plant to determine the optimal chlorine dosage to produce effleuent with low pollutant concentration. In this, mutiple ODEs show the behavoir of the system, rootfinding numerical methods are applied, and regression modelling shows trend results. Code.py can be found as a file in this repository. 

## 2.0 Numerical Methods

### 2.1 Method 1 — Coupled ODE

Function: solve_coupled_ode()

Purpose: This function is used to model how the concentrations of wastewater and chlorine change over the contact time in the tank.

### 2.2 Method 2 — Bisection Method

Function: bisection_method()

Purpose: This method uses the solution from the ODE to find the optimal chlorine dosage for the tank within the given time limit.

### 2.3 Method 3 — Newton–Raphson Method

Function: newton_raphson()

Purpose: A new ODE is created with different assumptions from the original model, and the Newton–Raphson method is used to solve for the change in the target time when the original optimised chlorine dosage is applied.

### 2.4 Method 4 — Regression Model

Function: fit_exponential_decay()

Purpose: Using data points from the ODE, the least squares regression method is used to calculate an exponential decay curve that simplifies the model and shows the overall trend.

## 3.0 How to Run the Code




## 4.0 Design and Modularity



## 5.0 Assumptions and Limitations

### 5.1 Assumptions and Principles:

1. Continously stirred tank/perfect mixing: this allows for unifrom concentration of pollutant and chlorine throughout the control volume.
   
2. Constant Flow Rate (Q): constant flow of the waste water into the tank is modelled as steady state for mass balance purposes. 

3. Fixed influent Concentration (Cin): The influent of waste water is assumed to have a uniform pollutant concentration. 

### 5.2 System Parameters: Fixed parameters seen in the correpsonding code are as follows,

1. Initial Pollutant Concentration (C0)
   
2. Influent Concentration (Cin)
   
3. Flow Rate (Q)
   
4. Natural Decay Rate (k0)
   
5. Chlorine Effectiveness (α)
    
6. Target Contact Time (ttarget)
    
7. Reactor Volume (V)
    
8. Chlorine Decay Constant (kCl)
    
9. Safety Limit for Chlorine (ulimit)

## 6.0 Repository Structure

code.py - Main script: runs the program and produces all outputs aswell as running all the definitions.

README new.md - Documentation (this file)

## 7.0 Authors

Lara Mason

James Hodgkiss

Katie Cornish 

Bondong Zhang

The Univerisity of Edinburgh

## 9.0 License

CMM 10
