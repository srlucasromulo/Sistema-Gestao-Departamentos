from model.creator.creator import Creator
from model.departamento import Departamento
from controller.departamento import DepartamentoController
from datetime import datetime


def getEntrada():
    opt = None

    print("Selecione a opcao:")
    print("1) Cadastrar documento")
    print("2) Visualizar documento")
    print("0) Sair")
    opt = int(input())

    while opt not in [0, 1, 2]:
        print("Entrada invalida!! Digite outra")
        opt = int(input())

    return opt


def getDocumento():
    print("Digite as informacoes do arquivo:")

    print("Nome: ")
    nome = input()

    print("Caminho:")
    caminho = input()
    caminho = "/home/lucasromulo/tmp/PDFs/" + caminho
    try:
        arquivo = open(caminho, "r")
    except FileNotFoundError:
        print("Arquivo nao encontrado!!")
        raise Exception

    print("Tipo:")
    tipo = input()

    print("Data(DD/MM/YYYY):")
    data = input()
    dia, mes, ano = map(int, data.split('/'))
    data = datetime(ano, mes, dia)
    if data > datetime.today():  # acertar isso
        raise Exception

    return nome, caminho, tipo, data


def readDocumento():
    creator = Creator()
    nome = None
    caminho = None
    tipo = None
    data = None

    print("Buscar por qual informacao?:")
    print("1) Nome")
    print("2) Caminho")
    print("3) Tipo")
    print("4) Data")
    opt = int(input())

    if opt not in [1, 2, 3, 4]:
        print("Opcao invalida!!")
    else:
        if opt == 1:
            print("Digite o nome:")
            nome = input()
        if opt == 2:
            print("Digite o caminho:")
            caminho = input()
            caminho = "/home/lucasromulo/tmp/PDFs/" + caminho
        if opt == 3:
            print("Digite o tipo:")
            tipo = input()
        if opt == 4:
            print("Digite a data(DD/MM/YYYY):")
            data = input()
            dia, mes, ano = map(int, data.split('/'))
            data = datetime(ano, mes, dia)

    return creator.newDocumento(nome, caminho, tipo, data)


def main():
    creator = Creator()
    departamento = Creator().getDepartamento()

    opt = getEntrada()

    while opt != 0:

        if opt == 1:
            try:
                info = getDocumento()
                documento = creator.newDocumento(info[0], info[1], info[2], info[3])
                DepartamentoController.addDocumento(departamento, documento)
            except Exception:
                pass

        if opt == 2:
            documento = readDocumento()
            documentos = DepartamentoController.readDocumento(departamento, documento)
            print(documentos)

        opt = getEntrada()


if __name__ == "__main__":
    main()
