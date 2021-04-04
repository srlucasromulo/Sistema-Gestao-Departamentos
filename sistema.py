from model.creator.creator import Creator
from model.departamento import Departamento
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
    if data > datetime.today(): # acertar isso
        raise Exception

    return nome, caminho, tipo, data


def readDocumento():
    pass

def main():

    creator = Creator()
    departamento = Creator().getDepartamento()

    opt = getEntrada()

    while opt != 0:

        if opt == 1:
            try:
                info = getDocumento()
                documento = creator.newDocumento(info[0],info[1],info[2],info[3])
            except Exception:
                pass

        if opt == 2:
            readDocumento()

        opt = getEntrada()


if __name__ == "__main__":
    main()
