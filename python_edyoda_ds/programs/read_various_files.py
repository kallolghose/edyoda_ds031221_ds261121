import csv

def read_csv(filename):
    fields = []
    rows = []

    with open(filename, "r") as file:
        csvreader = csv.reader(file)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

        print("Total Lines : {}".format(csvreader.line_num))
    
    print("Fields names are {}".format(",".join(field for field in fields)))

    for r in rows:
        for col in r:
            print("{}".format(col), end=", ")
        print("")


def write_csv_list(filename):
    fields = ['Name', 'Branch', 'Year', 'CGPA']
 
    # data rows of csv file
    rows = [['Nikhil', 'COE', '2', '9.0'],
            ['Sanchit', 'COE', '2', '9.1'],
            ['Aditya', 'IT', '2', '9.3'],
            ['Sagar', 'SE', '1', '9.5'],
            ['Prateek', 'MCE', '3', '7.8'],
            ['Sahil', 'EP', '2', '9.1']]
    
    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def write_csv_dict(file_name):
    fields = ['name', 'branch', 'year', 'cgpa']
    mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
         {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
         {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
         {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
         {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
         {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]

    with open(file_name, "w") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fields)
        csv_writer.writeheader()
        csv_writer.writerows(mydict)


read_csv("C:/Users/Hp/OneDrive/Documents/workspace/edYoda/python_space/test_csv.csv")
write_csv_list("C:/Users/Hp/OneDrive/Documents/workspace/edYoda/python_space/test_csv_list.csv")
write_csv_dict("C:/Users/Hp/OneDrive/Documents/workspace/edYoda/python_space/test_csv_dict.csv")
     