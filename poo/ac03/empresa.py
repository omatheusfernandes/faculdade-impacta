# Programação Orientada a Objetos
# AC03 - Herança e polimorfismo
#
# Email Impacta: matheus.fernandes@aluno.faculdadeimpacta.com.br

import re

class Pessoa:
    def __init__(self, nome, idade):

        if not isinstance(nome, str):
            raise TypeError("O atributo nome deve ser string")

        if nome == "":
            raise ValueError("O atributo nome não pode ser vazio")

        if not isinstance(idade, int):
            raise TypeError("O atributo idade deve ser um inteiro")

        if idade < 0:
            raise ValueError("O atributo idade não pode ser negativo")

        self.__nome = nome
        self.__idade = idade
    
    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    def aniversario(self):
        self.__idade += 1

class Funcionario(Pessoa):
    def __init__(self, nome, idade, email, carga_horaria):
        super().__init__(nome, idade)
        self.email = email
        self.carga_horaria = carga_horaria

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        if not isinstance(novo_email, str):
            raise TypeError("Email deve ser string.")

        if re.match("^[a-zA-Z0-9.]*@[a-zA-Z0-9.]*$", novo_email) == None:
            raise ValueError("Email deve conter apenas letras, números, pontos e apenas um arroba.")

        self.__email = novo_email


    @property
    def carga_horaria(self):
        raise NotImplementedError

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        raise NotImplementedError

    def calcula_salario(self):
        raise NotImplementedError

    def aumenta_salario(self):
        self._salarioHora *= 1.05


class Programador(Funcionario):
    def __init__(self, nome, idade, email, carga_horaria):
        super().__init__(nome, idade, email, carga_horaria)
        self._salario_hora = 35
        self.carga_horaria = carga_horaria

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria < 20 or nova_carga_horaria > 40:
            raise ValueError("A carga horária de programador deve ser maior ou igual a 20 e menor ou igual a 40.") 

        self.__carga_horaria = nova_carga_horaria

    def calcula_salario(self):
        return self._salario_hora * self.carga_horaria * 4.5


class Estagiario(Funcionario):
    def __init__(self, nome, idade, email, carga_horaria):
        super().__init__(nome, idade, email, carga_horaria)
        self._salario_hora = 15.5
        self.__auxAlimentacao = 250
        self.carga_horaria = carga_horaria

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria < 16 or nova_carga_horaria > 30: 
            raise ValueError("A carga horária do estagiário deve ser maior ou igual a 16 e menor ou igual a 30.") 
        self.__carga_horaria = nova_carga_horaria

    def calcula_salario(self):
        return (self._salario_hora * self.carga_horaria * 4.5 +
                self.__auxAlimentacao)
 
class Vendedor(Funcionario):
    def __init__(self, nome, idade, email, carga_horaria):
        super().__init__(nome, idade, email, carga_horaria)
        self._salario_hora = 30
        self.__auxAlimentacao = 350
        self.__auxTransVisita = 30
        self.zerar_visitas()

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria < 15 or nova_carga_horaria > 45: 
            raise ValueError("A carga horária de vendedor deve ser maior ou igual a 15 e menor ou igual a 45.") 

        self.__carga_horaria = nova_carga_horaria

    def calcula_salario(self):
        return (self._salario_hora * self.carga_horaria * 4.5 + self.__auxAlimentacao + self.visitas * self.__auxTransVisita)

    @property
    def visitas(self):
        return self.__visitas

    def realizar_visita(self, n_visitas):
        if not isinstance(n_visitas, int):
            raise TypeError("O parâmetro n_visitas deve ser inteiro.")

        if n_visitas < 0 or n_visitas > 10:
            raise ValueError("O parâmetro n_visitas deve ser maior ou igual a 0 e menor ou igual a 10.")

        self.__visitas += n_visitas

    def zerar_visitas(self):
        self.__visitas = 0

class EmpresaCreationError(Exception):
    pass


class Empresa:
    def __init__(self, nome, cnpj, area_atuacao, equipe):
        self.nome = nome
        self.cnpj = cnpj
        self.area_atuacao = area_atuacao
        self.__equipe = []

        try:
            for f in equipe:
                self.contrata(f)
        except TypeError:
            raise EmpresaCreationError
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novoNome):
        if not isinstance(novoNome, str):
            raise EmpresaCreationError

        self.__nome = novoNome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, novoCnpj):
        if not isinstance(novoCnpj, str):
            raise EmpresaCreationError

        self.__cnpj = novoCnpj

    @property
    def area_atuacao(self):
        return self.__area_atuacao

    @area_atuacao.setter
    def area_atuacao(self, novaAreaAtuacao):
        if not isinstance(novaAreaAtuacao, str):
            raise EmpresaCreationError

        self.__area_atuacao = novaAreaAtuacao

    @property
    def equipe(self):
        return self.__equipe

    def contrata(self, novo_funcionario):
        if not isinstance(novo_funcionario, Funcionario):
            raise TypeError("O parâmetro novo_funcionario deve ser da classe Funcionario.")

        self.__equipe.append(novo_funcionario)

    def folha_pagamento(self):
        return sum([f.calcula_salario() for f in self.equipe])

    def dissidio_anual(self):
        for f in self.equipe:
            f.aumenta_salario()

    def listar_visitas(self):
        return {f.email : f.visitas for f in self.equipe
                if isinstance(f, Vendedor)}

    def zerar_visitas_vendedores(self):
        for f in self.equipe:
            if isinstance(f, Vendedor):
                f.zerar_visitas()

