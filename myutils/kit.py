from random import shuffle, randint

# Para atrapar errores de logica relacionados al ajedrez
class ChessLogicError(Exception):
    pass

class Board(object):

    # inicializa el tablero con valores aleatorios para las filas, todas las reinas siempre van en una columna diferente
    def __init__(self, rows=8, cols=8):
        try: 
            if rows != cols: 
                raise ChessLogicError('The number of rows must be equal to the number of columns')
            else: 
                r = [i for i in range(rows)]
                c = [i for i in range(cols)]
                shuffle(r)
                positions = list(zip(r, c))
                self.queens = positions
                self.rows = rows
                self.cols = cols
                self.__score = -1
        except ChessLogicError as e: 
            print(e)

    def __str__(self):
        result = "____"*(self.cols) + "\n"
        for row in range(self.rows): 
            for col in range(self.cols):
                if row == self.queens[col][0] and col == self.queens[col][1]:
                    result += "| Q "
                else: 
                    result += "|   "
            result += "|\n"
            result += "____"*(self.cols) + "\n"

        return result

# calcula la 'distancia' checando los pares de reinas (nCr)
    @property
    def score(self):
        self.__score = 0
        for n in range(self.rows-1):
            for m in range(n+1, self.cols, 1):
                if self.queens[n][0] == self.queens[m][0]: 
                    self.__score += 1
                elif abs(self.queens[m][0] - self.queens[n][0]) == abs(self.queens[m][1] - self.queens[n][1]):
                    self.__score += 1
        return self.__score
    
    @score.setter
    def score(self, value):
        try: 
            if value < 0: 
                raise ValueError('Score can\'t be negative')
            else: 
                self.__score == value
        except ValueError as e: 
            print(e)

# Muta el tablero moviendo una reina al azar, de fila, siempre hacia abajo y si llega al final da la vuelta
    def permutate(self): 
        randomNum = randint(0, self.cols-1)
        # move the queen 
        r, c = self.queens[randomNum]
        newr = (r + 1)%self.rows
        self.queens[randomNum] = (newr, c)
        return self
