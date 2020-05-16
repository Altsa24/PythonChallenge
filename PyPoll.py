import os
import csv
#se pone el camino para jalar el earchivo
homework = os.path.join("Resources","election_data.csv")
#se asignan variables
file = open("election_data.csv")
total_votes = 0
candidates = []
candidate_vote_count = []
#calculate the total number of candidates listed in the csv file
with open(homework) as csvfile:
    #se lee el encabezado
    csvreader = csv.reader(csvfile, delimiter = ",")
    #se brinca el encabezadp
    next(csvreader, None)
    #se hace el total de lineas para saber el total de votos
    for row in csvreader:
    
        total_votes += 1

        candidate_in= (row[2]) 
        #sumar votos a cada candidato que ya este en la lista
        if candidate_in in candidates:
            candidate_index = candidates.index(candidate_in)
            candidate_vote_count[candidate_index] +=  1
        else:
            #agregar candidatos que no esten en la lista y sumar primer voto
            candidates.append(candidate_in)
            candidate_vote_count.append(1)

       

#definir variables
pct = []
max_votes = candidate_vote_count[0]
max_index = 0


for x in range(len(candidates)):
    #calcular porcntahte de cada candidato "x" es la cantidad de candidatos encontrado
    vote_pct = round(candidate_vote_count[x]/total_votes*100, 2)
    pct.append(vote_pct)
    #determinar quien tiene mas votos
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x
#definir ganador
election_winner = candidates[max_index] 
#impresiones  en terminal
print('------------------------------------------------------')
print('|                  Election Results                  |')
print('------------------------------------------------------')
print(f'Total Votes: {total_votes}')
print('------------------------------------------------------')
for x in range(len(candidates)):
    print(f'{candidates[x]} : {pct[x]}% ({candidate_vote_count[x]})')
print('-------------------------------------------------------')
print(f'Election winner: {election_winner}')
print('-------------------------------------------------------')
#archiv txt
output_file = os.path.join("Resources","Poll_Analysis_Summary.txt")

with open(output_file,"w") as file:

    file.write('------------------------------------------------------\n')
    file.write('|                  Election Results                  |\n')
    file.write('------------------------------------------------------\n')
    file.write(f'Total Votes: {total_votes}\n')
    file.write('------------------------------------------------------\n')
    for x in range(len(candidates)):
        file.write(f'{candidates[x]} : {pct[x]}% ({candidate_vote_count[x]})\n')
    file.write('-----------------------------------------------------\n')
    file.write(f'Election winner: {election_winner}\n')
    file.write('-----------------------------------------------------\n')
    file.write("---END OF REPORT---")
