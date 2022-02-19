from random import shuffle
import os
import time
os.system('cls||clear')
start_time = time.time()
sum1=0
counter=0
for t in range(0,99):
    list_of_added_elements=[]
    list_of_elements=[]
    for j in range(0,9):
        list_of_elements.append('R1')
        list_of_elements.append('R2')
        list_of_elements.append('R3')
    shuffle(list_of_elements)
    list_of_squares=[[[],[],[]],[[],[],[]],[[],[],[]]]
    indx=0
    break_out=False
    while len(list_of_elements)>0 and break_out==False  :

        for j in list_of_elements:
            if break_out==False:
                for i in range(0,3):
                    if j not in list_of_squares[i][0]:
                        list_of_squares[i][0].append(j)
                        list_of_added_elements.append('added')
                        list_of_elements.pop(list_of_elements.index(j))
                        
                    elif j in list_of_squares[i][0] and j not in list_of_squares[i][1]:
                        list_of_squares[i][1].append(j)
                        list_of_elements.pop(list_of_elements.index(j))
                        list_of_added_elements.append('added')
                        
                    elif j in list_of_squares[i][1]  and j not in list_of_squares[i][2] :
                        list_of_squares[i][2].append(j)
                        list_of_elements.pop(list_of_elements.index(j))
                        list_of_added_elements.append('added')
                    if j in list_of_squares[i][0] and j in list_of_squares[i][1] and j in list_of_squares[i][2] :
                        break_out=True
                        break
                    elif j in list_of_squares[0][i] and j in list_of_squares[1][i] and j in list_of_squares[2][i] :
                        break_out=True
                        break
                    elif j in list_of_squares[0][0] and j in list_of_squares[1][1] and j in list_of_squares[2][2] :
                        break_out=True
                        break
                    elif j in list_of_squares[0][2] and j in list_of_squares[1][1] and j in list_of_squares[2][0] :
                        break_out=True
                        break
                    elif 'R1' in list_of_squares[0][i] and 'R2' in list_of_squares[1][i] and 'R3' in list_of_squares[2][i] :
                            break_out=True
                            break
                    elif 'R1' in list_of_squares[i][0] and 'R2' in list_of_squares[i][1] and 'R3' in list_of_squares[i][2] :
                            break_out=True
                            break
                    elif 'R1' in list_of_squares[0][0] and 'R2' in list_of_squares[1][1] and 'R3' in list_of_squares[2][2] :
                            break_out=True
                            break
                    elif 'R1' in list_of_squares[0][2] and 'R2' in list_of_squares[1][1] and 'R3' in list_of_squares[2][0] :
                            break_out=True
                            break        
                    elif len(list_of_squares)==0:
                        break_out=True
                        break
            else:
                break
        sum1=sum1+len(list_of_added_elements)
        counter=counter+1
        
result=sum1/counter 
print(result)

maxloopcount = 100
print('Σε '+ str(maxloopcount) + ' επαναλήψεις, ο αλγόριθμος έλυσε το παιχνίδι σε :'+str(result) +' κατά μέσο όρο βήματα')
print("--- %s seconds ---" % (time.time() - start_time)) 
 



       
                






            
       
    



      



                               
                           


                  
                        
