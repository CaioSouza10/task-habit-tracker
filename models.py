from abc import ABC, abstractmethod
import re

data_padrao = r"^\d{4}-\d{2}-\d{2}$"
padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
"""^ e $: Garantem que a string inteira deve seguir o padrão (do início ao fim).

[\w\.-]+: Aceita letras, números, underline, ponto ou hífen antes do @.

@: Exige o símbolo de arroba.

[\w\.-]+: Aceita o nome do domínio (ex: gmail, yahoo).

\.\w+: Exige um ponto literal (\.) seguido da extensão (ex: com, br)."""


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, txt):
        txt = txt.strip()
        if not re.match(padrao, txt):
            raise ValueError('E-mail inválido!')
        else:
            self._email = txt


class ItemBase(ABC):
    def __init__(self, titulo:str, descricao:str='', concluido:bool=False):
        self.titulo = titulo
        self.descricao = descricao
        self.concluido = concluido

    @abstractmethod
    def marcar_como_concluido(self):
        pass


class Tarefa(ItemBase):
    def __init__(self, titulo, data_limite:str, descricao: str='', concluido:bool = False):
        super().__init__(titulo, descricao, concluido)
        self.data_limite = data_limite

    @property
    def data_limite(self):
        return self._data_limite

    @data_limite.setter
    def data_limite(self, data):
        data = data.strip()
        if not re.match(data_padrao, data):
            raise ValueError('ERRO! A data está em um formato inválido.')
        else:
            self._data_limite = data

    def marcar_como_concluido(self):
        self.concluido = True 


class Habito(ItemBase):
    def __init__(self, titulo, frequencia_dias:int, sequencia_atual:int=0 ,descricao = '', concluido = False):
        super().__init__(titulo, descricao, concluido)
        self.frequencia_dias = frequencia_dias
        self.sequencia_atual = sequencia_atual

    def marcar_como_concluido(self):
        self.concluido = True 
        self.sequencia_atual += 1


"""    DOC

Classe Usuario: Encapsula nome e e-mail. Usa @property e @email.setter com REGEX (r"^[\w\.-]+@[\w\.-]+\.\w+$") para impedir o cadastro de e-mails malformados.

Classe Abstrata ItemBase(ABC): Define o contrato comum (titulo, descricao, concluido) e obriga via @abstractmethod que qualquer item derivado implemente sua própria lógica de conclusão.

Classe Tarefa(ItemBase): Especializa um item adicionando data_limite, validada via REGEX no formato ISO (YYYY-MM-DD), e implementa marcar_como_concluido apenas alterando o status booleano.

Classe Habito(ItemBase): Especializa um item recorrente (frequencia_dias, sequencia_atual) e aplica polimorfismo ao sobrescrever marcar_como_concluido para também incrementar o contador de sequência (+= 1).
"""