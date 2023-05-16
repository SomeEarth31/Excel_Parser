#Needs to take input excel file path, and sheet name. 
import pandas as pd
import tkinter
from tkinter.filedialog import askopenfilename
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from graph import Graphs as gr

# File selection function
#-------------------------------------------------#
def File_Select():
#Selecting Excel File# 
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    root.lift()
    filename = askopenfilename()
    #print(filename)
    root.withdraw()
    root.destroy()
    print(filename)
    return filename
#-------------------------------------------------#

def Select_Data(col, a, b):
#Selecting Data from dataframe
    a=df.iloc[a:b, col].to_list()
    #print(a)
    return a

#-------------------------------------------------#

def clean_single_data(a):
#removing all empty spaces
    x = a[np.logical_not(np.isnan(a))]
    return x

#-------------------------------------------------#

def clean_double_data(a, b):
#cleans pair of data CORRECTLY so that there are no empty spaces
    temp_a=a
    temp_b=b

    x = a[np.logical_not(np.isnan(a))]
    y = b[np.logical_not(np.isnan(temp_a))]

    y = a[np.logical_not(np.isnan(b))]
    x = b[np.logical_not(np.isnan(temp_b))]
    
    return x, y

#-------------------------------------------------#

##Stores whole excel sheet in very data frame##

#filename = File_Select()
filename = 'D:/OneDrive - IIT Kanpur/College/Project Things/Prof. Pragrati Subramanium/EEGDATA/DataSet_Old/Old 2(May 2023)/EEG_DATA_Record_Copy.xlsx'
all_sheets = pd.read_excel(filename, sheet_name=None, skiprows=[0])
df=pd.concat(all_sheets, axis=1)

# for l in range(0, len(df.columns)): 
#         print(df.columns[l], l)
# print()

# Indexes going from 22 to 213(required)
#
df.drop(df.columns[[22, 23, 24, 25, 122, 123, 124, 125]], axis=1, inplace=True)
df=df.drop(df.index[range(125,176)])

# for l in range(0, len(df.columns)): 
#         print(df.columns[l], l)
# print()

#Sorts according to patients and gender
df.sort_values(by=[('Patient_Record', 'Gender'),('Patient_Record', 'Patients/\nHealthy'), ('Patient_Record', 'Age')], ascending=[True, False, True], inplace=True)
df.reset_index(drop=True, inplace=True)
#Day of Collection: 22-117; After 30 Days: 118-213


##Method to print values of specific collumns of groups of collumns(with examples)##

# print(df)
# print(df[[('Patient_Record', 'Gender'),('Patient_Record', 'Patients/\nHealthy'), ('Day_of_Collection', 'P.Total Score'), ('30_to_40_Days', 'P.Total Score')]])
# print(df[('Day_of_Collection', 'H.14')].to_markdown())
# print(df[('Patient_Record', 'Patients/\nHealthy')].to_markdown())
# print(df[('30_to_40_Days', 'H.14')].to_markdown())
# print(df[[('Patient_Record', 'Sr.No.'), ('Patient_Record', 'Medecine Group')]].to_markdown())

#-------------------------------------------------#

#Creates secondary lists for averages and std. dev##

# Rows: 0-19(female patients), 20-28(female healthy), 29-83(male patients), 84-124(male healthy)

rows, cols=(6,192)
data = [[0 for i in range(cols)] for j in range(rows)]
for i in range(0, 192): #192
    # print(i+22)
    a=clean_single_data(np.array(df.iloc[0:20, 22+i].to_list()))
    b=clean_single_data(np.array(df.iloc[20:29, 22+i].to_list()))
    c=clean_single_data(np.array(df.iloc[29:84, 22+i].to_list()))
    d=clean_single_data(np.array(df.iloc[84:125, 22+i].to_list()))
    x=np.append(a, c)
    y=np.append(b, d)
    data[0][i]=(len(x), np.average(x), np.std(x)) #all patients
    data[1][i]=(len(a), np.average(a), np.std(a)) #female patients
    data[2][i]=(len(c), np.average(c), np.std(c)) #male patients
    data[3][i]=(len(y), np.average(y), np.std(y)) #all healthy
    data[4][i]=(len(b), np.average(b), np.std(b)) #female healty
    data[5][i]=(len(d), np.average(d), np.std(d)) #male healthy
    # for j in range(6):
    #     print(data[j][i])

#-------------------------------------------------#

#Creates array for pvalues and all
#P(31, 127); G(39, 135); W(47, 143); T(68, 164); H(86, 182); M(117, 213)

rows, cols=(6,3)
paired_test = [[0 for i in range(cols)] for j in range(rows)]
j=0
for i in [31, 39, 47, 86, 117]:
    f=np.array(df.iloc[0:20, i].to_list())
    g=np.array(df.iloc[0:20, 100-4+i].to_list())
    x,y=clean_double_data(f, g)
    a=stats.ttest_rel(x,y)
    paired_test[j][0]=(len(x), -1*a.statistic, a.pvalue)

    h=np.array(df.iloc[29:84, i].to_list())
    k=np.array(df.iloc[29:84, 100-4+i].to_list())
    x,y=clean_double_data(h, k)
    a=stats.ttest_rel(x,y)
    paired_test[j][1]=(len(x), -1*a.statistic, a.pvalue)

    l=np.append(f, h)
    m=np.append(g, k)
    x,y=clean_double_data(l, m)
    a=stats.ttest_rel(x,y)
    paired_test[j][2]=(len(x), -1*a.statistic, a.pvalue)
    j=j+1

j=0



# print(paired_test)

#-------------------------------------------------#\
#Medecine Anlaysis
#collumn number 9, ('Patient_Record', 'Medecine Group')
check_nan=df[('Patient_Record', 'Medecine Group')].isnull()
df2=df
x=[]
for j in range(len(check_nan)):
    if (check_nan[j]==True):
        x.append(j)
df2=df2.drop(df2.index[x])
df2=df2.drop(df2.index[range(6,9)])
df2=df2.drop(df2.index[range(32,37)])
df2.sort_values(by=[('Patient_Record', 'Gender'), ('Patient_Record', 'Medecine Group'),
                    ('Patient_Record', 'Age')], ascending=[True, False, True], inplace=True)
df2.reset_index(drop=True, inplace=True)

#S: F(0,2) M(6,29) N: F(3,5) M(30,31)
# print(df2)


#For analysis: Age: 20-50 
#Collumns(All Patients):- F(0, 5)(6) & M(9, 34)(26) [0 indexd] 
rows, cols=(4,192)
data2 = [[0 for i in range(cols)] for j in range(rows)]
for i in range(0, 192): #192
    # print(i+22)
    a=clean_single_data(np.array(df2.iloc[0:3, 22+i].to_list()))
    b=clean_single_data(np.array(df2.iloc[6:30, 22+i].to_list()))
    c=clean_single_data(np.array(df2.iloc[3:6, 22+i].to_list()))
    d=clean_single_data(np.array(df2.iloc[30:32, 22+i].to_list()))
    data2[0][i]=(len(a), np.average(a), np.std(a)) #s-female
    data2[1][i]=(len(b), np.average(b), np.std(b)) #s- male
    data2[2][i]=(len(c), np.average(c), np.std(c)) #n-female
    data2[3][i]=(len(d), np.average(d), np.std(d)) #n-male
    # print(i, data2[0][i], data2[1][i])


rows, cols=(6,4)
paired_test2 = [[0 for i in range(cols)] for j in range(rows)]
j=0
for i in [31, 39, 47, 86, 117]:
    f=np.array(df2.iloc[0:3, i].to_list())
    g=np.array(df2.iloc[0:3, 100-4+i].to_list())
    x,y=clean_double_data(f, g)
    a=stats.ttest_rel(x,y)
    paired_test2[j][0]=(len(x), -1*a.statistic, a.pvalue)

    h=np.array(df2.iloc[6:30, i].to_list())
    k=np.array(df2.iloc[6:30, 100-4+i].to_list())
    x,y=clean_double_data(h, k)
    a=stats.ttest_rel(x,y)
    paired_test2[j][1]=(len(x), -1*a.statistic, a.pvalue)

    l=np.array(df2.iloc[3:6, i].to_list())
    m=np.array(df2.iloc[3:6, 100-4+i].to_list())
    x,y=clean_double_data(l, m)
    a=stats.ttest_rel(x,y)
    paired_test2[j][2]=(len(x), -1*a.statistic, a.pvalue)

    o=np.array(df2.iloc[30:32, i].to_list())
    q=np.array(df2.iloc[30:32, 100-4+i].to_list())
    x,y=clean_double_data(o, q)
    a=stats.ttest_rel(x,y)
    paired_test2[j][3]=(len(x), -1*a.statistic, a.pvalue)
    j=j+1

#print(paired_test2)
j=0
#-------------------------------------------------#
#Graphs(saves to a folder)
# P.B: 22-31, G.B: 32-39, W.B: 40-46, H.B: 69-86, M.B: 87-117
# All A: Above +100 and then -4
#calls function Graph from graph.py

gr(data, paired_test, data2, paired_test2)

#-------------------------------------------------#


print("-----------------------------------------------------------------------------------------")
print("Available Operations:\n1-Mean of Data\n2-Paired t-test data\n3-New t-test\n4-Print Collumns\n5-Mean of Medecine Data\n6-Paired T-test medecine data\n7-Exit")
i=1
while(i==1):
    a=int(input("What operation do you want to perform: "))

    if a==1:
        print("Enter collumn number(22-213): ")
        a=int(input())-22
        print("Enter data specification:")
        b=int(input())
        print(data[b][a])
        print()

    elif(a==2):
        print("Enter data number: ")
        a=int(input())
        b=int(input())
        print(paired_test[a][b])
        print()

    elif(a==3):
        print("Enter collumn numbers on which to perform a test(22-213): ")
        f=np.array(df.iloc[0:20, int(input())].to_list())
        g=np.array(df.iloc[0:20, int(input())].to_list())
        print("First data set:\n",f)
        print("Second data set:\n",g)
        x,y=clean_double_data(f, g)
        print("Cleaned data sets:", x, y)
        print(stats.ttest_rel(x,y))
        print()

    elif(a==4): 
        print("Here are all the indexes for each collumn:")
        for l in range(0, len(df.columns)): 
            print(df.columns[l], l)
        print()

    elif(a==5):
        print("Enter collumn number(22-213): ")
        a=int(input())-22
        print("Enter data specification:")
        b=int(input())
        print(data2[b][a])
        print()

    elif(a==6):
        print("Enter data number: ")
        a=int(input())
        b=int(input())
        print(paired_test2[a][b])
        print()

    elif(a==7): 
        print("Program Exitted")
        print()
        break
    else:
        print("Please select correct option\n")
        print()
    