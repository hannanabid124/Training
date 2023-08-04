import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime


def process_weather_data(file_path):

    """
    This function process weather data from a CSV file
    and find maximum temperature, minimum temperature,
    and maximum humidity along with their corresponding dates.

    Parameters:
        file_path (str): The path to the CSV
        file containing weather data files.

    Returns:
             max_temperature_value (float): \
                 The maximum temperature value.
             max_temperature_date (str): The date \
                 corresponding to the maximum temperature.
             min_temperature_value (float): The minimum \
                 temperature value.
             min_temperature_date (str): The date corresponding \
                 to the minimum temperature.
             max_humidity_value (int): The maximum humidity value.
             max_humidity_date (str): The date corresponding \
                 to the maximum humidity.
    """
    date_format = '%Y-%m-%d'
    data_list = []

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_list.append(row)

    highest_temperature = 'Max TemperatureC'
    highest_temperature_index = data_list[0].index(highest_temperature)

    lowest_temperature = 'Min TemperatureC'
    lowest_temperature_index = data_list[0].index(lowest_temperature)

    highest_humidity = 'Max Humidity'
    highest_humidity_index = data_list[0].index(highest_humidity)

    columns_to_check = [
        highest_temperature_index,
        lowest_temperature_index,
        highest_humidity_index]

    data_list = [row for row in data_list if all(row[col]
                 for col in columns_to_check)]

    max_temperature_value = max([float(each_row[highest_temperature_index])
                                 for each_row in data_list[1:]])
    max_temperature_date = datetime.strptime
    (data_list[max_temperature_value_index + 1][0], date_format)

    min_temperature_value = min([float(each_row
                                       [lowest_temperature_index])
                                 for each_row in data_list[1:]])
    min_temperature_date = datetime.strptime
    (data_list[min_temperature_value_index + 1][0], date_format)

    max_humidity_value = max([int(each_row[highest_humidity_index])
                              for each_row in data_list[1:]])
    max_humidity_date = datetime.strptime
    (data_list[max_humidity_value_index + 1][0], date_format)

    return (max_temperature_value, max_temperature_date,
            min_temperature_value, min_temperature_date,
            max_humidity_value, max_humidity_date)


def process_all_files_in_folder(folder_path, year):

    """
    This function process all weather data files in
    the given folder for a specific year and
    find the highest temperature, lowest temperature
    and highest humidity along with their corresponding dates.

    Parameters:
        folder_path (str): The path to the folder
        containing weather data files.
        year (int): The year for which weather data is to be processed.

    Returns:
        This function does not return anything.
        It prints the results and draws a horizontal bar chart.
    """

    max_temp_all_files = float()
    max_temp_date = ''
    min_temp_all_files = float()
    min_temp_date = ''
    max_humidity_all_files = 0
    max_humidity_date = ''

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt') and str(year) in file_name:
            file_path = os.path.join(folder_path, file_name)
    (max_temp, max_temp_date_curr,
     min_temp, min_temp_date_curr,
     max_humidity, max_humidity_date_curr) = process_weather_data(file_path)

    if max_temp > max_temp_all_files:
        max_temp_all_files = max_temp
        max_temp_date = max_temp_date_curr

    if min_temp < min_temp_all_files:
        min_temp_all_files = min_temp
        min_temp_date = min_temp_date_curr

    if max_humidity > max_humidity_all_files:
        max_humidity_all_files = max_humidity
        max_humidity_date = max_humidity_date_curr

    print('Highest Temperature:', max_temp_all_files, "C on", max_temp_date)
    print('Lowest Temperature:', min_temp_all_files, "C on", min_temp_date)
    print('Highest Humidity:', max_humidity_all_files, "% on",
          max_humidity_date)


def calculate_average_values(folder_path, year, month):

    """
    This function calculates average values of highest
    temperature, lowest temperature, and humidity

    for a specific year and month from
    weather data files in the given folder.

    Parameters:
        folder_path (str): The path to the folder
        containing weather data files.
        year (int): The year for which average values are to be calculated.

    Returns:
        This function does not return anything. It prints the average values.
    """


months = {
    '01': "Jan", '02': "Feb", '03': "Mar",
    '04': "Apr", '05': "May", '06': "Jun",
    '07': "Jul", '08': "Aug", '09': "Sep",
    '10': "Oct", '11': "Nov", '12': "Dec"
         }


def calculate_average_weather_data(folder_path, year, month):
    if month in months:
        month = months[month]
    else:
        print("Invalid month format. Please enter a valid month"
              "in the format MM.")
        return

    # Implement the average value calculation here
    total_high_temp = 0
    total_low_temp = 0
    total_humidity = 0
    count = 0

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt') and str(year) in file_name and \
                month in file_name:
            file_path = os.path.join(folder_path, file_name)
            max_temp, _, min_temp, _, \
                humidity, _ = process_weather_data(file_path)

            total_high_temp += max_temp
            total_low_temp += min_temp
            total_humidity += humidity
            count += 1

    if count == 0:
        print("No data found for the given year and month.")
    else:
        average_high_temp = total_high_temp / count
        average_low_temp = total_low_temp / count
        average_humidity = total_humidity / count

        print('Average Highest Temperature:', average_high_temp, "C")
        print('Average Lowest Temperature:', average_low_temp, "C")
        print('Average Humidity:', average_humidity, "%")


def draw_horizontal_bar_chart(max_temp, min_temp):
    """
    This function draws a horizontal bar chart
    to display the highest and lowest temperatures.

    Parameters:
        max_temp (float): The highest temperature value to be displayed.
        min_temp (float): The lowest temperature value to be displayed.

    Returns:
        This function does not return anything.
        It displays the bar chart using matplotlib.
    """

    max_temp_float = float(max_temp)
    min_temp_float = float(min_temp)

    plt.barh(['Max Temperature', 'Min Temperature'],
             [max_temp_float, min_temp_float],
             color=['red', 'blue'])
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Temperature Type')
    plt.title('Highest and Lowest Temperatures')
    plt.show()
