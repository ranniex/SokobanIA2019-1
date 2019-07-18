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

def iswin():
    rp = True
    for m in metas:
        if not cajaspos.__contains__(m):
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
        if iswin():
            winmessage()
            break

leertxt('nivel1.txt')
drawtablero(configconsola(tablero))
juegoconsola(True)

print(cajaspos)
print(metas)
print(jugadorpos)