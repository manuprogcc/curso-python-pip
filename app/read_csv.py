import csv

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",") #Reader es un iterable.
        header = next (reader) #Conseguimos las llaves.  Con next obtenemos la 1era fila ya que iteramos solo la primera fila.
        data = []

        for row in reader:
            iterable = zip(header, row) #Unirá los header y los row en tuplas. 
            country_dic = {key: value for key, value in iterable} #Generaremos un diccionario.
            data.append(country_dic) #Cada iteración, agregará a la lista un diccionario con su llave y valor.
        return data

if __name__ == "__main__":
    data = read_csv("data.csv")
    print(data[0]) #El 0 es para ver solo la posición 0.

# Tenemos una lista con valores. Por lo que lo transformaremos en un diccionario. La llave será el nombre de la columna.

