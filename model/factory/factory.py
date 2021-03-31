class Factory:
    def __init__(self):
        pass

    def newDepartamento(nome):
        departamento = Departamento(nome)
        return departamento

    def newDocumento(nome, caminho):
        documento = Documento(nome, caminho)
        return documento
