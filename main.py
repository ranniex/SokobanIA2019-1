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

def drawtablero(tabtemp):
    for fila in tabtemp:
        print(fila,'\n')

def leertxt(archivo):
    j = 0
    i = 0
    f = open(archivo,'r')
    linea = f.readlines()
    for l in linea:
        if l[1]==',': #Corregir el problema de que la ultima linea sea = '\n'
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
    f.close()

def valid_move(f,c,dir):
    if dir == 'U':
        if tablero[f][c] == 'W':
            return False
        elif isbox(cajaspos,f,c):
            if isbox(cajaspos,f-1,c):
                return False
            elif tablero[f-1][c] == 'W':
                return False
        return True
    elif dir == 'D':
        if tablero[f][c] == 'W':
            return False
        elif isbox(cajaspos,f,c):
            if isbox(cajaspos,f+1,c):
                return False
            elif tablero[f+1][c] == 'W':
                return False
        return True
    elif dir == 'R':
        if tablero[f][c] == 'W':
            return False
        elif isbox(cajaspos,f,c):
            if isbox(cajaspos,f,c+1):
                return False
            elif tablero[f][c+1] == 'W':
                return False
        return True
    elif dir == 'L':
        if tablero[f][c] == 'W':
            return False
        elif isbox(cajaspos,f,c):
            if isbox(cajaspos,f,c-1):
                return False
            elif tablero[f][c-1] == 'W':
                return False
        return True

def winmessage():
    print("#############################")
    print("#                           #")
    print("#      Ganaste hijo de      #")
    print("#    tu puta madre estoy    #")
    print("#         MAMADISIMO        #")
    print("#                           #")
    print("#############################")

def iswin(metasW, cajasposW):
    rp = True
    for m in metasW:
        if not cajasposW.__contains__(m):
            rp = False
    return rp

def make_move(f,c,dir):
    if isbox(cajaspos,f,c):
        for box in cajaspos:
            if box[0] == f and box[1] == c and dir == 'U':
                cajaspos.remove(box)
                cajaspos.append([f-1,c])
            elif box[0] == f and box[1] == c and dir == 'D':
                cajaspos.remove(box)
                cajaspos.append([f+1,c])
            elif box[0] == f and box[1] == c and dir == 'L':
                cajaspos.remove(box)
                cajaspos.append([f,c-1])
            elif box[0] == f and box[1] == c and dir == 'R':
                cajaspos.remove(box)
                cajaspos.append([f,c+1])
    jugadorpos[0] = f
    jugadorpos[1] = c

def configconsola(tab):
    tableroConsole = [i[:] for i in tab]
    tableroConsole[jugadorpos[0]][jugadorpos[1]] = '‡'
    for box in cajaspos:
        tableroConsole[box[0]][box[1]] = '▥' #'C' □ ▥

    return tableroConsole

def juegoconsola(a):
    while(a):
        jf = jugadorpos[0]
        jc = jugadorpos[1]
        move = input("move: ")
        if move == 'w':
            if valid_move(jf-1,jc,'U'):
                make_move(jf-1,jc,'U')
        if move == 's':
            if valid_move(jf+1,jc,'D'):
                make_move(jf+1,jc,'D')
        if move == 'a':
            if valid_move(jf,jc-1,'L'):
                make_move(jf,jc-1,'L')
        if move == 'd':
            if valid_move(jf,jc+1,'R'):
                make_move(jf,jc+1,'R')
        print("#################################")
        drawtablero(configconsola(tablero))
        if iswin(metas,cajaspos):
            winmessage()
            break

def agente():
    nodo = [ [jugadorpos[0],jugadorpos[1]], [i[:] for i in cajaspos], ['']]
    cola = []
    cola.append(nodo)
    contador = 0
    for n in cola:
        jf = n[0][0]
        jc = n[0][1]

        cajaspos[0]=n[1][0].copy()
        
        controlMov = n[2][len(n[2])-1]
        if (controlMov == 'U'):
            make_move(jf,jc,'U')
        if(controlMov == 'D'):
            make_move(jf,jc,'D')
        if(controlMov == 'L'):
            make_move(jf,jc,'L')
        if(controlMov == 'R'):
            make_move(jf,jc,'R')
        
        if iswin(metas,cajaspos):
            #print("cajaspos es: ", cajaspos, "\nY el nodo tiene las cajas en: ", n[1])
            print("el contador llego a: ", contador)
            return n[2]

        if(contador == 10):
            for algo in cola:
                print (algo,"\n")
            break

        if valid_move(jf-1,jc,'U'):
            make_move(jf-1,jc,'U')
            ns = [i[:] for i in n]
            ns[0]= [jf-1,jc]
            ns[1]= cajaspos.copy()
            ns[2].insert(len(n[2]),'U')
            cola.append(ns)
        if valid_move(jf+1,jc,'D'):
            make_move(jf+1,jc,'D')
            ns = [i[:] for i in n]
            ns[0]= [jf+1,jc]
            ns[1]= cajaspos.copy()
            ns[2].insert(len(n[2]),'D')
            cola.append(ns)
        if valid_move(jf,jc-1,'L'):
            make_move(jf,jc-1,'L')
            ns = [i[:] for i in n]
            ns[0]= [jf,jc-1]
            ns[1]= cajaspos.copy()
            ns[2].insert(len(n[2]),'L')
            cola.append(ns)
        if valid_move(jf,jc+1,'R'):
            make_move(jf,jc+1,'R')
            ns = [i[:] for i in n]
            ns[0]= [jf,jc+1]
            ns[1]= cajaspos.copy()
            ns[2].insert(len(n[2]),'R')
            cola.append(ns)
        contador+=1
    return "404"

leertxt('nivel1.txt')
#drawtablero(configconsola(tablero))
#juegoconsola(True)
print(agente())
#print(cajaspos)
#print(metas)
#print(jugadorpos)
