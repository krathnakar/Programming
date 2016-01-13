# -*- coding: utf-8 -*-
from numpy import *  # analysis:ignore
from sys import maxint
#TODO: Replace all TODO comments (yes, this one too!)
#TODO: Add doctests, post them on the forum


#STOCK_PRICES  = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
#STOCK_PRICE_CHANGES =[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
#STOCK_PRICE_CHANGES =[-3,-25,-2,-16,-23,-7,-5,-22]
STOCK_PRICE_CHANGES =[1,2,3,4,5]


#Implement pseudocode from the book
def find_maximum_subarray_brute(A, low=0, high=-1):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Implement the brute force method from chapter 4
    time complexity = O(n^2)
    >>> A =[-3,-25,-2,-16,-23,-7,-5,-22]
    >>> find_maximum_subarray_brute(A, low=0, high=-1)
    (2, 2)
    >>> A =[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    >>> find_maximum_subarray_brute(A, low=0, high=-1)
    (7, 10)
    """
    #TODO
    length = len(A)
    res = -maxint#assumed negative imported from sys
    ival=0
    jval=0
    for i in range(length):
        summ=0
        for j in range(i,length):     
            summ += A[j]
            
            if summ > res:
                jval = j
                ival = i
                res = summ
          
    return (ival,jval)





#Implement pseudocode from the book
def find_maximum_crossing_subarray(A, low, mid,  high):
    """
    Find the maximum subarray that crosses mid
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    
    """
    #TODO
    left_sum = -maxint#assumed negative imported from sys
    summ = 0
    for i in range(mid,low-1,-1):
        summ +=A[i]
        if summ>left_sum:
            left_sum=summ
            max_left = i
    
    right_sum = -maxint#assumed negative imported from sys
    summ = 0
    for j in range(mid+1,high+1):
        summ +=A[j]
        
        if summ>right_sum:
            right_sum=summ
            max_right = j
    return (max_left,max_right,left_sum+right_sum)


def find_maximum_subarray_recursive(A, low=0, high=-1):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Recursive method from chapter 4
    >>> A =[-3,-25,-2,-16,-23,-7,-5,-22]
    >>> find_maximum_subarray_recursive(A, low=0, high=len(A)-1)
    (2, 2)
    >>> A =[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    >>> find_maximum_subarray_recursive(A, low=0, high=len(A)-1)
    (7, 10)
    """
    #TODO
    (leftans,rightans,totval)=result(A,low,high)
    return(leftans,rightans)
    
#recursive task below return (i,j) tuple along with value    
def result(A,low,high):
    if high == low:
        #print low
        return (low,high,A[low])
    else:
        mid = (low+high)/2
        #print mid
        (left_low,left_high,left_sum) = result(A,low,mid)
        #print left_low
        (right_low,right_high,right_sum)= result(A,mid+1,high)
        (cross_low,cross_high,cross_sum)=find_maximum_crossing_subarray(A,low,mid,high)
        if left_sum>=right_sum and left_sum>=cross_sum:
            #print "left"
            return (left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            #print "right"
            return (right_low,right_high,right_sum)
        else:
            #print "cross"
            return (cross_low,cross_high,cross_sum)

def find_maximum_subarray_iterative(A, low=0, high=-1):
    """
    Return a tuple (i,j) where A[i:j] is the maximum subarray.
    Do problem 4.1-5 from the book.
    >>> A =[-3,-25,-2,-16,-23,-7,-5,-22]
    >>> find_maximum_subarray_iterative(A, low=0, high=-1)
    (2, 2)
    >>> A =[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    >>> find_maximum_subarray_iterative(A, low=0, high=-1)
    (7, 10)
    """
    #TODO
    res = 0
    start = 0
    end = 0
    summ =A[0]
    temp = 0
    for i in range(len(A)):
        
        res += A[i]
        if res >summ:
            summ = res
            start=temp
            end =i
            
        if res < 0 :
            temp = i+1
            res = 0
       
    return start,end


def square_matrix_multiply(A, B):
    """
    Return the product AB of matrix multiplication.
    >>> A= [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 1], [1, 2, 3, 1]]
    >>> B= [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 1], [1, 2, 3, 1]]
    >>> square_matrix_multiply(A, B)
    [[34, 44, 54, 25], [73, 95, 117, 64], [103, 128, 153, 94], [31, 38, 45, 22]]
    >>> A= [[1,0],[0,1]]
    >>> B= [[1,0],[0,1]]
    >>> square_matrix_multiply(A, B)
    [[1, 0], [0, 1]]
    """
    A = asarray(A)
    B = asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape
    C = [[0 for each in range(len(A))] for each in range(len(B))]
    
    #TODO
    for i in range(len(A)):
        for j in range(len(B)):
            #C[i][j] = 0
            for k in range(len(B)):
                C[i][j]+=A[i][k]*B[k][j]
    return C


def split(mat):
    a = len(mat)/2
    a11 = [[0 for j in range(0, a)] for i in range(0, a)]
    a12 = [[0 for j in range(0, a)] for i in range(0, a)]
    a21 = [[0 for j in range(0, a)] for i in range(0, a)]
    a22 = [[0 for j in range(0, a)] for i in range(0, a)]
    
    for i in xrange(0, a):
            for j in xrange(0, a):
                a11[i][j] = mat[i][j]
                a12[i][j] = mat[i][j+a]
                a21[i][j] = mat[i+a][j]
                a22[i][j] = mat[i+a][j+a]
    return a11,a12,a21,a22
    
def add(a, b): # add 2 matrices
    d = []
    for i in range(len(a)):
        c = []
        for j in range(len(a[0])):
            c.append(a[i][j] + b[i][j])
        d.append(c)
    return d

def sub(a, b): # subtract 2 matrices
    d = []
    for i in range(len(a)):
        c = []
        for j in range(len(a[0])):
            c.append(a[i][j] - b[i][j])
        d.append(c)
    return d


def square_matrix_multiply_strassens(A, B):
    """
    Return the product AB of matrix multiplication.
    Assume len(A) is a power of 2
    >>> A= [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 1], [1, 2, 3, 1]]
    >>> B= [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 1], [1, 2, 3, 1]]
    >>> square_matrix_multiply_strassens(A, B)
    [[34, 44, 54, 25], [73, 95, 117, 64], [103, 128, 153, 94], [31, 38, 45, 22]]
    >>> A= [[1,0],[0,1]]
    >>> B= [[1,0],[0,1]]
    >>> square_matrix_multiply_strassens(A, B)
    [[1, 0], [0, 1]]
    """
    A = asarray(A)
    B = asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape
    assert (len(A) & (len(A) -1)) == 0, "A is not a power of 2"
    #TODO
    #pass
    n=len(A)
    if n == 1:
        d = [[0]]
        d[0][0] = A[0][0] * B[0][0]
        return d
    else:
        a11, a12, a21, a22 = split(A)
        b11, b12, b21, b22 = split(B)
        
    p2=square_matrix_multiply_strassens(add(a11,a12),b22)
    p3=square_matrix_multiply_strassens(add(a21,a22),b11)
    p4=square_matrix_multiply_strassens(a22,sub(b21,b11))
    p5=square_matrix_multiply_strassens(add(a11,a22),add(b11,b22))
    p6=square_matrix_multiply_strassens(sub(a12,a22),add(b21,b22))
    p7=square_matrix_multiply_strassens(sub(a11,a21),add(b11,b12))
    p1=square_matrix_multiply_strassens(a11,sub(b12,b22))
    
    c11 = sub(add(add(p5,p4),p6),p2)
    c12 = add(p1,p2)
    c21 = add(p3,p4)
    c22 = sub(add(p1,p5),add(p3,p7))

    c = [[0 for a in range(len(c11)*2)] for b in range(len(c11)*2)]

    for i in range(len(c11)):
            for j in range(len(c11)):
                c[i][j] = c11[i][j]
                c[i][j+len(c11)] = c12[i][j]
                c[i+len(c11)][j] = c21[i][j]
                c[i+len(c11)][j+len(c11)] = c22[i][j]

    return c
    

def test():
    #TODO: Test all of the methods and print results.
    #pass
    A=[[1,2,3,4],[4,5,6,7],[7,8,9,1],[1,2,3,1]]
    B=[[1,2,3,4],[4,5,6,7],[7,8,9,1],[1,2,3,1]]
    print "STOCK_PRICE_CHANGES=",STOCK_PRICE_CHANGES
    print "Brute=",find_maximum_subarray_brute(STOCK_PRICE_CHANGES, low=0, high=-1)
    print "Iterative=",find_maximum_subarray_iterative(STOCK_PRICE_CHANGES, low=0, high=-1)
    print "Recursive",find_maximum_subarray_recursive(STOCK_PRICE_CHANGES, low=0, high=len(STOCK_PRICE_CHANGES)-1)
    print "A=",A
    print "B=",B
    print "Matrix Multiplication=",square_matrix_multiply(A, B)
    print "Strassen=",square_matrix_multiply_strassens(A,B)

if __name__ == '__main__':
    test()
    import doctest
    doctest.testmod()
    
