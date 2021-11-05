
import pytest
import LA
import QR

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [5, 3, 1]
test_const_01 = 2
test_const_02 = 3
test_identity_mtx = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
test_matrix_01 = [test_vector_01, test_vector_02, test_vector_03]
test_comp_const_01 = 3 + 4j
test_comp_const_02 = -3
test_comp_vec_01 = [3 + 4j, 1, 4-3j]
test_GS_mtx1 = [[2,2,1],[-2,1,2],[18,0,0]]
test_GS_mtx2 = [[12,6,-4],[-51,167,24],[4,-68,-41]]

def test_add_vectors1():
    
    assert LA.add_vectors(test_vector_01, test_vector_02) == [4,3,6]
  
def test_add_vectors2():
    
    assert LA.add_vectors(test_vector_02,test_vector_03) == [8,4,3]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      
def test_scalar_vector_mult1():
    
    assert LA.scalar_vector_mult(test_const_01, test_vector_01) == [2,4,8]
    
def test_scalar_vector_mult2():
    
    assert LA.scalar_vector_mult(test_const_02, test_vector_02) == [9,3,6]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_scalar_matrix_mult1():
    
    assert LA.scalar_matrix_mult(test_const_01, test_matrix_01) == [[2,4,8],[6,2,4],[10,6,2]]
  
def test_scalar_matrix_mult2():
    
    assert LA.scalar_matrix_mult(test_const_01,test_identity_mtx) == [[2,0,0],[0,2,0],[0,0,2]]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_add_matrix1():
    assert LA.add_matrix(test_matrix_01,test_matrix_01) == [[2,4,8],[6,2,4],[10,6,2]]

def test_add_matrix2():
    assert LA.add_matrix(test_matrix_01,test_identity_mtx) == [[2,2,4],[3,2,2],[5,3,2]]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
def test_matrix_vector_mult1():
    assert LA.matrix_vector_mult(test_matrix_01,test_vector_01) == [27, 16, 12]

def test_matrix_vector_mult2():
    assert LA.matrix_vector_mult(test_matrix_01,test_vector_02) == [16,13,16]
   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
   
def test_matrix_matrix_mult1():
    assert LA.matrix_matrix_mult(test_matrix_01, test_matrix_01) == [[27,16,12],[16,13,16],[19,16,27]]
    
def test_matrix_matrix_mult2():
    assert LA.matrix_matrix_mult(test_matrix_01, test_identity_mtx) == [[1,2,4],[3,1,2],[5,3,1]]
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_absolute_value1():
    assert LA.absolute_value(test_comp_const_01) == 5
    
def test_absolute_value2():
    assert LA.absolute_value(test_comp_const_02) == 3
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_pNorm1():
    assert LA.pNorm(test_comp_vec_01) == 51**(1/2)

def test_pNorm2():
    assert LA.pNorm(test_comp_vec_01 ,3) == 251**(1/3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_infNorm1():
    assert LA.infNorm(test_vector_01) == 4
    
def test_infNorm2():
    assert LA.infNorm(test_comp_vec_01) == 5
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
def test_normSelect1():
    assert LA.normSelect(test_comp_vec_01,2) == 51**(1/2)

def test_normSelect2():
    assert LA.normSelect(test_comp_vec_01,0,True) == 5
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_innerProd1():
    assert LA.innerProd(test_vector_01, test_vector_03) == 15

def test_innerProd2():
    assert LA.innerProd(test_vector_02, test_comp_vec_01 ) == 18+6j
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_orthonormal_vectorset1():
    expected: list = [[2/3,2/3,1/3],[-2/3,1/3,2/3],[1/3,-2/3,2/3]]
    for column in range(len( QR.orthonormal_vectorset(test_GS_mtx1))):
        for element in range(len(QR.orthonormal_vectorset(test_GS_mtx1)[column])):
            x= QR.orthonormal_vectorset(test_GS_mtx1)[column][element]
            y=expected[column][element]
            assert abs(x-y) <= 0.00001

def test_orthonormal_vectorset2():
    expected: list = [[6/7,3/7,-2/7],[-69/175,158/175,6/35],[-58/175,6/175,-33/35]]
    for column in range(len( QR.orthonormal_vectorset(test_GS_mtx2))):
        for element in range(len(QR.orthonormal_vectorset(test_GS_mtx2)[column])):
            x= QR.orthonormal_vectorset(test_GS_mtx2)[column][element]
            y=expected[column][element]
            assert abs(x-y) <= 0.00001


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_stable_GramSchmidt1():
    expected: list = [[3,0,0],[0,3,0],[12,-12,6]]
    for index in range(0,2):
        for column in range(len( QR.stable_GramSchmidt(test_GS_mtx1)[1])):
            for element in range(len(QR.stable_GramSchmidt(test_GS_mtx1)[1][column])):
                assert LA.absolute_value(QR.stable_GramSchmidt(test_GS_mtx1)[1][column][element] - expected[column][element]) <= 0.001

def test_stable_GramSchmidt2():
    expected: list =  [[14,0,0],[21,175,0],[-14,-70,35]]
    for index in range(0,2):
        for column in range(len( QR.stable_GramSchmidt(test_GS_mtx2)[1])):
            for element in range(len(QR.stable_GramSchmidt(test_GS_mtx2)[1][column])):
                assert LA.absolute_value(QR.stable_GramSchmidt(test_GS_mtx2)[1][column][element] - expected[column][element]) <= 0.001

