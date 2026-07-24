def linear_lr(step, total_steps, initial_lr, final_lr=0.0, warmup_steps=0) -> float:
    """
    Linear warmup (0→initial_lr) then linear decay (initial_lr→final_lr).
    Steps are 0-based; clamp at final_lr after total_steps.
    """
    # Write code here
    if step<warmup_steps:
        if warmup_steps!=0:
            return (step*initial_lr)/warmup_steps
        else:
            raise ValueError("Divison by Zero not possible")
    elif warmup_steps<=step<=total_steps:
        if (total_steps-warmup_steps)!=0:
            return final_lr+((initial_lr-final_lr)*((total_steps-step)/(total_steps-warmup_steps)))
        elif (total_steps-warmup_steps)==0 and (total_steps-step)==0:
            return 5*(10**-5)
        elif (total_steps-warmup_steps==0):
            raise ValueError("Divison by Zero not possible")
    else:
        return final_lr