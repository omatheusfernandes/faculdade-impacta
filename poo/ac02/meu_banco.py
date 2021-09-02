# Programação Orientada a Objetos
# AC02 ADS-EaD - Criando classes
#
# Email Impacta: matheus.fernandes@aluno.faculdadeimpacta.com.br


class Cliente:
    def __init__(self, nome, telefone, email):
        self._nome = nome
        self.telefone = telefone
        self.email = email

        pass

    #PROPERTY NOME
    @property
    def nome(self):
        return self._nome
    pass

    #PROPERTY TELEFONE
    @property
    def telefone(self):
        return self._telefone
    pass

    #SETTER TELEFONE
    @telefone.setter
    def telefone(self, novo_telefone):
        if not isinstance(novo_telefone, str):
            raise TypeError
        for dgt in novo_telefone:
            if dgt not in ("0123456789-() "):
                raise ValueError

        self._telefone = novo_telefone
    pass

    #PROPERTY EMAIL
    @property
    def email(self):
        return self._email
    pass

    @email.setter
    def email(self, novo_email):
        # * caso o email não seja uma string, levanta um TypeError;
        if not isinstance(novo_email, str):
            raise TypeError
        numArrobas = 0

        # * caso o email não seja válido levanta um ValueError;
        #   considere o email válido se ele contiver exatamente 1 símbolo de arroba '@'
        for c in novo_email:
            if c =="@":
                numArrobas += 1

        if numArrobas != 1:
            raise ValueError

        self._email = novo_email
        pass


class Conta:
    def __init__(self, clientes, numero, saldo_inicial):
        self._clientes = clientes
        self._numero = numero
        self._saldo = saldo_inicial
        self._operacoes = [("saldo inicial", saldo_inicial)]

    def sacar(self, valor):
        # * Caso o valor do saque seja maior que o saldo da conta,
        # deve retornar um ValueError, e não efetuar o saque
        if valor > self._saldo:
            raise ValueError

        self._saldo -= valor
        self._operacoes.append(("saque", valor))

    def depositar(self, valor):
        self._saldo += valor
        self._operacoes.append(("deposito", valor))

    def tirar_extrato(self):
        return self._operacoes

    @property
    def clientes(self):
        return self._clientes

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo
    pass


class Banco:
    def __init__(self, nome):
        self._nome = nome
        self._contas = list()

    def abrir_conta(self, clientes, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError

        num = len(self._contas) + 1
        self._contas.append(Conta(clientes, num, saldo_inicial))

    @property
    def nome(self):
        return self._nome

    @property
    def contas(self):
        return self._contas

    pass