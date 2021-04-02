from model.factory.factory import Factory


class Sistema:
    def __init__(self):
        factory = Factory()
        departamento = factory.newDepartamento()
        pass


def getEntrada():

    opt = None

    print("Selecione a opcao:")
    print("1) Cadastrar documento")
    print("2) Visualizar documento")
    print("0) Sair")
    opt = int(input())

    while(opt not in [0,1,2]):
        print("Entrada invalida!! Digite outra")
        opt = int(input())

    return opt


def main():

    opt = getEntrada()

    while(opt != 0):

        if(opt == 1):

            print("Digite as informacoes do arquivo:")

            print("Nome: ")
            nome = input()
            print("Caminho:")
            caminho = input()
            print("Tipo:")
            tipo = intpu()
            print("Data:")
            data = input()


        if(opt == 2):


        opt = getEntrada()


if __name__ == "__main__":
    main()
