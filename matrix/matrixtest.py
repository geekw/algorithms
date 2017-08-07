from matrix import Matrix

ma = Matrix(1, 2)
ma[0,0] = 1
ma[0,1] = 2
mb = Matrix(2, 1)
mb[0,0] = 1
mb[1,0] = 2
mc = ma * mb
print mc[0,0]


