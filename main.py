import csv
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


def convert_temperature(temperature_str, target_temp):
    value, unit = float(temperature_str[:-2]), temperature_str[-2:]
    if unit == '°C' and target_temp == 'F':
        return celsius_to_fahrenheit(value)
    elif unit == '°F' and target_temp == 'C':
        return fahrenheit_to_celsius(value)
    return value


def standardize(input_file, output_file, target_t):
    with open(input_file, 'r') as in_file, open(output_file, 'w', newline='') as out_file:
        reader = csv.reader(in_file)
        writer = csv.writer(out_file)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            date, temp_str = row
            converted_temp = convert_temperature(temp_str, target_t)
            writer.writerow([date, f'{round(converted_temp, 1)}°{target_t}'])


input_file = 'input_data.csv'
output_file = 'standardized_measurements.csv'
target_t = 'C'
standardize(input_file, output_file, target_t)