import csv

def read_csv(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def print_data(data):
    for row in data:
        for key, value in row.items():
            print(f"{key} → {value}")
        print() 

def min_value(data, column):
    return min(float(row[column]) for row in data)

def max_value(data, column):
    return max(float(row[column]) for row in data)

def sum_values(data, column):
    return sum(float(row[column]) for row in data)

def count_values(data, column):
    return len(data)

def average_value(data, column):
    return sum_values(data, column) / count_values(data)

file_path = '11.csv'
data = read_csv(file_path)

print_data(data)

column_name = 'vozrast'  
print(f"min znathenie v stolbthe '{column_name}': {min_value(data, column_name)}")
print(f"max znathenie v stolbthe'{column_name}': {max_value(data, column_name)}")
print(f"symma znathenie v stolbthe'{column_name}': {sum_values(data, column_name)}")
print(f"kolithestvo znathenie v stolbthe'{column_name}': {count_values(data, column_name)}")
print(f"srednee znathenie v stolbthe'{column_name}': {average_value(data, column_name)}")
