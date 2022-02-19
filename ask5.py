#Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες. 
# Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει κείμενο με μόνο πεζά γράμματα (μετατρέπετε τα κεφαλαία σε πεζά) και τον κενό χαρακτήρα (space).
# Αρχικά, χωρείστε αυτό το κείμενο σε λέξεις σύμφωνα με το κενό.
# Στις λέξεις που έχετε υπολογίστε τα ακόλουθα στατιστικά: 
# α) ποιες είναι οι δέκα δημοφιλέστερες λέξεις; 
# Αν κάποιες εμφανίζονται το ίδιο πλήθος και βγαίνουν παραπάνω από δέκα, κρατείστε όποιες νομίζετε εσείς ή στην τύχη.
# β) Ποιοι είναι οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις; 
# γ) Επαναλάβετε το ίδιο για τρία γράμματα.
import string
list_of_values=[]
stri=''
stri2=''
emptylist=[]
every_element=''
list_of_first_two_letters=[]
list_of_10_biggest_keys=[]
list_of_read=[]
dict_of_values={}
dict_of_two_letters={}
dict_of_three_letters={}
list_of_most_two=[]
list_of_first_three_letters=[]
with open ("two_cities_some.txt",'r') as file:
    read=file.read()
read=read.lower()
read=list(read)
list_of_alphabet=list(string.ascii_lowercase)
list_of_alphabet.append(" ")
list_of_alphabet.append("\n")
for j in read:
    if j in list_of_alphabet:
      list_of_read.append(j)
for j in list_of_read:
    stri=stri +str(j)
stri=stri.split()
for j in list_of_read:
    stri2=stri2 +str(j)
stri2=stri2.split()
for j in stri:
  dict_of_values[j]=stri.count(j)
for j in dict_of_values.values():
  list_of_values.append(j)
list_of_values.sort()
rest=len(list_of_values)-10
list_of_10_biggest_values=list_of_values[rest-1:]
for j in dict_of_values.keys():
  if dict_of_values[j] in list_of_10_biggest_values:
    list_of_10_biggest_keys.append(j)
if len(list_of_10_biggest_keys)>10:
  while len(list_of_10_biggest_keys)>10:
    list_of_10_biggest_keys.pop(-1)
for j in list_of_10_biggest_keys:
  print('Λέξη:' +str(j)+','+'Φορές που εμφανίστηκε:'+str(dict_of_values[j])+'\n')
for j in stri2:
  if len(j)>1:
   every_element=every_element+j[0]+j[1]
   list_of_first_two_letters.append(every_element)
   every_element=''
for j in list_of_first_two_letters:
  dict_of_two_letters[j]=list_of_first_two_letters.count(j)
list_of_most_two_letters=list(dict_of_two_letters.values())
list_of_most_two_letters.sort()
for i in dict_of_two_letters.keys():
  mylist=list(dict_of_two_letters.values())
  if mylist.count(dict_of_two_letters[i])>1 and dict_of_two_letters[i] in list_of_most_two_letters[-3:]:
    dict_of_two_letters[i]=0
    pass
  elif mylist.count(dict_of_two_letters[i])==1 and dict_of_two_letters[i] in list_of_most_two_letters[-3:]:
    emptylist.append(i)

for i in emptylist:
  print('Combination:'+str(i)+',Number of times it appeared:'+str(dict_of_two_letters[i]))
print('\n')
emptylist.clear()
mylist.clear()
for j in stri2:
  if len(j)>2:
   every_element=every_element+j[0]+j[1]+j[2]
   list_of_first_three_letters.append(every_element)
   every_element=''
for j in list_of_first_three_letters:
  dict_of_three_letters[j]=list_of_first_three_letters.count(j)
list_of_most_three_letters=list(dict_of_three_letters.values())
list_of_most_three_letters.sort()
for i in dict_of_three_letters.keys():
  mylist=list(dict_of_three_letters.values())
  if mylist.count(dict_of_three_letters[i])>1 and dict_of_three_letters[i] in list_of_most_three_letters[-3:]:
    dict_of_two_letters[i]=0
    pass
  elif mylist.count(dict_of_three_letters[i])==1 and dict_of_three_letters[i] in list_of_most_three_letters[-3:]:
    emptylist.append(i)
for i in emptylist:
  print('Combination:'+str(i)+',Number of times it appeared:'+str(dict_of_three_letters[i]))



 



 

  












      


   




   




   
