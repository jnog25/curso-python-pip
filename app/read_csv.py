import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

if __name__ == '__main__':
    resultado = read_csv('/home/jnog/Platzi/01_Python/02_comprehensions/app/data.csv')
    print(resultado[0])