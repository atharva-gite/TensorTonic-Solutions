import math
def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    sum_p=0
    for i in range(len(actual_tokens)):
        p=prob_distributions[i][actual_tokens[i]]
        sum_p+=math.log(p)
    
        
    return math.exp((-1/len(actual_tokens)*sum_p))
    