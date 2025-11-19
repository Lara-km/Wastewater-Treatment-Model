# Water Treatment Model
## 1.0 Introduction

This ReadMe file explains the Python code in code.py. It describes how to run the code, outlines the numerical methods used, and discusses design choices.

The code models the tertiary stage of a wastewater treatment plant to determine the optimal chlorine dosage to produce effluent with low pollutant concentration. In this, multiple ODEs show the behaviour of the system, root-finding numerical methods are applied, and regression modelling shows trend results. Code.py can be found as a file in this repository.

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
 
### 3.1 Requirements
The code requires the following libraries: 
NumPy – for numerical arrays and computation 

Matplotlib – for plotting graphs 

SciPy – for curve fitting and Newton-Raphson root finding 

### 3.2 Running the program  

The entire code is executed from the Python script ‘code.py’.

Download the code.py file and open in spyder, or copy and paste from the code.py GitHub repository.

### 3.3 What the program does when run 

When the script is run, it automatically: 

Solves coupled pollutant chlorine ODEs using Euler’s Method  

Uses the bisection method to calculate the optimal uin that achieves the target effluent concentration after 12 hrs of contact time. 

Generates diagnostic plots:  

- Bisection convergence  

- Pollutant concentration over time  

- Chlorine decay profile  

 

Fits a regression model to the pollutant decay curve using non-linear least squares 

Uses Newton-Raphson root finding to calculate the time required to reach the target concentration when the addition of internal decay is factored in 

Produces 2 final plots, including: 

Regression model  

Pollutant concentrations over time, including internal decay 

 

### 3.4 Configuring Parameters 

All the system parameters (flow rate, decay constants, time step target concentration, etc.) are defined near the top of the script. These values can be adapted to model different wastewater systems.

### 3.5 Output  

The script produces: 

Printed numerical results including: 

Optimal chlorine dose 

Residual checks  
Time to target with internal decay  

A set of plots that visualise system behaviour: 

- Bisection convergence 

- Pollutant decay 

- Chlorine decay 

- Regression fit 

- Pollutant decay with internal decay 



## 4.0 Design and Modularity

Although the project is implemented into a single Python file, it is designed using a modular internal structure. The file contains multiple clearly defined functions for readability and reusability, allowing it to be easier to debug and extend.

### 4.1 Internal Structure

All numerical methods are each implemented as separate functions.

All plots have separate callable functions.

The flow of the project is defined in a function, waste_water_treatment_system(), at the bottom. This calls all the correctly ordered functions under one name.

### 4.2 Why a Modular Structure

Each function performs one clearly defined task.

Functions can be reused with different inputs without changing the rest of the code.

The numerical method functions are completely independent from plotting or printing functions.

Separation improves readability and makes the code easier to maintain or modify.

## 5.0 Assumptions and Limitations

### 5.1 Assumptions and Principles:

1. Continuously stirred tank/perfect mixing: this allows for uniform concentration of pollutant and chlorine throughout the control volume.
   
2. Constant Flow Rate (Q): constant flow of the wastewater into the tank is modelled as steady state for mass balance purposes. 

3. Fixed influent concentration (Cin): The influent of wastewater is assumed to have a uniform pollutant concentration. 

### 5.2 System Parameters: 
Fixed parameters seen in the corresponding code are as follows:

1. Initial Pollutant Concentration (C0)
   
2. Influent Concentration (Cin)
   
3. Flow Rate (Q)
   
4. Natural Decay Rate (k0)
   
5. Chlorine Effectiveness (α)
    
6. Target Contact Time (ttarget)
    
7. Reactor Volume (V)
    
8. Chlorine Decay Constant (kCl)
    
9. Safety Limit for Chlorine (ulimit)


### 5.3 Code Limitations

1. Code is very responsive to system parameters.
   
2. To effectively use this code for different areas within the UK or elsewhere, the system parameters must be changed according to specific data available.

3.  The Newton-Raphson method increases the sensitivity of the code due to the decay terms present.

   
## 6.0 Repository Structure

code.py - Main script: runs the program and produces all outputs as well as running all the definitions.

README.md - Documentation (this file)

## 7.0 Authors

Lara Mason

James Hodgkiss

Katie Cornish 

Bondong Zhang

The University of Edinburgh

## 9.0 Licence

CMM 10
