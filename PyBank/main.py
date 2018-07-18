#import dependencies
import csv

#Read in a .csv file
with open('budget_data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader: 
        print(row) 
         
#The total number of months included in the dataset
months = ["Date"]


print ("Count for number of months : ", months.count)

profitlosses = ["Profit/Losses"]
total_profitlosses = 0

#The total amount of profit/losses gained over the entire period
total_profitlosses = ["Profit/Losses"].sum()

#The average change in profit/losses between months over the entire period
average_profitlosses = (total_profitlosses / 42) 
print(average_profitlosses)


#The greatest decrease in profit/losses over the entire period
#max_profitlosses = def.profit.diff().max()
max_profitlosses = ["Profit/Losses"].max()
max_profitlosses

date = ["Profit/Losses" == max_profitlosses, "Date"]
max_date = date.iloc[0]
max_date

#The greatest increase in profit/losses (date and amount) over the entire per
min_profitlosses = ["Profit/Losses"].min()


min_date = loc[df["Profit/Losses"] == min_profitlosses, "Date"]
min_date_loc = date.iloc[0]
min_date_loc
#min_date

print(f" Total Months: {months}\n Total Profit/Losses: {total_profitlosses}\n Average Revenue Change: {average_profitlosses}\n Greatest Increase in Revenue: {max_date} {max_profitlosses}\n Greatest Decrease in Profit/Losses: {min_date_loc} {min_profitlosses}")



