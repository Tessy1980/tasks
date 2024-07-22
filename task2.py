def likelihood_min_max():
    """
    This function creates a tuple named likelihoods containing the likelihoods that a step will fall.
    It returns a tuple with the minimum and maximum values.
    """
    likelihoods = (50, 38, 27, 99, 4)
    return (min(likelihoods), max(likelihoods))

def run_task2():
    """
    This function calls the likelihood_min_max function and stores the returned value in a local variable.
    It then displays the minimum and maximum values in the format:
    "Minimum likelihood of falling: {min_value}%" and "Maximum likelihood of falling: {max_value}%".
    """
    min_max_likelihood = likelihood_min_max()
    print(f"Minimum likelihood of falling: {min_max_likelihood[0]}%")
    print(f"Maximum likelihood of falling: {min_max_likelihood[1]}%")

# To run the tasks and see the output
if __name__ == "__main__":
    run_task2()
