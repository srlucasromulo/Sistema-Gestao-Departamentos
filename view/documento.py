class DocumentoView:

    def __init__(self):
        pass

    @staticmethod
    def toString(documentos):

        string = []

        for doc in documentos:
            print("Nome: " + doc.getNome())
            print("Caminho: " + doc.getCaminho())
            print("Tipo: " + doc.getTipo())
            print("Data: {}".format(doc.getData()))
