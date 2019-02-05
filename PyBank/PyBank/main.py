import os 
import csv

csvpath=os.path.join("budget_data.csv")
myList = list(csv.reader(open('budget_data.csv')))

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    months=0
    profitloss=0
    changesum=0.00
    maxchange=0
    minchange=10000000

    csv_header = next(csvreader)
    for row in csvreader:
        months+=1
        profitloss+=float(row[1])
        if months==1:
            previous=float(row[1])
        else:
            change=float(row[1])-previous
            previous=float(row[1])
            changesum+=change

            if change>maxchange:
                maxchange=change
                maxmonth=row[0]
            elif change<minchange:
                minchange=change
                minmonth=row[0]

avg=round(changesum/(months-1),2)
print("Financial Analysis")    
print("----------------------------------")
print("Total Months: "+str(months))
print("Total Profit/Losses: "+str(profitloss))
print("Average Change: "+str(avg))
print("Greatest Increase in Profits: "+maxmonth+" ($"+str(maxchange)+")")
print("Greatest Decrease in Profits: "+minmonth+" ($"+str(minchange)+")")

output_file = os.path.join("output.txt")
with open(output_file, 'w') as textfile:
    textfile.write("Financial Analysis"+"\n")
    textfile.write("----------------------------------------"+"\n")
    textfile.write("Total Months: "+str(months)+"\n")
    textfile.write("Total Profit/Losses: "+str(profitloss)+"\n")
    textfile.write("Average Change: "+str(avg)+"\n")
    textfile.write("Greatest Increase in Profits: "+maxmonth+" ($"+str(maxchange)+")"+"\n")
    textfile.write("Greatest Decrease in Profits: "+minmonth+" ($"+str(minchange)+")"+"\n") 


        


