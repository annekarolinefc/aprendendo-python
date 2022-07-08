class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo #atributo privado
        self.autor = autor #atributo primado

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo=titulo

livro1 = Livro('Curso de Python', 'Alcimar Costa')
#print(livro1._Livro__titulo)
print(livro1.titulo)
livro1.titulo = 'Novo autor'
print(livro1.titulo)
