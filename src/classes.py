class Filmes: #objeto
    def __init__(self, titulo, autor, ano, genero): #modelo de atributo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero #atributos dentro do construtor

    __assistido = 'Pendente' #atributos fora do construtor
    favorito = False

#Setters
    def assistir(self):
        self.__assistido = 'Assistindo'
    
    def favoritar(self):
        # self.favorito = True
        if self.favorito :
            self.favorito = False
        else:
            self.favorito = True
    
    #metodo GeTter
    def mostrar(self):
        return[
        self.titulo,
        self.autor,
        self.ano,
        self.genero,
        self.__assistido,
        self.favorito]

    def jsonificar(self):
        return{
            'titulo': self.titulo,
            'autor': self.autor,
            'ano': self.ano,
            'genero': self.genero,
            'assistido': self.__assistido.upper(),
            'favorito': self.favorito
        }
    
    @property #Getter como propriedade que seve como atributo do objeto
    def assistido(self):
        return self.__assistido

    @staticmethod
    def cadastrar(titulo, autor, ano, genero):
        return Filmes(titulo, autor, ano, genero)