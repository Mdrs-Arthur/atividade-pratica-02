from models import Autor, Livro


def popular_banco(session):
    if session.query(Autor).first:
        return
    """Cadastre autores e livros iniciais para testar a aplicação."""
    # TODO: crie pelo menos 3 autores.
    autor1 = Autor(nome='Machado de Assis', pais='Brasil')
    autor2 = Autor(nome='Graciliano Ramos', pais='Brasil')
    autor3 = Autor(nome='Carlos Drummond de Andrade', pais='Brasil')
    # TODO: crie pelo menos 6 livros.
    # TODO: inclua livros disponíveis e indisponíveis.
    livro1 = Livro(titulo='A Mão e a Luva', ano=1874, disponivel=True, autor = autor1)
    livro2 = Livro(titulo='Iaiá Garcia', ano=1878, disponivel=False, autor = autor1)
    livro3 = Livro(titulo='Casa Velha', ano=1885, disponivel=True, autor = autor1)
    livro4 = Livro(titulo='Esaú e Jacó', ano=1904, disponivel=False, autor = autor1)
    livro5 = Livro(titulo='Vidas Secas', ano=1938, disponivel=True, autor = autor2)
    livro6 = Livro(titulo='A Rosa do Povo', ano=1945, disponivel=False, autor = autor3)
    # TODO: use session.add ou session.add_all e finalize com session.commit().
    session.add_all([autor1, autor2, autor3, livro1, livro2, livro3, livro4, livro5, livro6])
    session.commit()
