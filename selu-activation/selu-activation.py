import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    # Write code here
    answer_arr=[]
    for num in x:
        if num>0:
            answer_arr.append(lam*num)
        else:
            answer_arr.append(lam*alpha*(np.exp(num)-1))
    return answer_arr
