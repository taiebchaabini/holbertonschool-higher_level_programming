#!/usr/bin/python3
def square_matrix_map(matrix=[]):
   new_matrix = list(map(lambda x:(x[0]*x[0],x[1]*x[1],x[2]*x[2]),matrix))
   return (new_matrix)
