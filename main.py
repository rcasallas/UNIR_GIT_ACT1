import os
import sys
import argparse

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

def sort_list(items, ascending=True):
    """Ordena una lista en orden ascendente o descendente."""
    if not isinstance(items, list):
        raise RuntimeError(f"No se puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))

def remove_duplicates_from_list(items):
    """Elimina los duplicados de una lista."""
    return list(set(items))

def read_words_from_file(filename):
    """Lee las palabras de un archivo. Si el archivo no existe, devuelve una lista predeterminada."""
    if not os.path.isfile(filename):
        print(f"El archivo {filename} no existe, usando palabras predeterminadas.")
        return ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]  # Evita agregar líneas vacías

def main():
    parser = argparse.ArgumentParser(description="Procesa un archivo de palabras.")
    parser.add_argument("filename", nargs="?", default=DEFAULT_FILENAME, help="El archivo que contiene las palabras")
    parser.add_argument("remove_duplicates", nargs="?", default="no", choices=["yes", "no"],
                        help="Indica si se deben eliminar duplicados ('yes' o 'no')")
    
    args = parser.parse_args()

    # Leer las palabras del archivo o lista predeterminada
    word_list = read_words_from_file(args.filename)

    # Eliminar duplicados si el argumento lo indica
    if args.remove_duplicates.lower() == "yes":
        word_list = remove_duplicates_from_list(word_list)

    # Ordenar la lista en orden ascendente
    sorted_words = sort_list(word_list)
    
    print(sorted_words)

if __name__ == "__main__":
    main()
