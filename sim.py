import random
import matplotlib.pyplot as plt
#genera tablero aleatorio
#p: probabilidad de roca hueca, n cantidad de filas de la roca
#m: cantidad de columnas de la roca
def rand_board(n,m,p):
    board = []
    for i in range (0,n):
        board.append([])
        for j in range (0,m):
            rand = random.random()
            if rand<p:
                board[i].append(True)
                #la roca es hueca
            else:
                board[i].append(False)
                #la roca es solida
    # for i in range(0,n):
    #     for j in range (0,m):
    #         print (board[i][j],end="\t")
    #     print()
    # print("------------------------")
    return board

#retorna las posiciones donde hay hueco en una fila
def ret_row_true(l,n):
    ans = []
    for i in range (0,len(l)):
        if l[n][i]:
            ans.append([n,i])
    return ans

# retorna verdadero si hay un camino a traves del tablero desde un punto inicial 
# se van añadiendo todos los nodos a los que se puede accerder directamente desde 
# el nodo inicial a una lista, despues se toman los nodos que se añadieron y se hace 
# lo mismo hasta que se llega hasta lu ultima fila (hay camino) o ya no se puede avanzar mas 
def find_path(board,visited,inicial,path):
    j=0
    rows= len (board)
    columns= len(board[0])
    while True:
        try:
            row = path[j][0]
            column = path[j][1]
            if path[j][0]==rows-1 and board[row][column]:
                return True
            if row-1>=0:
                if board[row-1] [column] and not (str([row-1,column]) in visited):
                    path.append([row-1,column])
                    visited.add(str([row-1,column]))
            if row+1<rows:
                if board[row+1] [column] and not (str([row+1,column]) in visited):
                    if row+1 == rows-1: return True
                    path.append([row+1,column])
                    visited.add(str([row+1,column]))
            if column-1>=0:
                if board[row] [column-1] and not (str([row,column-1]) in visited):
                    path.append([row,column-1])
                    visited.add(str([row,column-1]))
            if column+1<columns:
                if board[row] [column+1] and not (str([row,column+1]) in visited):
                    path.append([row,column+1])
                    visited.add(str([row,column+1]))
            j+=1 
        except: 
            break
    return False

#retorna true si ha un camino posible o false si no hay caminos
def simulate(board):
    inicial = ret_row_true(board,0)
    final = ret_row_true(board,len(board)-1)
    if len(inicial)<=0 or len(final)<=0:
        return False
    for i in range(0,len(inicial)):
        path = []
        visited = set()
        path.append(inicial[i])
        visited.add(str(inicial[i]))
        if find_path(board,visited,inicial,path):
            return True
    return False

param = input("ingrese 1 para definir los parametros o otro valor para ejecturar la simulacion por defecto ")

if param == ("1"):
    increment=float(input("incremento de p (delta p) "))
    iterations=int(input("cantidad de simulaciones para cada p "))
    rows = int(input("cantidad de filas "))
    columns=int(input("cantidad de columnas "))
    print("ejecutando simulacion")
else:
    increment = 0.001
    iterations = 200
    rows = 5
    columns = 5
    print ("ejecutando simulacion por defecto")
ans =[]
ans.append([])
ans.append([])
k=0

for i in range (0, int(1/increment)+1):
    aux=0
    for j in range(0, iterations):        
        #simular tablero de rocas
        board = rand_board(rows,columns,k)
        if (simulate(board)):
            #si hay un camino sumar uno 
            aux+=1
    #p = numero de tableros con camino / numero de tableros simulados
    p=aux/iterations
    ans[0].append(k)
    ans[1].append(p)
    k += increment 
plt.plot(ans[0],ans[1])
plt.ylabel("theta(p)")
plt.xlabel("p")
plt.show()