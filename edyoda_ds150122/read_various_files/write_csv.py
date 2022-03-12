import csv


def write_csv(filename):
    fields = ['Name', 'Branch', 'Year', 'CGPA']
    row1 = ['Nikhil', 'CSE', '3', '9.0']
    row2 = ['Sandeep', 'ECE', '4', '9.5']
    row3 = ['Kallol', 'CSE', '4', '8.0']
    row4 = ['Jitendra', 'CSE', '3', '8.9']

    rows = [row1, row2, row3, row4]

    with open(filename, "w") as fp:
        csv_write_obj = csv.writer(fp)
        csv_write_obj.writerow(fields)  # write the line to the file
        # csv_write_obj.writerow(row1) # []
        # csv_write_obj.writerow(row2) # []
        # csv_write_obj.writerow(row3) # []
        csv_write_obj.writerows(rows) # [[]]


write_csv("C:/Users/Hp/OneDrive/Documents/workspace/edYoda/python_space/cgpa.csv")



