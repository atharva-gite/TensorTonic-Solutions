import numpy as np

def l1_norm(matrix,axis):
    rows,cols=np.shape(matrix)
    sum_arr=[]
    if axis==1:
        for i in range(rows):
            sum_row=0
            for j in range(cols):
                sum_row+=abs(matrix[i][j])
            sum_arr.append(sum_row)
        for i in range(rows):
            if sum_arr[i]!=0:
                matrix[i,:]=matrix[i,:]/sum_arr[i]
    elif axis==0:
        for i in range(cols):
            sum_cols=0
            for j in range(rows):
                sum_cols+=abs(matrix[j][i])
            sum_arr.append(sum_cols)
        for i in range(cols):
            if sum_arr[i]!=0:
                matrix[:,i]=matrix[:,i]/sum_arr[i]
    else:
        sum=0
        for i in range(rows):
            for j in range(cols):
                sum+=abs(matrix[i][j])
        for i in range(rows):
            for j in range(cols):
                if sum!=0:
                    matrix[i][j]=matrix[i][j]/sum
    return matrix

def l2_norm(matrix,axis):
    rows,cols=np.shape(matrix)
    sum_arr=[]
    if axis==1:
        for i in range(rows):
            sum_row=0
            for j in range(cols):
                sum_row+=matrix[i][j]**2
            sum_arr.append(sum_row)
        print(sum_arr)   
        for i in range(rows):
            if sum_arr[i]!=0:
                matrix[i,:]=matrix[i,:]/np.sqrt(sum_arr[i])
                print(matrix)
    elif axis==0:
        for i in range(cols):
            sum_col=0
            for j in range(rows):
                sum_col+=matrix[j][i]**2
            sum_arr.append(sum_col)
        print(sum_arr)
        for i in range(cols):
            if sum_arr[i]!=0:
                matrix[:,i]=matrix[:,i]/np.sqrt(sum_arr[i])
    else:
        sum_mat=0
        for i in range(rows):
            for j in range(cols):
                sum_mat+=matrix[i][j]**2
        for i in range(rows):
            for j in range(cols):
                if sum!=0:
                    matrix[i][j]=matrix[i][j]/np.sqrt(sum_mat)
    return matrix

def max_norm(matrix,axis):
    rows,cols=np.shape(matrix)
    max_arr=[]
    if axis==1:
        for i in range(rows):
            max_row=0
            for j in range(cols):
                if max_row<abs(matrix[i][j]):
                    max_row=abs(matrix[i][j])
            max_arr.append(max_row)
        for i in range(rows):
            if max_arr[i]!=0:
                matrix[i,:]=matrix[i,:]/max_arr[i]
    elif axis==0:
        for i in range(cols):
            max_col=0
            for j in range(rows):
                if max_col<abs(matrix[j][i]):
                    max_col=abs(matrix[j][i])
            max_arr.append(max_col)
        print(max_arr)
        for i in range(cols):
            if max_arr[i]!=0:
                matrix[:,i]=matrix[:,i]/max_arr[i]
    else:
        max_mat=0
        for i in range(rows):
            for j in range(cols):
                if max_mat<abs(matrix[i][j]):
                    max_mat=abs(matrix[i][j])
        for i in range(rows):
            for j in range(cols):
                if max_mat!=0:
                    matrix[i][j]=matrix[i][j]/max_mat
    return matrix


def matrix_normalization(matrix, axis=None, norm_type='l2'):
    matrix=np.array(matrix,dtype='float')
    axes=[0,1,None]
    types=['l1','l2','max']
    if np.ndim(matrix)!=2 or axis not in axes or norm_type not in types:            
        return None
    if norm_type=="l2":
        return l2_norm(matrix,axis)
    elif norm_type=="l1":
        return l1_norm(matrix,axis)
    elif norm_type=="max":
        return max_norm(matrix,axis)