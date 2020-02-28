#wczytaj dane
#uruchom naprzemiennie funkcje - zamaluj kratki i skresl kratki
#wyswietl obrazek


def draw():
    print("Nothing")


def color_boxes():
    print("Nothing")


def remove_boxes():
    print("Nothing")


if __name__ == "__main__":
    width = 10
    height = 10

    table = [[None for i in range(width)] for j in range(height)]
    mask = [[None for i in range(width)] for j in range(height)]

    columns = [[5], [7], [8], [8], [8], [8], [8], [8], [7], [5]]
    rows = [[2,2], [4,4], [10], [10], [10], [10], [8], [6], [4], [2]]