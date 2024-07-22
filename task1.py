# tuple_tasks.py
def likelihood():
    """
    This function creates a tuple named likelihoods containing the likelihoods that a step will fall.
    It returns the step with the smallest likelihood of falling.
    """
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)

def run_task1():
    """
    This function calls the likelihood function and stores the returned value in a local variable.
    It then displays a message in the format: "Minimum likelihood of falling: {value}%" where {value} is the value returned by the previous function call.
    """
    min_likelihood = likelihood()
    print(f"Minimum likelihood of falling: {min_likelihood}%")

# To run the task and see the output
if __name__ == "__main__":
    run_task1()
