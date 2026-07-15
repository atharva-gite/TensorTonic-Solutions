def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    hits=0
    for i in range(len(recommendations)):
        arr1=recommendations[i]
        arr2=ground_truth[i]
        arr1=arr1[:k]
        for ele in arr2:
            if ele in arr1:
                hits+=1
            
    return hits/len(recommendations)