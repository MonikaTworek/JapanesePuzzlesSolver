#wczytaj dane
#uruchom naprzemiennie funkcje - zamaluj kratki i skresl kratki
#wyswietl obrazek

width = 10
height = 10

table = [[None for i in range(width)] for j in range(height)]
mask = [[None for i in range(width)] for j in range(height)]

columns = [[5], [7], [8], [8], [8], [8], [8], [8], [7], [5]]
rows = [[2, 2], [4, 4], [10], [10], [10], [10], [8], [6], [4], [2]]


def draw():
    for i in range(height):
        print(table[i])


def is_in_progress():
    for i in range(width):
        for j in range(height):
            if table[i][j] is None:
                return True
    return False


def color_boxes():
    ####WERSJA BEZ PATRZENIA CO JEST W TABLICY
    for col in range(height):
        counter = 0
        type = 0
        last_is_zero = False
        ### sprawdzić, czy jak jest puste, a my jesteśmy w trybie zaznacz jakby kolor (type %2 = 0), to przesuń się o tyle ile jest już wykreślone
        ### sprawdzić, czy jeżeli jest coś zakolorowane, to możemy to dokończyć...
        for number in rows[col]:
            for j in range(number):
                mask[col][counter] = type
                counter += 1
            last_is_zero = False
            if counter < height: #co jak mam dokładnie i dodanie pustego miałoby wyjść poza?
                type += 1
                mask[col][counter] = type
                counter += 1
                last_is_zero = True
                type += 1

        #idziemy od drgiej strony i sprawdzamy, czy typy się zgadzają
        pointer = height - 1
        temp = reversed(rows[col])
        if last_is_zero:
            type -= 2

        for number in temp:
            for j in range(number):
                if mask[col][pointer] == type:
                    table[col][pointer] = "X"
                pointer -= 1
            type -= 1
            if pointer > 0:
                if mask[col][pointer] == type:
                    table[col][pointer] = "_"
                pointer -= 1
                type -= 1

        for k in range(height):
            mask[col][k] = None

    for col in range(width):
        counter = 0
        type = 0
        last_is_zero = False
        for number in columns[col]:
            for j in range(number):
                mask[counter][col] = type
                counter += 1
            last_is_zero = False
            if counter < width: #co jak mam dokładnie i dodanie pustego miałoby wyjść poza?
                type += 1
                mask[counter][col] = type
                counter += 1
                last_is_zero = True
                type += 1

        #idziemy od drgiej strony i sprawdzamy, czy typy się zgadzają
        pointer = width - 1
        temp = reversed(columns[col])
        if last_is_zero:
            type -= 2

        for number in temp:
            for j in range(number):
                if mask[pointer][col] == type:
                    table[pointer][col] = "X"
                pointer -= 1
            type -= 1
            if pointer > 0:
                if mask[pointer][col] == type:
                    table[pointer][col] = "_"
                pointer -= 1
                type -= 1

        for k in range(height):
            mask[k][col] = None

#pomysł -> każda kolumna w osobnym wątku i potem podobnie dla wierszy


def remove_boxes():
    print("Nothing")


if __name__ == "__main__":
    in_progress = True
    while in_progress:
        color_boxes()
        remove_boxes()
        in_progress = is_in_progress()

    draw()