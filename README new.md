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
 
### 3.1 Requirments
The code requires the following libraries: 
NumPy – for numerical arrays and computation 

Matplotlib – for plotting graphs 

SciPy – for curve fitting and Newton Raphson root finding 

### 3.2 Running the program  

The entire code is executed from the python script ‘code.py’ 

Copy the code from GitHub and it can be run inside an IDE such as spyder 

### 3.3 what the program does when run 

When the script is run it automatically: 

Solves coupled pollutant chlorine ODE’s using Euler’s Method  

Uses the bisection method to calculate the optimal uin that acheives the target effluent concentration after 12hrs of contact time. 

Generates diagnostic plots:  

- Bisection convergence  

- Pollutant concentration over time  

- Chlorine decay profile  

 

Fits a regression model to the pollutant decay curve using non-linear least squares 

Uses Newton raphson root finding to calculate the time required to reach the target concentration when the addition of internal decay is factored in 

Produces 2 final plots including: 

Regression model  

Pollutant concentrations over time including internal decay 

 

### 3.4 Configuring Parameters 

All the system parameters (flow rate, decay constants, time step target concentration, etc) are defined near the top of the script. These values can be adapted to model different wastewater systems.

### 3.5 Output  

The script produces: 

Printed numerical results including: 

Optimal chlorine dose 

Residual checks  
Time to target with internal decay  

A set of plots that visualise system behaviour: 

-Bisection convergence 

-Pollutant decay 

-Chlorine decay 

-Regression fit 

-Pollutant decay with internal decay 



## 4.0 Design and Modularity



## 5.0 Assumptions and Limitations

### 5.1 Assumptions and Principles:

1. Continously stirred tank/perfect mixing: this allows for unifrom concentration of pollutant and chlorine throughout the control volume.
   
2. Constant Flow Rate (Q): constant flow of the waste water into the tank is modelled as steady state for mass balance purposes. 

3. Fixed influent Concentration (Cin): The influent of waste water is assumed to have a uniform pollutant concentration. 

### 5.2 System Parameters: 
Fixed parameters seen in the correpsonding code are as follows,

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

1. Code is very responsive to system parameters
   
2. To effectivly use this code for different Areas within the UK or elsewhere, the system parameters must be changed according to specific data available

3.  The Newton-Raphson Method increases the sensitivity of the code due to the decay terms present

   
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
