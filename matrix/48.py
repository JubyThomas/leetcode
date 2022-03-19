"""solution 1"""

  A.reverse()
        for row in range(len(A)):
            for col in range(row):
                A[row][col], A[col][row] = A[col][row], A[row][col]
