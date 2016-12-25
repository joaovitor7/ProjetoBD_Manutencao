import MySQLdb

class Banco:

    def __init__(self, host, user, passwd, db):
        con = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        self.cursor = con.cursor()

    """

    Consultas às tabelas

    """

    # Consultar clientes pelo nome
    def consultaClienteNome(self, nomeCliente):
        self.cursor.execute("SELECT * FROM Cliente WHERE nomeCli = '%s'" % str(nomeCliente))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar clientes pelo CPF
    def consultaClienteCPF(self, cpfCliente):
        self.cursor.execute("SELECT * FROM Cliente WHERE cpf = '%s'" % str(cpfCliente))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar todos os clientes cadastrados
    def consultaClientes(self):
        self.cursor.execute("SELECT * FROM Cliente")
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar computador pelo modelo
    def consultaComputadorModelo(self, modelo):
        self.cursor.execute("SELECT * FROM Computador WHERE modelo = '%s'" % str(modelo))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar computador pelo número de série
    def consultaComputadorNumSerie(self, numSerie):
        self.cursor.execute("SELECT * FROM Computador WHERE numSerie = '%s'" % str(numSerie))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar computador pelo cpf do cliente
    def consultaComputadorCliente(self, cpfCli):
        self.cursor.execute("SELECT * FROM Computador WHERE cpfCli = '%s'" % str(cpfCli))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar todos os computadores cadastrados
    def consultaComputadores(self):
        self.cursor.execute("SELECT * FROM Computador")
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar peça pelo código
    def consultaPecaCod(self, codPeca):
        self.cursor.execute("SELECT * FROM Peca WHERE codPeca = '%s'" % str(codPeca))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar todas as peças
    def consultaPecas(self):
        self.cursor.execute("SELECT * FROM Peca")
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar peças que estão sendo utilizadas em algum serviço pelo número de série do computador
    def consultaServicoPecaNumSerie(self, numSerie):
        self.cursor.execute("SELECT * FROM Peca_Upgrade_Revisao WHERE numSerieMaquina = '%s'" % str(numSerie))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar peças que estão sendo utilizadas em algum serviço pelo código da pela
    def consultaServicoPecaCod(self, codPeca):
        self.cursor.execute("SELECT * FROM Peca_Upgrade_Revisao WHERE codPecaServico = '%s'" % str(codPeca))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar peças que estão sendo utilizadas em algum serviço pela data programada
    def consultaServicoPecaData(self, dataProgramada):
        self.cursor.execute("SELECT * FROM Peca_Upgrade_Revisao WHERE dataProgramadaServico = '%s'" % str(dataProgramada))
        resultado = self.cursor.fetchall()
        print(resultado)


"""

Código para testar os métodos - Apagar para versão final

"""

bd = Banco('localhost', 'root', 'root', 'manutencao')
bd.consultaClienteNome('Pedro')
bd.consultaClienteCPF(12345678998)
bd.consultaClientes()
bd.consultaComputadorCliente(12345678998)
bd.consultaComputadores()
bd.consultaPecaCod('1A234567')
bd.consultaPecas()