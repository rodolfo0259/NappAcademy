from rh.classes.Colaborador import Colaborador


class Departamento:
    def __init__(self, nome_setor, responsavel=None, dia=None, mes=None, ano=None):
        self._nome_setor = nome_setor
        self._colaboradores = []
        if responsavel != None:
            self._responsavel = Colaborador(responsavel, dia, mes, ano)
            self._colaboradores.append(Colaborador(responsavel, dia, mes, ano))
        else:
            self._responsavel = None

    @property
    def nome(self):
        return self._nome_setor

    @nome.setter
    def nome(self, value):
        self._nome_setor = value

    @property
    def responsavel(self):
        if self._responsavel is None:
            return None
        return str(self._responsavel)

    @property
    def colaboradores(self):
        return self._colaboradores

    def add_colaborador(self, nome, dia, mes, ano):
        self._colaboradores.append(Colaborador(nome, dia, mes, ano))

    def verificar_aniversariantes(self):
        lista = []
        for colaborador in self.colaboradores:
            if colaborador.aniversario_hoje():
                lista.append((colaborador.nome, colaborador.aniversario, self._nome_setor))
        return lista

    def __str__(self):
        return self._nome_setor

    def __repr__(self):
        return 'Departamento = ' + self._nome_setor
