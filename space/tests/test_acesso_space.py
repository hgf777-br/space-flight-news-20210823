from space.space import Space


def test_criar_acesso_space():
    sp = Space()
    assert sp is not None


def test_acessar_qtd_artigos():
    sp = Space()
    count = sp.articles_count()
    assert isinstance(count, int) and count != -1

def test_listar_artigos():
    sp = Space()
    a = sp.articles(15)
    assert len(a) == 15
