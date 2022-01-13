class Square_Matrix:

    def __init__(self,size): # square-matrix object constructed to apply LU decomposition and perform other tasks
        if  not isinstance(size,int) and size <= 0:
            raise ValueError("Please input integer greater than 0")

        self.matrix_size=size
        self.matrix_values= self.create_square_matrix()
        self.U= None
        self.L= None

    def __len__(self): # return length of the matrix
        return self.matrix_size

    def __repr__(self): # prints original matrix
        s=""
        for i in self.matrix_values:
            if isinstance(i,list):
                s += "[ "+ " ".join([str(x) for x in i])+ " ]\n"
        return s
    def U_matrix(self): # prints U matrix
        print("U=")
        for i in self.U:
            print(i)

    def L_matrix(self): # printse L matrix
        print("L=")
        for i in self.L:
            print(i)

    def create_square_matrix(self): # creates the square matrix from the user inputted values
        lst=[]
        for i in range(1,len(self)+1):
            temp_lst = []
            for j in range(1,len(self)+1):
                while True:
                    try:
                        x = float(input("Enter Value for " + "row " +str(i)+", column "+str(j)+"."))
                        temp_lst.append(x)
                        break
                    except ValueError:
                        print("Please enter a proper value.")
            lst.append(temp_lst)
        return lst

    def LU_Decomposition(self): # performs LU decomposition on inputted matrix to produce L and U matrices.
        self.L=[]
        self.U=self.matrix_values
        for i in range(len(self)):
            self.L.append([0 if x!=i else 1 for x in range(len(self))])

        row_start=1
        for i in range(len(self)):
            Divisor = self.matrix_values[i][i]
            for j in range(row_start, len(self)):
                Dividend= self.matrix_values[j][i]
                Quotient=Dividend/Divisor
                self.L[j][i]=Quotient
                for z in range(len(self)):
                    self.U[j][z]= self.U[j][z]-Quotient*self.U[i][z]
            row_start+=1

    def solve_for_b_with_LU_Decomposition(self): # Solves for x inn Ax=b with LU decomposition
        if self.U is None and self.L is None:
            self.LU_Decomposition()
        U= self.U
        L= self.L
        b = [] # User inputs components of b they are solving for in Ax=b
        for i in range(1, len(self) + 1):
            while True:
                try:
                    x = float(input("Enter component " + str(i) + " for b:"))
                    b.append(x)
                    break
                except ValueError:
                    print("Please enter a proper value.")
        y=[b[0]] # Solves y in Ly=b
        for row in range(1,len(self)):
            y_comp=b[row]
            for j in range(row):
                y_comp=y_comp-y[j]*L[row][j]
            y.append(y_comp)

        x=[0 for i in range(len(self)-1)] # Solves x in Ux=Y
        x.append(y[len(self)-1]/U[len(self)-1][len(self)-1])
        for row in range(len(self)-2,-1,-1):
            y_comp=y[row]
            for col in range(len(self)-1,row,-1):
                y_comp=y_comp-x[col]*U[row][col]
                z=col
            x[row]= y_comp/U[row][z-1]
        return "x= "+ str(x)

    def determinant(self): # computes determinant value of square matrix using the LU factorization
        if self.U is None and self.L is None:
            self.LU_Decomposition()

        det_U=1
        for i in range(len(self)):
            det_U *= self.U[i][i]
        return det_U



z = Square_Matrix(3) # creating 3x3 matrix. Assumes that user inputs valid values that allow LU decomposition.
print(z) # printing out the matrix
z.LU_Decomposition() # performing LU decomposition on the matrix to generate L and U matrices
print(z.L_matrix()) # printing the L matrix
print(z.U_matrix()) # printing the U matrix

print(z.solve_for_b_with_LU_Decomposition()) # solves for "b" value using lu decomposition
print(z.determinant()) # solves the determinant of the matrix.
