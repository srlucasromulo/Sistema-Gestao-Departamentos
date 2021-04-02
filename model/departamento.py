class Departamento:

    __instancia = None

    def __init__(self):
        self.__nome = "Departamento tal da UFSJ"
        self.__cursos = []
        self.__funcionarios = []
        self.__documentos = []

    def getInstancia():     # Singleton
        if self.__instancia is None:
            self.__instancia = Departamento()
        return self.__instancia

    def getNome():
        return self.__nome

    def setNome(nome):
        self.__nome = nome

    def getCursos():
        return self.__cursos

    def setCursos(cursos):
        self.__cursos = cursos

    def getFuncionarios():
        return self.__funcionarios

    def setFuncionarios(funcionarios):
        self.__funcionarios = funcionarios

    def getDocumentos():
        return self.__documentos

    def setDocumentos(documentos):
        self.__documentos = documentos
