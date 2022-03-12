import csv


# User Defined Function
def read_csv(filename):
    print("Opening file {}".format(filename))

    fields = [] # Storing Headers
    rows = [] # Store the values/rows
    with open(filename, "r") as fp:
        csv_obj = csv.reader(fp)
        fields = next(csv_obj) # this is to extract all the headers

        # For loop is to extract all the rows
        for line in csv_obj:
            rows.append(line)

        print("===HEADERS====")
        print(fields)
        print("===ROWS====")
        for row in rows:
            print(row)


read_csv("C:/Users/Hp/OneDrive/Documents/workspace/edYoda/python_space/test_csv.csv")
