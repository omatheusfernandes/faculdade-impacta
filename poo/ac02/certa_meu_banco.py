class Cliente:
    def __init__(self, nome, telefone, email):
        self._nome = nome
        self.telefone = telefone
        self.email = email

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        if not isinstance(novo_telefone, str):
            raise TypeError
        for d in novo_telefone:
            if d not in ("0123456789-() "):
                raise ValueError
        self._telefone = novo_telefone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        if not isinstance(novo_email, str):
            raise TypeError

        numero_arrobas = 0

        for c in novo_email:
            if c == "@":
                numero_arrobas += 1

        if numero_arrobas != 1:
            raise ValueError

        self._email = novo_email

class Conta:
    def __init__(self, clientes, numero, saldo_inicial):
        self._clientes = clientes
        self._numero = numero
        self._saldo = saldo_inicial
        self._operacoes = [("saldo inicial", saldo_inicial)]

    def sacar(self, valor):
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

class Banco:
    def __init__(self, nome):
        self._nome = nome
        self._contas = list()

    def abrir_conta(self, clientes, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError

        numero = len(self._contas) + 1
        self._contas.append(Conta(clientes, numero, saldo_inicial))

    @property
    def nome(self):
        return self._nome

    @property
    def contas(self):
        return self._contas