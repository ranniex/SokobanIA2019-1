import sys

tablero = []
cajaspos = []
jugadorpos = []
metas = []

def isbox(boxpos,f,c):
    rp = False
    for v in boxpos:
        if v[0] == f and v[1] == c:
            rp = True
    return rp

def leertxt(archivo):
    j = 0
    i = 0
    f = open(archivo,'r')
    linea = f.readlines()
    for l in linea:
        try:
            if l[1]==',': 
                if len(jugadorpos) == 0:
                    jugadorpos.append(int(l[0]))
                    jugadorpos.append(int(l[2]))
                else:
                    cajaspos.append( [int(l[0]),int(l[2])] )
            else:
                j = 0
                temp = []
                for a in l.replace('\n',''):
                    temp.append(a)
                    if a == 'X':
                        metas.append( [i,j] )
                    j += 1
                tablero.append(temp)
            i += 1
        
        except IndexError:
            pass
    f.close()

def valid_move(f,c,dir,cajasposNodo):

    if dir == 'U':
        if tablero[f][c] == 'W':
            return False
        elif isbox(cajasposNodo,f,c):
            if isbox(cajasposNodo,f-1,c):
                return False
            elif tablero[f-1][c] == 'W':
                return False
            elif (tablero[f-2][c] == 'W' and tablero[f-1][c-1] == 'W'):
                if not (metas.__contains__([f-1,c])):
                    return False
            elif (tablero[f-2][c] == 'W' and tablero[f-1][c+1] == 'W'):
                if not (metas.__contains__([f-1,c])):
                    return False
            
        return True
    elif dir == 'D':
        if tablero[f][c] == 'W':
            return False
        elif isbox(cajasposNodo,f,c):
            if isbox(cajasposNodo,f+1,c):
                return False
            elif tablero[f+1][c] == 'W':
                return False
            elif (tablero[f+2][c] == 'W' and tablero[f+1][c-1] == 'W'):
                if not (metas.__contains__([f+1,c])):
                    return False
            elif (tablero[f+2][c] == 'W' and tablero[f+1][c+1] == 'W'):
                if not (metas.__contains__([f+1,c])):
                    return False
            
        return True
    elif dir == 'R':
        if tablero[f][c] == 'W':
            return False
        elif isbox(cajasposNodo,f,c):
            if isbox(cajasposNodo,f,c+1):
                return False
            elif tablero[f][c+1] == 'W':
                return False
            elif (tablero[f][c+2] == 'W' and tablero[f+1][c+1] == 'W'):
                if not (metas.__contains__([f,c+1])):
                    return False
            elif (tablero[f][c+2] == 'W' and tablero[f-1][c+1] == 'W'):
                if not (metas.__contains__([f,c+1])):
                    return False
            
        return True
    elif dir == 'L':
        if tablero[f][c] == 'W':
            return False
        elif isbox(cajasposNodo,f,c):
            if isbox(cajasposNodo,f,c-1):
                return False
            elif tablero[f][c-1] == 'W':
                return False
            elif (tablero[f][c-2] == 'W' and tablero[f+1][c-1] == 'W'):
                if not (metas.__contains__([f,c-1])):
                    return False
            elif (tablero[f][c-2] == 'W' and tablero[f-1][c-1] == 'W'):
                if not (metas.__contains__([f,c-1])):
                    return False
        return True

    print("#############################")
    print("#                           #")
    print("#      Ganaste hijo de      #")
    print("#    tu puta madre estoy    #")
    print("#         MAMADISIMO        #")
    print("#                           #")
    print("#############################")

def iswin(metas,cajaspos):
    rp = True
    for m in metas:
        if not cajaspos.__contains__(m):
            rp = False
    return rp

def make_move(f,c,dir, cajasposNodo):
    if isbox(cajasposNodo,f,c):
        for box in cajasposNodo:
            if box[0] == f and box[1] == c and dir == 'U':
                cajasposNodo.remove(box)
                cajasposNodo.append([f-1,c])
            elif box[0] == f and box[1] == c and dir == 'D':
                cajasposNodo.remove(box)
                cajasposNodo.append([f+1,c])
            elif box[0] == f and box[1] == c and dir == 'L':
                cajasposNodo.remove(box)
                cajasposNodo.append([f,c-1])
            elif box[0] == f and box[1] == c and dir == 'R':
                cajasposNodo.remove(box)
                cajasposNodo.append([f,c+1])
    #print("Vector cajas y dir",cajasposNodo, dir)
    #jugadorpos[0] = f
    #jugadorpos[1] = c
    
    return cajasposNodo

def agenteAmplitud(cajaspos):
    move = 'W'
    ns = []
    nodo_inicial = [ [jugadorpos[0], jugadorpos[1]], [i[:] for i in cajaspos], '']
    cola = []
    cola.append(nodo_inicial)
    contador = 0
    for n in cola:
        jf = n[0][0]
        jc = n[0][1]
        cajaspos = [i[:] for i in n[1]]
        movimientos = n[2]
        
        if iswin(metas, cajaspos):
            print("La solucion por amplitud es: ")
            return movimientos
        
        if move == 'W':
            if valid_move(jf-1,jc,'U',cajaspos):
                make_move(jf-1,jc,'U', cajaspos)
                movimientos += 'U'
                ns = [ [jf-1,jc], [i[:] for i in cajaspos], movimientos]
                flag = True
                for validar in cola:
                    if (validar[1]== ns[1]):
                        if(validar[0]== ns[0]):
                            flag=False
                if flag:
                    cola.append(ns)
                movimientos = movimientos[:len(movimientos) - 1]
                cajaspos = [i[:] for i in n[1]]
        if move == 'W':
            if valid_move(jf+1,jc,'D',cajaspos):
                make_move(jf+1,jc,'D',cajaspos)
                movimientos += 'D'
                ns = [ [jf+1,jc], [i[:] for i in cajaspos], movimientos]
                flag = True
                for validar in cola:
                    if (validar[1]== ns[1]):
                        if(validar[0]== ns[0]):
                            flag=False
                if flag:
                    cola.append(ns)
                movimientos = movimientos[:len(movimientos) - 1]
                cajaspos = [i[:] for i in n[1]]
        if move == 'W':
            if valid_move(jf,jc-1,'L',cajaspos):
                make_move(jf,jc-1,'L',cajaspos)
                movimientos += 'L'
                ns = [ [jf,jc-1], [i[:] for i in cajaspos], movimientos]
                flag = True
                for validar in cola:
                    if (validar[1]== ns[1]):
                        if(validar[0]== ns[0]):
                            flag=False
                if flag:
                    cola.append(ns)
                movimientos = movimientos[:len(movimientos) - 1]
                cajaspos = [i[:] for i in n[1]]
        if move == 'W':
            if valid_move(jf,jc+1,'R',cajaspos):
                make_move(jf,jc+1,'R',cajaspos)
                movimientos += 'R'
                ns = [ [jf,jc+1], [i[:] for i in cajaspos], movimientos]
                flag = True
                for validar in cola:
                    if (validar[1]== ns[1]):
                        if(validar[0]== ns[0]):
                            flag=False
                if flag:
                    cola.append(ns)
                movimientos = movimientos[:len(movimientos) - 1]
                cajaspos = [i[:] for i in n[1]]
        contador += 1
    return False

def agenteProfundidad(cajaspos):
    ns = []
    nodo_inicial = [ [jugadorpos[0], jugadorpos[1]], [i[:] for i in cajaspos], '']
    cola = []
    cola.append(nodo_inicial)
    contador = 0
    explorado = []
    while(len(cola)>0):
        explorado.insert((len(explorado)),cola[0])
        n=cola.pop(0)
        jf = n[0][0]
        jc = n[0][1]
        cajaspos = [i[:] for i in n[1]]
        movimientos = n[2]

        if iswin(metas, cajaspos):
            print("La solucion por profundidad es: ")
            return movimientos

        
        if valid_move(jf,jc+1,'R',cajaspos):
            make_move(jf,jc+1,'R', cajaspos)
            movimientos += 'R'
            ns = [ [jf,jc+1], [i[:] for i in cajaspos], movimientos]
            flag = True
            for validar in cola:
                if (validar[1]== ns[1]):
                    if(validar[0]== ns[0]):
                        flag=False
            
            for validar in explorado:
                if (validar[1]== ns[1]):
                    if(validar[0]== ns[0]):
                        flag=False
            if flag:
                cola.insert(0,ns)
            movimientos = movimientos[:len(movimientos) - 1]
            cajaspos = [i[:] for i in n[1]]

        if valid_move(jf,jc-1,'L',cajaspos):
            make_move(jf,jc-1,'L', cajaspos)
            movimientos += 'L'
            ns = [ [jf,jc-1], [i[:] for i in cajaspos], movimientos]
            flag = True
            for validar in cola:
                if (validar[1]== ns[1]):
                    if(validar[0]== ns[0]):
                        flag=False
            
            for validar in explorado:
                if (validar[1]== ns[1]):
                    if(validar[0]== ns[0]):
                        flag=False
            if flag:
                cola.insert(0,ns)
            movimientos = movimientos[:len(movimientos) - 1]
            cajaspos = [i[:] for i in n[1]]

        if valid_move(jf+1,jc,'D',cajaspos):
            make_move(jf+1,jc,'D', cajaspos)
            movimientos += 'D'
            ns = [ [jf+1,jc], [i[:] for i in cajaspos], movimientos]
            flag = True
            for validar in cola:
                if (validar[1]== ns[1]):
                    if(validar[0]== ns[0]):
                        flag=False
            
            for validar in explorado:
                if (validar[1]== ns[1]):
                    if(validar[0]== ns[0]):
                        flag=False
            if flag:
                cola.insert(0,ns)
            movimientos = movimientos[:len(movimientos) - 1]
            cajaspos = [i[:] for i in n[1]]

        if valid_move(jf-1,jc,'U',cajaspos):
            make_move(jf-1,jc,'U', cajaspos)
            movimientos += 'U'
            ns = [ [jf-1,jc], [i[:] for i in cajaspos], movimientos]
            flag = True
            for validar in cola:
                if (validar[1]== ns[1]):
                    if(validar[0]== ns[0]):
                        flag=False
            
            for validar in explorado:
                if (validar[1]== ns[1]):
                    if(validar[0]== ns[0]):
                        flag=False
            if flag:
                cola.insert(0,ns)
            
            movimientos = movimientos[:len(movimientos) - 1]
            cajaspos = [i[:] for i in n[1]]

        contador += 1
    return False

def agenteIterativo(cajaspos):
    ns = []
    nodo_inicial = [ [jugadorpos[0], jugadorpos[1]], [i[:] for i in cajaspos], '']
    cola = []
    cola.append(nodo_inicial)
    contador = 0
    depth = 0
    while(len(cola)>0):
        for n in cola:
            if(len(n[2]) <= depth):
                jf = n[0][0]
                jc = n[0][1]
                cajaspos = [i[:] for i in n[1]]
                movimientos = n[2]

                if iswin(metas, cajaspos):
                    print ("La solucion por profundidad iterativa es: ")
                    return movimientos

        
                if valid_move(jf,jc+1,'R',cajaspos):
                    make_move(jf,jc+1,'R', cajaspos)
                    movimientos += 'R'
                    ns = [ [jf,jc+1], [i[:] for i in cajaspos], movimientos]
                    flag = True
                    for validar in cola:
                        if (validar[1]== ns[1]):
                            if(validar[0]== ns[0]):
                                flag=False
            
                    if flag:
                        cola.insert(0,ns)
                    movimientos = movimientos[:len(movimientos) - 1]
                    cajaspos = [i[:] for i in n[1]]

                if valid_move(jf,jc-1,'L',cajaspos):
                    make_move(jf,jc-1,'L', cajaspos)
                    movimientos += 'L'
                    ns = [ [jf,jc-1], [i[:] for i in cajaspos], movimientos]
                    flag = True
                    for validar in cola:
                        if (validar[1]== ns[1]):
                            if(validar[0]== ns[0]):
                                flag=False
            
                    if flag:
                        cola.insert(0,ns)
                    movimientos = movimientos[:len(movimientos) - 1]
                    cajaspos = [i[:] for i in n[1]]

                if valid_move(jf+1,jc,'D',cajaspos):
                    make_move(jf+1,jc,'D', cajaspos)
                    movimientos += 'D'
                    ns = [ [jf+1,jc], [i[:] for i in cajaspos], movimientos]
                    flag = True
                    for validar in cola:
                        if (validar[1]== ns[1]):
                            if(validar[0]== ns[0]):
                                flag=False
            
                    if flag:
                        cola.insert(0,ns)
                    movimientos = movimientos[:len(movimientos) - 1]
                    cajaspos = [i[:] for i in n[1]]

                if valid_move(jf-1,jc,'U',cajaspos):
                    make_move(jf-1,jc,'U', cajaspos)
                    movimientos += 'U'
                    ns = [ [jf-1,jc], [i[:] for i in cajaspos], movimientos]
                    flag = True
                    for validar in cola:
                        if (validar[1]== ns[1]):
                            if(validar[0]== ns[0]):
                                flag=False
            
                    if flag:
                        cola.insert(0,ns)
            
                    movimientos = movimientos[:len(movimientos) - 1]
                    cajaspos = [i[:] for i in n[1]]
        
        depth+=1
        contador += 1
    return False


entrada_consola = sys.argv
direccion_nivel = entrada_consola[1]
leertxt(direccion_nivel)


print(agenteAmplitud(cajaspos))
print(agenteProfundidad(cajaspos))
print(agenteIterativo(cajaspos))
