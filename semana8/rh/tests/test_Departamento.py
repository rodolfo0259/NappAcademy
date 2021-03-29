from rh.classes.Departamento import Departamento
from datetime import date, timedelta


class TestDepartamento:
    def test_class_declared(self):
        objeto = Departamento('Departamento XYZ')
        assert isinstance(objeto, Departamento)

    def test_instanciar(self):
        objeto = Departamento('Departamento XYZ')
        assert objeto.nome == 'Departamento XYZ'
        assert objeto.responsavel is None

    def test_str_repr(self):
        objeto = Departamento('Departamento XYZ')
        assert str(objeto) == 'Departamento XYZ'
        assert repr(objeto) == 'Departamento = Departamento XYZ'

    def test_setters(self):
        objeto = Departamento('Curadoria')
        assert objeto.nome == 'Curadoria'
        objeto.nome = 'ETL'
        assert objeto.nome == 'ETL'

    def test_properties(self):
        objeto = Departamento('Departamento XYZ')
        assert objeto.nome == 'Departamento XYZ'

    def test_responsavel(self):
        departamento = Departamento('Departamento XYZ')
        assert departamento.responsavel is None
        departamento = Departamento('Departamento XYZ','José da Silva', 1, 1, 1990)
        #departamento.informar_responsavel('José da Silva', 1, 1, 1990)
        assert departamento.responsavel == 'José da Silva'

    def test_responsavel_substituido(self):
        departamento = Departamento('Departamento XYZ')
        assert departamento.responsavel is None
        departamento = Departamento('Departamento XYZ','José da Silva', 1, 1, 1990)
        assert departamento.responsavel == 'José da Silva'
        departamento = Departamento('Departamento XYZ','João Oliveira', 1, 1, 1990)
        assert departamento.responsavel == 'João Oliveira'

    def test_add_colaborador(self):
        departamento = Departamento('Departamento XYZ')
        departamento = Departamento('Departamento XYZ','José da Silva', 1, 1, 1990)
        departamento.add_colaborador('João Oliveira', 18, 3, 1992)
        departamento.add_colaborador('Pedro Mendonça', 18, 4, 1993)
        assert len(departamento.colaboradores) == 3

    def test_verificar_aniversariantes(self):
        dt1 = date.today() - timedelta(days=4)
        hoje = date.today()
        retorno = [('João Oliveira', f'1992-{hoje.month:02d}-{hoje.day}', 'Departamento XYZ'),
                ('Luis Fernando', f'2000-{hoje.month:02d}-{hoje.day}', 'Departamento XYZ')]

        depto = Departamento('Departamento XYZ','José da Silva', dt1.day, dt1.month, 1990)
        depto.add_colaborador('João Oliveira', hoje.day, hoje.month, 1992)
        depto.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
        depto.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
        depto.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1085)
        aniversariantes = depto.verificar_aniversariantes()
        assert aniversariantes == retorno
        assert len(aniversariantes) == 2
        assert len(aniversariantes[0]) == 3
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == list
