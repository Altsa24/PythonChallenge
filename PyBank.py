#se importan las funcions os y csv
import os 
import csv
#se pone el camino para jalar el earchivo
homework = os.path.join("Resources","budget_data.csv")
#se asignan variables
file = open("budget_data.csv")
#crear listados vacioes que se iran llenandp
total_profit = []
monthly_change = []
total_months=[]
#abbrir archivo como csv
with open(homework) as csvfile:
    #leer encabezado
    csvreader = csv.reader(csvfile,delimiter=",")
    #brincarse el encqbezado
    csvheader= next(csvfile,None)
    #crear listados de los meses y prifits
    for row in csvreader:
        total_profit.append(int(row[1]))
        total_months.append(row[0])    
    #calcular el cambio de profits en los meses y gacer el lisatdo
    for i in range(len(total_profit)-1):
        monthly_change.append(total_profit[i+1]-total_profit[i])
        # Take the difference between two months and append to monthly profit change
#determinar el valor de las variables de maximo y miinmo
max_increase = max(monthly_change)
max_decrease= min(monthly_change)
#emparejar el mes porq el calculo se queda en el mes anterior
max_increase_month = monthly_change.index(max(monthly_change)) + 1
max_decrease_month = monthly_change.index(min(monthly_change)) + 1
#calculo del total de proft
total_sum=sum(total_profit)
#total de meses
total_mon=len(total_months)
#total de cambio en los meses
total_monthly_change = sum(monthly_change)
#promedio mensual del cambio el -1 es porq el primer mes no se contempla cambio
average = round(total_monthly_change/(total_mon-1),2)

#imprimir informacion
print("Financial Analysis")
print("----------------------------")
print(f"Total of Months: {total_mon}")
print(f"Total : ${total_sum}")
print(f"Average Change : ${average}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")
    
# salida de archivos
output_file = os.path.join("Resources","Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
# imprimir en archivo txt los datos 
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_mon}\n")
    file.write(f"Total: ${total_sum}\n")
    file.write(f"Average Change: {average}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})\n")