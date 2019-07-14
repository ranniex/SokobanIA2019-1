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
            tablero.append(l.replace('\n',''))
    f.close()
    for f in tablero:
        j = 0
        for c in f:
            if c == 'X':
                metas.append( [i,j] )
            j += 1
        i += 1

leertxt('nivel1.txt')

print(tablero)
print(jugadorpos)
print(cajaspos)
print(metas)