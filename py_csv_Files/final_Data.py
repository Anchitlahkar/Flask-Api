import csv

rows = []
with open("Filtered_Data.csv", "r") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        rows.append(row)

headers = rows[0]
star_data = rows[1:]


final_Star_list = []

for value in star_data:
  temp_dict = {
      "Name": value[1],
      "Distance": value[2],
      "Mass": value[3],
      "Radius": value[4],
      "Gravity": value[5],
  }

  final_Star_list.append(temp_dict)

print(final_Star_list)
