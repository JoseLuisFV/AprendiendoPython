from Heroe import Heroe


def main():
    print('hI')
    zane = Heroe('Zane', 'clerigo')
    zane.presentacion()
    zane.ver_mis_stats()
    bioz = Heroe('BIOZ', 'Espantan')
    bioz.presentacion()
    bioz.ver_mis_stats()
    name = "fafa"
    if isinstance(name, str):
        print(name)


if __name__ == '__main__':
    main()
