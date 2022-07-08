from class_livro import Livro

livro1 = Livro('Curso de Python em 6h', 'Alcimar Costar', 'Udemy', '878-98-9988-988-9', 2018)
livro2 = Livro('Python para web', 'Alcimar Costar', 'Udemy', '999-98-9988-988-9', 2018)
livro3 = Livro('Inteligência Artificial', 'Alcimar Costar', 'Udemy', '888-98-9988-988-9', 2018)

livros = [livro1, livro2, livro3]

for l in livros:
    print(l)