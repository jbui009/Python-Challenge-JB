import os
import csv

path = "../Downloads/budget_data 3.csv"

budget_data_path = os.path.join('..','Downloads', 'budget_data 3.csv')

months = 0
total_profit = 0
change_in_month = []
change = 0
greatest_increase = 0
greatest_decrease = 0
previous_profit = 0
average_change = 0

with open(budget_data_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        print(row)
        date = row[0]
        profit_losses = int(row[1])
        profit_gain = int(row[1])
        total_profit = total_profit + profit_gain
        print(total_profit)
        change = profit_losses - previous_profit

        if months != 1:
            change_in_month.append(change)
        if change > greatest_increase:
            greatest_increase = change
            greatest_month = date
        if change < greatest_decrease:
            greatest_decrease = change
            lowest_month = date

        previous_profit = profit_losses

average_change = int(round(sum(change_in_month)/len(change_in_month), 2))

print("Financial Analysis")
print("______________________")
print(months)
print(total_profit)
print(average_change)
print(greatest_increase)
print(greatest_decrease)


output_file = "output.txt"
with open(output_file, "w") as doc:
    doc.write(data)