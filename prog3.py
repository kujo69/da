from scipy.stats import binom

n = 10 # Number of trials
p = 0.5 # Probability of success
k_success = 2 # Number of successes

prob_2_success = binom.pmf(k_success, n, p)
print(f"Probability of 2 successes out of 10 trials: {prob_2_success}")
