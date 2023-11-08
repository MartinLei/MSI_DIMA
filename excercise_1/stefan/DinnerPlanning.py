from constraint import Problem

# Create a CSP problem instance
problem = Problem()

# Define the variables and domains
problem.addVariable("Mr_Dupont", [0, 1])
problem.addVariable("Mrs_Dupont", [0, 1])
problem.addVariable("Emma", [0, 1])
problem.addVariable("Georg", [0, 1])
problem.addVariable("Ivana", [0, 1])

# Define the constraints

# If Mr. Dupont then Mrs Duopont
def constraint1(Mr_Dupont, Mrs_Dupont):
    return not Mr_Dupont or Mrs_Dupont

# Ivana or Georg
def constraint2(Ivana, Georg):
    return Ivana or Georg

# Mrs. Dupont xor Emma
def constraint3(Mrs_Dupont, Emma):
    return Mrs_Dupont != Emma

def constraint4(Emma, Georg):
    return (Emma and Georg) or (not Emma and not Georg)

def constraint5(Ivana, Georg, Mr_Dupont):
    return not Ivana or (Georg and Mr_Dupont)

problem.addConstraint(constraint1, ["Mr_Dupont", "Mrs_Dupont"])
problem.addConstraint(constraint2, ["Ivana", "Georg"])
problem.addConstraint(constraint3, ["Mrs_Dupont", "Emma"])
problem.addConstraint(constraint4, ["Emma", "Georg"])
problem.addConstraint(constraint5, ["Ivana", "Georg", "Mr_Dupont"])

# Solve the CSP
solutions = problem.getSolutions()

# Print the valid solutions
for solution in solutions:
    print("Solution:")
    for variable, value in solution.items():
        print(f"{variable}: {'Coming' if value == 1 else 'Not Coming'}")
    print()
