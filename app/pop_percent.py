import read_csv
import charts


def run():
    dict_data = read_csv.read_csv('/home/jnog/Platzi/01_Python/02_comprehensions/app/data.csv')
    #print(dict_data)
    #Funcion lambda para hacer un diccionario con dos columnas
    new_dict = dict(map(lambda data: (data["Country/Territory"], data["World Population Percentage"]), dict_data))
    print(new_dict)
    labels = new_dict.keys()
    values = new_dict.values()
    charts.generate_pie_chart(labels, values)
    return labels, values


if __name__ == '__main__':
    run()
    