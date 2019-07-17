tablero = []
cajaspos = []
jugadorpos = []
metas = []

def leertxt(archivo):
    j = 0
    i = 0
    f = open(archivo,'r')
    linea = f.readlines()
    for l in linea:
        if l[1]==',':
            if len(jugadorpos) == 0:
                jugadorpos.append(l[0])
                jugadorpos.append(l[2])
            else:
                cajaspos.append( [l[0],l[2]] )
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
    """for f in tablero:
        j = 0
        for c in f:
            if c == 'X':
                metas.append( [i,j] )
            j += 1
        i += 1"""

"""def leertxt(archivo):
    j = 0
    i = 0
    f = open(archivo,'r')
    linea = f.readlines()
    for l in linea:
        if l[1]==',': #Corregir el problema de que la ultima linea sea = '\n'
            if len(jugadorpos) == 0:
                jugadorpos.append(l[0])
                jugadorpos.append(l[2])
            else:
                cajaspos.append( [l[0],l[2]] )
        else:
            tablero.append(l)#l.replace('\n',''))
    f.close()
    for f in tablero:
        j = 0
        for c in f:
            if c == 'X':
                metas.append( [i,j] )
            j += 1
        i += 1"""

leertxt('nivel1.txt')

def valid_move(f,c,dir):
    if dir == 'U':
        if tablero[f][c] == 'W'
