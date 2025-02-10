'''
tablero.py: Dibuja el tablero del juego del gato
'''
import random

def dibuja_tablero(simbolos:dict):
    '''  Dibuja el tablero del juego de el gato '''
    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')

def ia(simbolos: dict):
    ''' Estrategia mejorada de la computadora '''
    def hay_ganador(tablero, jugador):
        ''' Verifica si el jugador puede ganar en la siguiente jugada '''
        combinaciones = [('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'),  # Filas
                         ('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9'),  # Columnas
                         ('1', '5', '9'), ('3', '5', '7')]  # Diagonales
        for a, b, c in combinaciones:
            if tablero[a] == tablero[b] == jugador and tablero[c] not in ['X', 'O']:
                return c
            if tablero[a] == tablero[c] == jugador and tablero[b] not in ['X', 'O']:
                return b
            if tablero[b] == tablero[c] == jugador and tablero[a] not in ['X', 'O']:
                return a
        return None

    # 1. Intentar ganar
    movimiento = hay_ganador(simbolos, 'O')
    if movimiento:
        simbolos[movimiento] = 'O'
        return

    # 2. Bloquear al oponente si va a ganar
    movimiento = hay_ganador(simbolos, 'X')
    if movimiento:
        simbolos[movimiento] = 'O'
        return

    # 3. Tomar el centro si está libre
    if simbolos['5'] not in ['X', 'O']:
        simbolos['5'] = 'O'
        return

    # 4. Intentar jugar en una esquina
    esquinas = ['1', '3', '7', '9']
    esquinas_libres = [e for e in esquinas if simbolos[e] not in ['X', 'O']]
    if esquinas_libres:
        simbolos[random.choice(esquinas_libres)] = 'O'
        return

    # 5. Jugar en cualquier otro espacio libre
    espacios_libres = [k for k in simbolos.keys() if simbolos[k] not in ['X', 'O']]
    if espacios_libres:
        simbolos[random.choice(espacios_libres)] = 'O'

    ''' Estrategia mejorada de la computadora '''
    def hay_ganador(tablero, jugador):
        ''' Verifica si el jugador puede ganar en la siguiente jugada '''
        combinaciones = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  # Filas
                         (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columnas
                         (1, 5, 9), (3, 5, 7)]  # Diagonales
        for a, b, c in combinaciones:
            if tablero[a] == tablero[b] == jugador and tablero[c] not in ['X', 'O']:
                return c
            if tablero[a] == tablero[c] == jugador and tablero[b] not in ['X', 'O']:
                return b
            if tablero[b] == tablero[c] == jugador and tablero[a] not in ['X', 'O']:
                return a
        return None

    # 1. Intentar ganar
    movimiento = hay_ganador(simbolos, 'O')
    if movimiento:
        simbolos[movimiento] = 'O'
        return

    # 2. Bloquear al oponente si va a ganar
    movimiento = hay_ganador(simbolos, 'X')
    if movimiento:
        simbolos[movimiento] = 'O'
        return

    # 3. Tomar el centro si está libre
    if simbolos[5] not in ['X', 'O']:
        simbolos[5] = 'O'
        return

    # 4. Intentar jugar en una esquina
    esquinas = [1, 3, 7, 9]
    esquinas_libres = [e for e in esquinas if simbolos[e] not in ['X', 'O']]
    if esquinas_libres:
        simbolos[random.choice(esquinas_libres)] = 'O'
        return

    # 5. Jugar en cualquier otro espacio libre
    espacios_libres = [k for k in simbolos.keys() if simbolos[k] not in ['X', 'O']]
    if espacios_libres:
        simbolos[random.choice(espacios_libres)] = 'O'

def usuario(simbolos:dict):
    ''' Estrategia del usuario '''
    ocupado = True
    lista_numeros = [str(i) for i in range(1,10)] #del 1 al 9
    while ocupado is True:
        x = input('Elija un número del 1 al 9: ')
        if x in lista_numeros:
            if simbolos[x] not in ['X','O']:
                simbolos[x] = 'X'
                ocupado = False
            else:
                print('Esa casilla ya está ocupada')
        else:
            print('Elija un número del 1 al 9')

def juego(simbolos:dict):
    ''' Juego del gato ''' 
    lista_combinaciones = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9'],
        ['1','5','9'],
        ['3','5','7']
    ]
    en_juego = True
    dibuja_tablero(simbolos)
    movimientos = 0
    gana = None
    while en_juego:
        usuario(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos,lista_combinaciones)
        if gana is not None:
            en_juego = False
            continue
        if movimientos >= 9:
            en_juego = False
            continue
        ia(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos,lista_combinaciones)
        if gana is not None:
            en_juego = False
            continue
        if movimientos >= 9:
            en_juego = False
            continue
    return gana

def checa_winner(simbolos:dict, combinaciones:list):
    ''' Checa si hay un ganador '''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]]
    return None

def actualiza_score(score:dict,ganador:str):
    ''' Actualiza el score '''
    X = score["X"]
    O = score["O"]
    if ganador is not None:
        print(f'El ganador es {ganador}')
        if ganador == 'X':
            X["G"] += 1
            O["P"] += 1
        elif ganador == 'O':
            O["G"] += 1
            X["P"] += 1
        else:
            X["E"] += 1
            O["E"] += 1
    else:
        print('Empate')
        X["E"] += 1
        O["E"] += 1

def despliega_tablero(score:dict):
    ''' Despliega el tablero de score '''
    print(f'''
    X | G: {score["X"]["G"]} | P: {score["X"]["P"]} | E: {score["X"]["E"]}
    O | G: {score["O"]["G"]} | P: {score["O"]["P"]} | E: {score["O"]["E"]}
    ''')

if __name__ == '__main__':
    numeros = [str(i) for i in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    g = juego(dsimbolos)
    if g is not None:
        print(f'El ganador es {g}')
    else:
        print('Empate')
    '''
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)
    
    x = random.choice(numeros)
    numeros.remove(x)
    dsimbolos[x] = 'X'
    dibuja_tablero(dsimbolos)
    o = random.choice(numeros)
    numeros.remove(o)
    dsimbolos[o] = 'O'
    dibuja_tablero(dsimbolos)
    print(numeros)
    '''