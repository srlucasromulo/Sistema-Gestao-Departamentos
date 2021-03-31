from model.factory.factory import Factory


class Sistema:
    def __init__(self):
        factory = Factory()
        departamento = factory.newDepartamento("Robson")
        pass


def main():
    pass


if __name__ == "__main__":
    main()
