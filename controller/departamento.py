class DepartamentoController:
    def __init__(self):
        pass

    @staticmethod
    def addDocumento(departamento, documento):
        documentos = departamento.getDocumentos()
        documentos.append(documento)
        departamento.setDocumentos(documentos)
