from random import shuffle
import os
import time
#K1:mikra kapakia
#K2:mesaia kapakia
#k3:megala kapakia
os.system('cls||clear')
start_time = time.time()
sum1=0
counter=0
for t in range(0,100):
    dict_of_kapakia={}
    for j in range(1,4):
        dict_of_kapakia['K'+str(j)]=j

    
    list_of_kapakia=[]
    list_of_squares=[[[''],[''],['']],[[''],[''],['']],[[''],[''],['']]]
    list_of_steps=[]
    for i in range(0,9):
        list_of_kapakia.append('K1')
        list_of_kapakia.append('K2')
        list_of_kapakia.append('K3')
    shuffle(list_of_kapakia)
    index=0
    bool_of_break=False
    bool_of_some_break=False
    while bool_of_break==False:
        for j in list_of_kapakia:

            bool_of_some_break=False
            if  bool_of_break==False:
        
             for i in range(0,3):
                    if bool_of_some_break==False:


                        for x in range(0,3):

                            if  list_of_squares[i][x][-1]=='':
                                list_of_squares[i][x].append(j)
                                list_of_steps.append('step')
                                list_of_kapakia.pop(list_of_kapakia.index(j))
                                bool_of_some_break=True
                                break
                            elif list_of_squares[i][x][-1]!='' and dict_of_kapakia[j]>dict_of_kapakia[list_of_squares[i][x][-1]]:
                                list_of_squares[i][x].append(j)
                                list_of_steps.append('step')
                                list_of_kapakia.pop(list_of_kapakia.index(j))
                                bool_of_some_break=True
                                break
                            #orizontia
                            if list_of_squares[i][0][-1]==list_of_squares[i][1][-1]==list_of_squares[i][2][-1] and list_of_squares[i][0][-1]!='':
                                index=index+1
                                bool_of_break=True
                                break
                            #katheta 
                            elif list_of_squares[0][i][-1]==list_of_squares[1][i][-1]==list_of_squares[2][i][-1] and list_of_squares[0][i][-1]!='':
                                index=index+1
                                bool_of_break=True
                                break
                            #prwth diagwinios
                            elif list_of_squares[0][0][-1]==list_of_squares[1][1][-1]==list_of_squares[2][2][-1] and list_of_squares[0][0][-1]!='':
                                index=index+1
                                bool_of_break=True
                                break
                            #deuterh diagwnios
                            elif list_of_squares[0][2][-1]==list_of_squares[1][1][-1]==list_of_squares[2][0][-1] and list_of_squares[0][2][-1]!='':
                                index=index+1
                                bool_of_break=True
                                break
                            #se aujanomeno megethos
                            #orizontia
                            elif list_of_squares[i][0][-1]=='K1' and list_of_squares[i][1][-1]=='K2' and list_of_squares[i][2][-1]=='K3':
                                index=index+1
                                bool_of_break=True
                                break
                            #katheta
                            elif list_of_squares[0][i][-1]=='K1' and list_of_squares[1][i][-1]=='K2' and list_of_squares[2][i][-1]=='K3':
                                
                                index=index+1
                             
                                bool_of_break=True
                                break
                            # prwth diagwnios
                            elif list_of_squares[0][2][-1]=='K1' and list_of_squares[1][1][-1]=='K2' and list_of_squares[2][0][-1]=='K3':
                                index=index+1
                                bool_of_break=True
                                break
                            elif list_of_squares[0][0][-1]=='K1' and list_of_squares[1][1][-1]=='K2' and list_of_squares[2][2][-1]=='K3':
                                index=index+1
                                bool_of_break=True
                                break
                    else:
                        break
        sum1=sum1+len(list_of_steps)
        counter=counter+1
result=sum1/counter
print('Σε '+ str(100) + ' επαναλήψεις, ο αλγόριθμος έλυσε το παιχνίδι σε :'+str(result) +' κατά μέσο όρο βήματα')
print("--- %s seconds ---" % (time.time() - start_time)) 
 
         
                      

            
                   

  
 





                        
                    
                    
                    



                    

                          
                      

        

           
                
         

                        

