import math
def sumofsquares(num):
    if num < 1:
        return False
    else:
        sqroot = int(math.sqrt(num)//1)
        for i in range(sqroot,0,-1):
            for j in range(i,0,-1):
                if (i**2 + (j)**2) == num:
                    # print(i,j)
                    return True
    return False
# print(sumofsquares(41))
# print(sumofsquares(30))
# print(sumofsquares(17))
print(sumofsquares(-17))
# print(sumofsquares(0))
# print(sumofsquares(1))
# print(sumofsquares(2))
def wellbracketed(expr):
    open_bracket = 0
    close_bracket = 0
    for i in expr:
        if i == "(":
            open_bracket += 1
        elif i == ")":
            close_bracket += 1
    if open_bracket == close_bracket:
        return True
    else:
        return False
# print(wellbracketed("22)"))
# print(wellbracketed("(a+b)(a-b)"))
print(wellbracketed("(a(b+c)-d)((e+f)"))
def rotatelist(lst,rotation):
    if rotation>=len(lst):
        shift = rotation%len(lst)
    else:
        shift = rotation
    if shift == 0:
        return lst
    temp = lst[-shift:]+lst[:-shift]
    return temp

# print(rotatelist([1,2,3,4,5],3))
# print(rotatelist([1,2,3,4,5],1))
print(rotatelist([1,2,3,4,5],12))
