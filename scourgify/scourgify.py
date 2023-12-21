# import sys
# import csv

# students=[]

# if len(sys.argv) <3 :
#     sys.exit("Too few command-line arguments")
# elif len(sys.argv)>3:
#     sys.exit("Too many command-line arguments")
# elif len(sys.argv) ==3:
#     try:
#         with open(sys.argv[1], "r") as rfile, open(sys.argv[2],"w") as wfile:
#             reader = csv.DictReader(rfile)
#             for row in reader:
#                 splited = row ["name"].split(",")
#                 students.appends({"first":splited[1].lstrip(),
#                                   "last":splited[0],
#                                   "house":row["house']
#                                   })
#              writer=csv.DictWriter(wfile, fieldnames=["first","last","house"])
#              writer.writerow({"first":"first","last":"last","house":"house"})
#              for row in students:
#                 writer.writerow({
#                     "first":row["first"],
#                     "last":row["last"],
#                     "house":row["house"]
#                 })

#     except FileNotFoundError:
#         sys.exit("Could not read invalid_file.csv")

import sys
import csv

if (len(sys.argv) < 3):
    sys.exit("Too few command-line arguments")
elif (len(sys.argv) > 3):
    sys.exit("Too many command-line arugments")

input_csv_file, output_csv_file = sys.argv[1:]
if not input_csv_file.endswith(".csv"):
    sys.exit("Not a CSV File")

cleaned_output = []
try:
    with open(input_csv_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row['name'].split(", ")
            house = row["house"]
            cleaned_output.append(
                {"first": first, "last": last, "house": house})

    with open(output_csv_file, 'w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(cleaned_output)


except FileNotFoundError:
    sys.exit(f"Could not read {input_csv_file}")