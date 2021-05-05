class Cliente():
    def __init__(self, nome, data_nascimento, email, profissao, sexo):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__email = email
        self.__profissao = profissao
        self.__sexo = sexo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def profissao(self):
        return self.profissao

    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo
