#-------------------------------------------------------------------------------
# Purpose:
#
# Author:      Olivier (Boschko) Laflamme
# Created:     13/12/2019
# Copyright:   (c) Olivier (Boschko) Laflamme 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from z3 import *

    # 9x9 matrix of integer variables
X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(9) ]
      for i in range(9) ]

s = Solver()

# A --> 0
# B --> 1
# C --> 2
# D --> 3
# E --> 4
# F --> 5
# G --> 6
# H --> 7
# I --> 8

# B9 + B8 + C1 + H4 + H4 = 23
s.add(X[1][8] + X[1][7] + X[2][0] + X[7][3] + X[7][3] == 23 )
# A5 + D7 + I5 + G8 + B3 + A5 = 19
s.add(X[0][4] + X[3][6] + X[8][4] + X[6][7] + X[1][2] + X[0][4] == 19 )
# I2 + I3 + F2 + E9 = 15
s.add(X[8][1] + X[8][2] + X[5][1] + X[4][8] == 15 )
# I7 + H8 + C2 + D9 = 26
s.add(X[8][6] + X[7][7] + X[2][1] + X[3][8] == 26 )
# I6 + A5 + I3 + B8 + C3 = 20
s.add(X[8][5] + X[0][4] + X[8][2] + X[1][7] + X[2][2] == 20 )
# I7 + D9 + B6 + A8 + A3 + C4 = 27
s.add(X[8][6] + X[3][8] + X[1][5] + X[0][7] + X[0][2] + X[2][3] == 27 )
# C7 + H9 + I7 + B2 + H8 + G3 = 31
s.add(X[2][6] + X[7][8] + X[8][6] + X[1][1] + X[7][7] + X[6][2] == 31 )
# D3 + I8 + A4 + I6 = 27
s.add(X[3][2] + X[8][7] + X[0][3] + X[8][5] == 27 )
# F5 + B8 + F8 + I7 + F1 = 33
s.add(X[5][4] + X[1][7] + X[5][7] + X[8][6] + X[5][0] == 33 )
# A2 + A8 + D7 + E4 = 21
s.add(X[0][1] + X[0][7] + X[3][6] + X[4][3] == 21 )
# C1 + I4 + C2 + I1 + A4 = 20
s.add(X[2][0] + X[8][3] + X[2][1] + X[8][0] + X[0][3] == 20 )
# F8 + C1 + F6 + D3 + B6 = 25
s.add(X[5][7] + X[2][0] + X[5][5] + X[3][2] + X[1][5] == 25 )


# each cell contains a value in {1, ..., 9}
cells_c  = [ And(1 <= X[i][j], X[i][j] <= 9)
             for i in range(9) for j in range(9) ]

# each row contains a digit at most once
rows_c   = [ Distinct(X[i]) for i in range(9) ]

# each column contains a digit at most once
cols_c   = [ Distinct([ X[i][j] for i in range(9) ])
             for j in range(9) ]

# each 3x3 square contains a digit at most once
sq_c     = [ Distinct([ X[3*i0 + i][3*j0 + j]
                        for i in range(3) for j in range(3) ])
             for i0 in range(3) for j0 in range(3) ]

sudoku_c = cells_c + rows_c + cols_c + sq_c

# sudoku instance, we use '0' for empty cells
instance = ((0,0,0, 0,0,0, 0,0,1),
            (0,1,2, 0,0,0, 0,0,0),
            (0,0,0, 0,0,0, 2,0,0),
            (0,0,0, 0,0,0, 0,0,2),
            (0,2,0, 0,0,0, 0,0,0),
            (0,0,0, 0,0,0, 0,0,0),
            (0,0,0, 0,0,0, 1,2,0),
            (1,0,0, 0,0,2, 0,0,0),
            (2,0,0, 1,0,0, 0,0,0))

instance_c = [ If(instance[i][j] == 0,
                  True,
                  X[i][j] == instance[i][j])
               for i in range(9) for j in range(9) ]


s.add(sudoku_c + instance_c)


if s.check() == sat:
    m = s.model()
    r = [ [ m.evaluate(X[i][j]) for j in range(9) ]
          for i in range(9) ]
    print_matrix(r)
else:
    print ("failed to solve")