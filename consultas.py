from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    # TODO: use select(Livro) e acesse livro.autor.nome.
    livro = select(Livro)
    for l in session.scalars(livro):
        print(f'{l.titulo} - autor:{l.autor.nome}, status: {l.disponivel}')


def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    # TODO: filtre Livro.disponivel igual a True.
    livro = select(Livro)
    for l in session.scalars(livro):
        if l.disponivel == True:
            print(f'{l.titulo}')


def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    # TODO: use contains ou like no título.
    livro = select(Livro).where(Livro.titulo.like(f'%{trecho}%'))
    for l in session.scalars(livro):
        print(f'{l.titulo}')
    


def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    # TODO: busque o autor e navegue por autor.livros.
    autor = select(Autor).where(Autor.nome.like(f'%{nome_autor}%'))
    for l in session.scalars(autor):
        print(f'{l.livros}')
