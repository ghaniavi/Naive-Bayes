import csv
 
with open('TrainsetTugas1ML.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    next(csvReader)
    arr = []
    for row in csvReader:
       arr.append((row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
       
with open('TestsetTugas1ML.csv') as csvDataFile:
    csvReader1 = csv.reader(csvDataFile)
    next(csvReader1)
    arr1 = []
    for row in csvReader1:
       arr1.append((row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

   
       
def prob_kls():
    tdk,ya=0,0
    for row in arr:
            if (row[7] == '>50K'):
                ya += 1
            else :
                tdk += 1
         
    prob_ya = ya/ya+tdk
    prob_tdk = tdk/ya+tdk
    return prob_ya,prob_tdk,ya,tdk
        
def prob_atribut(ya,tdk):
        old_ya = 0
        young_ya = 0
        adult_ya = 0
        old_tdk = 0
        young_tdk = 0
        adult_tdk = 0
        Private_ya = 0
        Self_ya = 0
        Local_gov_ya = 0
        Private_tdk = 0 
        Self_tdk = 0
        Local_gov_tdk = 0
        Some_college_ya = 0
        Bachelors_ya = 0
        HS_grad_ya = 0
        Some_college_tdk = 0
        Bachelors_tdk = 0
        HS_grad_tdk = 0
        Married_ya = 0
        never_married_ya = 0
        Divorced_ya = 0
        Married_tdk = 0
        Never_married_tdk = 0
        Divorced_tdk = 0
        specialty_ya = 0
        Never_ya = 0
        managerial_ya = 0
        specialty_tdk = 0
        Never_tdk = 0
        managerial_tdk = 0
        Husband_ya = 0
        Not_ya = 0
        child_ya = 0
        Husband_tdk = 0
        Not_tdk = 0
        child_tdk = 0
        normal_ya = 0
        many_ya = 0
        low_ya = 0
        normal_tdk = 0
        many_tdk = 0
        low_tdk = 0
        for row2 in arr:
            for row in row2:
                if ((row == 'old') and (row2[7] == '>50K')):
                    old_ya += 1
                elif ((row == 'young') and (row2[7] == '>50K')):
                    young_ya +=1
                elif ((row == 'adult') and (row2[7] == '>50K')):
                    adult_ya += 1
                elif ((row == 'old') and (row2[7] == '<=50K')):
                    old_tdk += 1
                elif ((row == 'young') and (row2[7] == '<=50K')):
                    young_tdk +=1
                elif ((row == 'adult') and (row2[7] == '<=50K')):
                    adult_tdk += 1
                    
                elif ((row == 'Private') and (row2[7] == '>50K')):
                    Private_ya += 1
                elif ((row == 'Self-emp-not-inc') and (row2[7] == '>50K')):
                    Self_ya +=1
                elif ((row == 'Local-gov') and (row2[7] == '>50K')):
                    Local_gov_ya += 1
                elif ((row == 'Private') and (row2[7] == '<=50K')):
                    Private_tdk += 1
                elif ((row == 'Self-emp-not-inc') and (row2[7] == '<=50K')):
                    Self_tdk +=1
                elif ((row == 'Local-gov') and (row2[7] == '<=50K')):
                    Local_gov_tdk += 1

                elif ((row == 'Some-college') and (row2[7] == '>50K')):
                    Some_college_ya += 1
                elif ((row == 'Bachelors') and (row2[7] == '>50K')):
                    Bachelors_ya +=1
                elif ((row == 'HS-grad') and (row2[7] == '>50K')):
                    HS_grad_ya += 1
                elif ((row == 'Some-college') and (row2[7] == '<=50K')):
                    Some_college_tdk += 1
                elif ((row == 'Bachelors') and (row2[7] == '<=50K')):
                    Bachelors_tdk +=1
                elif ((row == 'HS-grad') and (row2[7] == '<=50K')):
                    HS_grad_tdk += 1

                elif ((row == 'Married-civ-spouse') and (row2[7] == '>50K')):
                    Married_ya += 1
                elif ((row == 'Never-married') and (row2[7] == '>50K')):
                    never_married_ya +=1
                elif ((row == 'Divorced') and (row2[7] == '>50K')):
                    Divorced_ya += 1
                elif ((row == 'Married-civ-spouse') and (row2[7] == '<=50K')):
                    Married_tdk += 1
                elif ((row == 'Never-married') and (row2[7] == '<=50K')):
                    Never_married_tdk +=1
                elif ((row == 'Divorced') and (row2[7] == '<=50K')):
                    Divorced_tdk += 1

                elif ((row == 'Prof-specialty') and (row2[7] == '>50K')):
                    specialty_ya += 1
                elif ((row == 'Never-married') and (row2[7] == '>50K')):
                    Never_ya +=1
                elif ((row == 'Exec-managerial') and (row2[7] == '>50K')):
                   managerial_ya += 1
                elif ((row == 'Prof-specialty') and (row2[7] == '<=50K')):
                    specialty_tdk += 1
                elif ((row == 'Never-married') and (row2[7] == '<=50K')):
                    Never_tdk +=1
                elif ((row == 'Exec-managerial') and (row2[7] == '<=50K')):
                   managerial_tdk += 1

                elif ((row == 'Husband') and (row2[7] == '>50K')):
                    Husband_ya += 1
                elif ((row == 'Not-in-family') and (row2[7] == '>50K')):
                    Not_ya +=1
                elif ((row == 'Own-child') and (row2[7] == '>50K')):
                    child_ya += 1
                elif ((row == 'Husband') and (row2[7] == '<=50K')):
                    Husband_tdk += 1
                elif ((row == 'Not-in-family') and (row2[7] == '<=50K')):
                    Not_tdk +=1
                elif ((row == 'Own-child') and (row2[7] == '<=50K')):
                    child_tdk += 1
                
                elif ((row == 'normal') and (row2[7] == '>50K')):
                    normal_ya += 1
                elif ((row == 'many') and (row2[7] == '>50K')):
                    many_ya +=1
                elif ((row == 'low') and (row2[7] == '>50K')):
                    low_ya += 1
                elif ((row == 'normal') and (row2[7] == '<=50K')):
                    normal_tdk += 1
                elif ((row == 'many') and (row2[7] == '<=50K')):
                    many_tdk +=1
                elif ((row == 'low') and (row2[7] == '<=50K')):
                    low_tdk += 1
                    
        temp.append(('old',old_ya / ya,old_tdk/tdk))
        temp.append(('young',young_ya / ya,young_tdk/tdk))
        temp.append(('adult',adult_ya / ya,adult_tdk/tdk))
        temp.append(('Private',Private_ya / ya,Private_tdk / tdk))
        temp.append(('Self-emp-not-inc',Self_ya / ya,Self_tdk / tdk))
        temp.append(('Local_gov',Local_gov_ya / ya,Local_gov_tdk / tdk))
        temp.append(('Some-college',Some_college_ya / ya,Some_college_tdk / tdk))
        temp.append(('Bachelors',Bachelors_ya / ya,Bachelors_tdk / tdk))        
        temp.append(('HS-grad',HS_grad_ya / ya,HS_grad_tdk / tdk))
        temp.append(('Married-civ-spouse',Married_ya / ya,Married_tdk / tdk))
        temp.append(('Never-married',never_married_ya / ya,Never_married_tdk / tdk))
        temp.append(('Divorced',Divorced_ya / ya,Divorced_tdk / tdk))
        temp.append(('Prof-specialty',specialty_ya / ya,specialty_tdk / tdk))
        temp.append(('Never-married',Never_ya / ya,Never_tdk / tdk))
        temp.append(('Exec-managerial',managerial_ya / ya,managerial_tdk / tdk))
        temp.append(('Husband',Husband_ya / ya,Husband_tdk / tdk))
        temp.append(('Not-in-family',Not_ya / ya,Not_tdk / tdk))
        temp.append(('Own-child',child_ya / ya,child_tdk / tdk))
        temp.append(('normal',normal_ya / ya,normal_tdk / tdk))
        temp.append(('many',many_ya / ya,many_tdk / tdk))
        temp.append(('low',low_ya / ya,low_tdk / tdk))
        
def hitung():
   for row in arr1:
      for row2 in temp:
         lbh_bsr,lbh_kcl = 1.0,1.0
         for i in range(7):
            if (row2[0] == row[i]):
               lbh_bsr = lbh_bsr * row2[1]
               lbh_kcl = lbh_kcl * row2[2]
               
         hsl_semua_bsr_ya = lbh_bsr * prob_ya
         hsl_semua_kcl_tdk = lbh_kcl * prob_tdk
         
      final(hsl_semua_bsr_ya,hsl_semua_kcl_tdk)


def final(hsl_semua_bsr_ya,hsl_semua_kcl_tdk):
   
   if (hsl_semua_bsr_ya > hsl_semua_kcl_tdk):
      temp1.append(">50K")
   else :
      temp1.append("<=50K")
      
prob_ya,prob_tdk,ya,tdk = prob_kls()
temp,temp1 = [],[]
prob_atribut(ya,tdk)
hitung()
print(temp1)
#a = 0
#j = 0
#for i in arr:
#   print(i[7])
#   if (i[7] == temp1[j]):
#      a+=1
#b = (a/160) * 100
#print(b)

w = open('TebakanTugas1ML.csv ', 'w')
writer = csv.writer(w)
writer.writerow('class')
for r in temp1:
   writer.writerow((str(r)))
w.close()

