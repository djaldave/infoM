import csv

with open('in.csv', newline='') as f_input, open('output.csv', 'w+', newline='') as f_output:
    csv_input = csv.reader(f_input, skipinitialspace=True)
    csv_output = csv.writer(f_output, quoting=csv.QUOTE_NONNUMERIC)

    for row_input in csv_input:
        row_output = ["insert into tblfake_apps(id, name, category, downloads, price) values ("]
        for col in row_input:

            try:
                row_output.append(int(col))
            except ValueError as e:
                row_output.append(col)
        row_output.append(")")
        csv_output.writerow(row_output)
