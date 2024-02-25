import csv
from converter.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from converter.distance import meters_to_feet, feet_to_meters


def convert_temperature(temperature_str, target_temp):
    value, unit = float(temperature_str[:-2]), temperature_str[-2:]
    if unit == '°C' and target_temp == 'F':
        return celsius_to_fahrenheit(value)
    elif unit == '°F' and target_temp == 'C':
        return fahrenheit_to_celsius(value)
    return value


def convert_distance(distance_str, target_dist):
    value, unit = float(distance_str.replace('ft', 'f')[:-1]), distance_str[-1]
    if unit == "m" and target_dist == "ft":
        return meters_to_feet(value)
    elif unit == "f" and target_dist == "m":
        return feet_to_meters(value)
    return value


def standardize(input_file, output_file, target_temp, target_dist):
    with open(input_file, 'r') as in_file, open(output_file, 'w', newline='') as out_file:
        reader = csv.reader(in_file)
        writer = csv.writer(out_file)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            date, dist_str, temp_str = row
            converted_dist = convert_distance(dist_str, target_dist)
            converted_temp = convert_temperature(temp_str, target_temp)
            writer.writerow([date, f'{round(converted_dist, 1)}{target_dist}',
                            f'{round(converted_temp, 1)}°{target_temp}'])


if __name__ == '__main__':
    input_file = 'input_data.csv'
    output_file = 'standardized_measurements.csv'
    target_temp = 'F'
    target_dist = 'm'
    standardize(input_file, output_file, target_temp, target_dist)
