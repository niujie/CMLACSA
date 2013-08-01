from vec import Vec
from mat import Mat
from bitutil import noise
from GF2 import one

## Task 1 part 1
""" Create an instance of Mat representing the generator matrix G. You can use
the procedure listlist2mat in the matutil module (be sure to import first).
Since we are working over GF (2), you should use the value one from the
GF2 module to represent 1"""
from matutil import listlist2mat
G = listlist2mat([[one,0,one,one],[one,one,0,one],[0,0,0,one],[one,one,one,0],[0,0,one,0],[0,one,0,0],[one,0,0,0]])


## Task 1 part 2
# Please write your answer as a list. Use one from GF2 and 0 as the elements.
from vecutil import list2vec
#encoding_1001 = G * list2vec([one,0,0,one])
encoding_1001 = [0,0,one,one,0,0,one]


## Task 2
# Express your answer as an instance of the Mat class.
R = listlist2mat([[0,0,0,0,0,0,one],[0,0,0,0,0,one,0],[0,0,0,0,one,0,0],[0,0,one,0,0,0,0]])

## Task 3
# Create an instance of Mat representing the check matrix H.
H = listlist2mat([[0,0,0,one,one,one,one],[0,one,one,0,0,one,one],[one,0,one,0,one,0,one]])

## Task 4 part 1
def find_error(e):
    """
    Input: an error syndrome as an instance of Vec
    Output: the corresponding error vector e
    Examples:
        >>> find_error(Vec({0,1,2}, {0:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{3: one})
        >>> find_error(Vec({0,1,2}, {2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{0: one})
        >>> find_error(Vec({0,1,2}, {1:one, 2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{2: one})    
    """
    #temp = listlist2mat([[0,one,one],[0,0,0],[0,one,0],[one,0,0],[0,0,0],[0,0,0],[0,0,0]])
    #temp = Mat((set(range(7)),set(range(3))),{(0,1):one, (0,2):one, (2,1):one, (3,0):one})
    ind = -1
    for i in H.D[1]:
        if H[0,i] == e[0] and H[1,i] == e[1] and H[2,i] == e[2]:
            ind = i
            break
    if -1 == ind:
        return Vec(set(range(7)), {})
    else:
        return Vec(set(range(7)), {ind:one})


## Task 4 part 2
# Use the Vec class for your answers.
non_codeword = Vec({0,1,2,3,4,5,6}, {0: one, 1:0, 2:one, 3:one, 4:0, 5:one, 6:one})
error_vector = Vec({0, 1, 2, 3, 4, 5, 6},{6: one})
code_word = Vec({0, 1, 2, 3, 4, 5, 6},{0: one, 1: 0, 2: one, 3: one, 4: 0, 5: one, 6: 0})
original = Vec({0, 1, 2, 3},{0: 0, 1: one, 2: 0, 3: one}) # R * code_word


## Task 5
def find_error_matrix(S):
    """
    Input: a matrix S whose columns are error syndromes
    Output: a matrix whose cth column is the error corresponding to the cth column of S.
    Example:
        >>> S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
        >>> find_error_matrix(S)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 2): 0, (3, 2): one, (0, 0): 0, (4, 3): one, (3, 0): 0, (6, 0): 0, (2, 1): 0, (6, 2): 0, (2, 3): 0, (5, 1): one, (4, 2): 0, (1, 0): 0, (0, 3): 0, (4, 0): 0, (0, 1): 0, (3, 3): 0, (4, 1): 0, (6, 1): 0, (3, 1): 0, (1, 1): 0, (6, 3): 0, (2, 0): 0, (5, 0): 0, (2, 2): 0, (1, 3): 0, (5, 3): 0, (5, 2): 0, (0, 2): 0})
    """
    output = {}
    from matutil import mat2coldict
    from matutil import coldict2mat
    from vecutil import list2vec
    S_col = mat2coldict(S)
    for i in S_col.keys():
        output[i] = find_error(S_col[i])
    return coldict2mat(output)


## Task 6
s = "I'm trying to free your mind, Neo. But I can only show you the door. You’re the one that has to walk through it."
from bitutil import str2bits
from bitutil import bits2mat
P = bits2mat(str2bits(s))

## Task 7
from matutil import mat2coldict
from matutil import coldict2mat
P_col = mat2coldict(P)
C = coldict2mat({i:G*P_col[i] for i in range(len(P_col.keys()))})
bits_before = 224*4
bits_after = 224*7


## Ungraded Task
from bitutil import noise
CTILDE = C + noise(C, 0.02)

## Task 8
def correct(A):
    """
    Input: a matrix A each column of which differs from a codeword in at most one bit
    Output: a matrix whose columns are the corresponding valid codewords.
    Example:
        >>> A = Mat(({0,1,2,3,4,5,6}, {1,2,3}), {(0,3):one, (2, 1): one, (5, 2):one, (5,3):one, (0,2): one})
        >>> correct(A)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {1, 2, 3}), {(0, 1): 0, (1, 2): 0, (3, 2): 0, (1, 3): 0, (3, 3): 0, (5, 2): one, (6, 1): 0, (3, 1): 0, (2, 1): 0, (0, 2): one, (6, 3): one, (4, 2): 0, (6, 2): one, (2, 3): 0, (4, 3): 0, (2, 2): 0, (5, 1): 0, (0, 3): one, (4, 1): 0, (1, 1): 0, (5, 3): one})
    """
    error_syndrome = H * A
    error_mat = find_error_matrix(error_syndrome)
    return A + error_mat
