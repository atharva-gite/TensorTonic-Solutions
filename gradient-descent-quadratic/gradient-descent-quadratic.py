def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x_min=(-b)/(2*a)
    f_der_x0=2*a*x0+b
    sign=-1 #true represents a +ve, move left
    x=x0+(sign*lr*f_der_x0)
    for _ in range(steps):
        f_der=2*a*x+b
        # if f_der<0:
        #     sign=-1
        # else:
        #     sign=1
        x=x+(sign*lr*f_der)
        
    return x