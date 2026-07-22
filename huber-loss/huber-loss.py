import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    answer_arr=[]
    for i in range(len(y_true)):
        e=y_true[i]-y_pred[i]
        if abs(e)<=delta:
            answer_arr.append(e**2/2)
        else:
            answer_arr.append(delta*(abs(e)-(delta/2)))
    answer_arr=np.array(answer_arr)
    return np.mean(answer_arr)