import csv
import os
import matplotlib.pyplot as plt

def process_weather_data(file_path):
    
    data_list = []
    

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_list.append(row)

    highestTemperature = 'Max TemperatureC'
    highestTemperature_index = data_list[0].index(highestTemperature)

    lowestTemperature = 'Min TemperatureC'
    lowestTemperature_index = data_list[0].index(lowestTemperature)

    highestHumidity = 'Max Humidity'
    highestHumidity_index = data_list[0].index(highestHumidity)

    columns_to_check = [
        highestTemperature_index, 
        lowestTemperature_index, 
        highestHumidity_index]
    
    data_list = [row for row in data_list if all(row[col] 
                                                 for col in columns_to_check)]

    column_values = [float(each_row[highestTemperature_index]) 
                     for each_row in data_list[1:]]
    
    max_temperature_value = max(column_values)
    max_temperature_value_index = column_values.index(max_temperature_value)
    max_temperature_row = data_list[max_temperature_value_index + 1]

    column_values = [float(each_row[lowestTemperature_index]) for each_row in data_list[1:]]
    min_temperature_value = min(column_values)
    min_temperature_value_index = column_values.index(min_temperature_value)
    min_temperature_row = data_list[min_temperature_value_index + 1]

    column_values = [int(each_row[highestHumidity_index]) for each_row in data_list[1:]]
    max_humidity_value = max(column_values)
    max_humidity_value_index = column_values.index(max_humidity_value)
    max_humidity_row = data_list[max_humidity_value_index + 1]

    return max_temperature_value, max_temperature_row[0], min_temperature_value, min_temperature_row[0], max_humidity_value, max_humidity_row[0]

def process_all_files_in_folder(folder_path, year):
    max_temp_all_files = float('-inf')
    max_temp_date = ''
    min_temp_all_files = float('inf')
    min_temp_date = ''
    max_humidity_all_files = 0
    max_humidity_date = ''

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt') and str(year) in file_name:
            file_path = os.path.join(folder_path, file_name)
            max_temp, max_temp_date_curr, min_temp, min_temp_date_curr, max_humidity, max_humidity_date_curr = process_weather_data(file_path)

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
    print('Highest Humidity:', max_humidity_all_files, "% on", max_humidity_date)
    
    draw_horizontal_bar_chart(max_temp_all_files, min_temp_all_files)

    
def calculate_average_values(folder_path, year, month):
    months = {'01': "Jan", '02': "Feb", '03': "Mar", '04': "Apr", '05': "May", '06': "Jun",
              '07': "Jul", '08': "Aug", '09': "Sep", '10': "Oct", '11': "Nov", '12': "Dec"}

    if month in months:
        month = months[month]
    else:
        print("Invalid month format. Please enter a valid month in the format MM.")
        return

    # Implement the average value calculation here
    total_high_temp = 0
    total_low_temp = 0
    total_humidity = 0
    count = 0

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt') and str(year) in file_name and month in file_name:
            file_path = os.path.join(folder_path, file_name)
            max_temp, _, min_temp, _, humidity, _ = process_weather_data(file_path)

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
    plt.barh(['Max Temperature', 'Min Temperature'], [max_temp, min_temp], color=['red', 'blue'])
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Temperature Type')
    plt.title('Highest and Lowest Temperatures')
    plt.show()

if __name__ == "__main__":
    folder_path = '/Users/abdulhannan/Desktop/WeatherMan/weatherfiles'

    while True:
        choice = input("Enter 'H' to see highest values, 'A' to see average values, or 'Q' to quit: ")

        if choice.upper() == 'H':
            y = input("Enter Year: ")
            process_all_files_in_folder(folder_path, y)
        elif choice.upper() == 'A':
            y = input("Enter Year: ")
            m = input("Enter Month (in the format MM): ")
            calculate_average_values(folder_path, y, m)
        elif choice.upper() == 'Q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 'H', 'A', or 'Q'.")