import tkinter
from tkinter.filedialog import askopenfilename
import openpyxl
import numpy as np
import scipy.stats as stats

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
    return filename

#-------------------------------------------------#

def Sheet_Select(filename):
#Selecting Sheet in Excel Workbook
    sheet_name=input("Enter the sheet name: ")
    sheet=filename[sheet_name]
    return sheet

#-------------------------------------------------#

def Select_Data():
#Selecting Data rom Excel Sheet
    filename=File_Select()
    wb = openpyxl.load_workbook(filename)
    sheet=Sheet_Select(wb)
    cell_start=input("Data Range START point(Ex. C1): ")
    cell_end=input("Data Range END point(Ex. C109): ")
    x = []
    for rowOfCellObjects in sheet[cell_start:cell_end]:
        for cellObj in rowOfCellObjects:
            x.append(cellObj.value)
    filename=None
    return x

#-------------------------------------------------#
#-------------------------------------------------#

def clean_single_data(x):
#removing all empty spaces
    filtered_items = filter(lambda item: item is not None, x)
    return list(filtered_items)

#-------------------------------------------------#

def clean_double_data(x, y):
#cleans pair of data CORRECTLY so that there are no empty spaces
    x_new=[]
    y_new=[]
    x__new=[]
    y__new=[]
    for i in range(0, len(x)):
        if x[i] is not None:
            x_new.append(x[i])
            y_new.append(y[i])

    for i in range(0, len(y_new)):
       if y_new[i] is not None:
           y__new.append(y_new[i])
           x__new.append(x_new[i])

    return x__new, y__new

#-------------------------------------------------#
#-------------------------------------------------#

def mean():
#mean of list
    print("\n")
    print(np.average(clean_single_data(Select_Data())))

#-------------------------------------------------#

def stdev():
#stdev of list, Var(x) is stdev(x) squared.
    print("\n")
    print(np.std(clean_single_data(Select_Data())))

#-------------------------------------------------#

def var():
#Var(x) is stdev(x) squared.
    print("\n")
    print(np.var(Select_Data()))

#-------------------------------------------------#

def single_t():
#Single t-test(cleans data)
    pop_mean=input("What is the population mean: ")
    print("\n")
    print(stats.ttest_1samp(a = clean_single_data(Select_Data()), popmean = pop_mean))

#------------------------------------------------#

def double_t():
#double t-test(cleans data)
    print("\n")
    print(stats.ttest_ind(a= clean_single_data(Select_Data()),
                 b= clean_single_data(Select_Data()),
                equal_var=False))
    
#------------------------------------------------#

def paired_t():
#paired t-test(cleans data together)
    x_new,y_new=clean_double_data(Select_Data(),Select_Data())
    print(stats.ttest_rel(a = x_new,
                b = y_new))
    
#------------------------------------------------#
#-------------------------------------------------#

print("Available Operations:\n1-Mean of Data\n2-Standard Deviation of data")
print("3-Variance of data\n4-Single t-test\n5-Double t-test\n6-Paired t-test\n7-Exit")
i=1
while(i==1):
    a=int(input("What operation do you want to perform: "))
    if a==1:
        mean()
    elif(a==2):
        stdev()
    elif(a==3):
        var()
    elif(a==4):
        single_t()
    elif(a==5):
        double_t()
    elif(a==6):
        paired_t()
    elif(a==7):
        break
    else:
        print("Please select correct option\n")
    
