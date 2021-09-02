class Cliente:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    @property #getter
    def nome(self):
        return self.__nome

    @property #getter
    def telefone(self)  :
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        if not isinstance(novo_email, str):
            # raise TypeError("Apenas strings!")
            print('não é string')

        if '@' not in novo_email:
            raise ValueError("Email inválido!")
            
        self.__email = novo_email


#CONSTRUÇÃO
cliente = Cliente('Matheus', '951701730', 'matheus@fernandes.com.br')
print('---------Getter---------')
print(cliente.nome)
print(cliente.email)
print(cliente.telefone)
print('---------Fim do Getter---------')

print('---------Setter---------')
cliente.email = 10
cliente.email = "xxxxxx"
cliente.email = "email@email.com"
print(cliente.email)
print('---------Fim do Setter---------')