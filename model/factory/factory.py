from model.documento import Documento
from model.departamento import Departamento


class Factory:
    def __init__(self):
        pass

    def newDepartamento(self, nome):
        departamento = Departamento(nome)
        return departamento

    def newDocumento(self, nome, caminho):
        documento = Documento(nome, caminho)
        return documento
