def matmult(matA, matB):
    matA_rows = len(matA)
    matA_columns = len(matA[0])
    matB_rows = len(matB)
    matB_columns = len(matB[0])
    assert (matA_columns == matB_rows), "Matrix Multiplication not possible"
    matC_rows = matA_rows
    matC_columns = matB_columns
    matC = []
    for i in range(matC_rows):
        matC.append([0]*matC_columns)
    for r in range(matC_rows):
        for c in range(matC_columns):
            for k in range(matB_rows):
                matC[r][c] += matA[r][k] * matB[k][c]
    return matC


def ascending(lst):
    if len(lst) < 2:
        return True
    small = lst[0]
    for i in range(1, len(lst)):
        if small > lst[i]:
            return False
        small = lst[i]
    return True


'''
def alternating(lst):
    if lst == [] or len(lst) < 3:
        return True
    odd_lst = []
    even_lst = []
    even_flag = True
    odd_flag = True
    for element in range(0, len(lst), 2):
        even_lst.append(lst[element])
    for element in range(1, len(lst), 2):
        odd_lst.append(lst[element])
    if len(even_lst) < 2 or len(odd_lst) < 2:
        return True
    # computing even list
    dec = even_lst[1]
    inc = even_lst[0]
    if dec >= inc:
        even_flag = False
    else:
        for i in range(0, (len(even_lst)),2):
            if even_lst[i] != inc:
                even_flag = False
                break
        for i in range(1, (len(even_lst)),2):
            if even_lst[i] != dec:
                even_flag = False
                break
    # computing odd list
    dec = odd_lst[1]
    inc = odd_lst[0]
    if dec >= inc:
        odd_flag = False
    else:
        for i in range(0, (len(odd_lst)),2):
            if odd_lst[i] != inc:
                odd_flag = False
                break
        for i in range(1, (len(odd_lst)),2):
            if odd_lst[i] != dec:
                odd_flag = False
                break
    if odd_flag or even_flag:
        return True
    else:
        return False
'''


def alternating(lst):
    if len(lst) < 3:
        return True
    prev = lst[0]
    i_d = False
    d_i = True
    if prev > lst[1]:
        i_d = True
    else:
        d_i = True
    if i_d:
        inc = False
        for i in range(1, len(lst)):
            current = lst[i]
            if inc:
                if not (current > prev):
                    return False
                inc = False
                prev = current
            else:
                if not (current < prev):
                    return False
                inc = True
                prev = current
        return True
    else:
        inc = True
        for i in range(1,len(lst)):
            current = lst[i]
            if inc:
                if not (current > prev):
                    return False
                inc = False
                prev = current
            else:
                if not (current < prev):
                    return False
                inc = True
                prev = current
        return True        
            

print(alternating([]))
print(alternating([1,3,2,3,1,5]))
print(alternating([3,2,3,1,5]))
print(alternating([3,2,2,1,5]))
print(alternating([3,2,1,3,5]))
