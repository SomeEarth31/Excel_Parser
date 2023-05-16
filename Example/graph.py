import matplotlib.pyplot as plt
import numpy as np

# P.B: 22-31, G.B: 32-39, W.B: 40-47, H.B: 69-86, M.B: 87-117
# All A: Above +100 and then -4

#     data[0][i]=(len(x), np.average(x), np.std(x)) #all patients
#     data[1][i]=(len(a), np.average(a), np.std(a)) #female patients
#     data[2][i]=(len(c), np.average(c), np.std(c)) #male patients
#     data[3][i]=(len(y), np.average(y), np.std(y)) #all healthy
#     data[4][i]=(len(b), np.average(b), np.std(b)) #female healty
#     data[5][i]=(len(d), np.average(d), np.std(d)) #male healthy

def Graphs(data, paired_test, data2, paired_test2):
#------------ Graph One ----------------------#
    x_1=[]
    x_2=[] 
    er_x_1=[]
    er_x_2=[]
    num1=[]
    num2=[]
    for i in [31, 39, 46, 86, 117]:
        x_1.append(data[0][i-22][1])
        er_x_1.append(data[0][i-22][2])
        x_2.append(data[0][i-22+100-4][1])
        er_x_2.append(data[0][i-22+100-4][2])
        num1.append(data[0][i-22][0])
        num2.append(data[0][i-22+100-4][0])

    axis=['PHQ-9', 'GAD-7', 'Well Being', 'HDRS', 'MMSE']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(11,9))
    pps=plt.bar(x_pos, x_1, yerr=er_x_1, color='red', width=0.4, label='Day One', capsize=10)
    pps2=plt.bar(x_pos+0.4, x_2, yerr=er_x_2, color='royalblue', width=0.4, label='After 30 days', capsize=10)
    plt.ylabel('Average Scores')
    plt.xlabel('Tests')
    plt.xticks(x_pos+0.2, axis)
    plt.title('Comparison of Patient Data(Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    plt.savefig('graph1.png')
    #plt.show()

#------------ Graphs Two and Three ----------------------#
    x_1.clear()
    x_2.clear() 
    er_x_1.clear()
    er_x_2.clear()
    num1.clear()
    num2.clear()
    y_1=[]
    y_2=[]
    er_y_1=[] 
    er_y_2=[]
    num3=[]
    num4=[]
    for i in [31, 39, 46, 86, 117]:
        x_1.append(data[0][i-22][1])
        er_x_1.append(data[0][i-22][2])
        x_2.append(data[0][i-22+100-4][1])
        er_x_2.append(data[0][i-22+100-4][2])
        num1.append(data[0][i-22][0])
        num2.append(data[0][i-22+100-4][0])
        
        y_1.append(data[3][i-22][1])
        er_y_1.append(data[3][i-22][2])
        y_2.append(data[3][i-22+100-4][1])
        er_y_2.append(data[3][i-22+100-4][2])
        num3.append(data[3][i-22][0])
        num4.append(data[3][i-22+100-4][0])

    axis=['PHQ-9', 'GAD-7', 'Well Being', 'HDRS', 'MMSE']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(11,9))
    pps=plt.bar(x_pos, x_1, yerr=er_x_1, color='red', width=0.4, label='Patients', capsize=10)
    pps2=plt.bar(x_pos+0.4, y_1, yerr=er_y_1, color='royalblue', width=0.4, label='Healthy', capsize=10)
    plt.ylabel('Average Scores')
    plt.xlabel('Tests')
    plt.xticks(x_pos+0.2, axis)
    plt.title('Comparison of Healthy vs. Patient Data(Day 1)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num3[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
        
    plt.savefig('graph2.png')
    #plt.show()

    axis=['PHQ-9', 'GAD-7', 'Well Being', 'HDRS', 'MMSE']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(11,9))
    pps=plt.bar(x_pos, x_2, yerr=er_x_2, color='red', width=0.4, label='Patients', capsize=10)
    pps2=plt.bar(x_pos+0.4, y_2, yerr=er_y_2, color='royalblue', width=0.4, label='Healthy', capsize=10)
    plt.ylabel('Average Scores')
    plt.xlabel('Tests')
    plt.xticks(x_pos+0.2, axis)
    plt.title('Comparison of Healthy vs. Patient Data(After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num4[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
        
    plt.savefig('graph3.png')
    #plt.show()

#------------ Graphs Four to Eight ----------------------#
    x_1.clear()
    x_2.clear() 
    er_x_1.clear()
    er_x_2.clear()
    num1.clear()
    num2.clear()
    y_1.clear()
    y_2.clear()
    er_y_1.clear()
    er_y_2.clear()
    num3.clear()
    num4.clear()

    for i in range(22,31):
        x_1.append(data[0][i-22][1])
        er_x_1.append(data[0][i-22][2])
        x_2.append(data[0][i-22+100-4][1])
        er_x_2.append(data[0][i-22+100-4][2])
        num1.append(data[0][i-22][0])
        num2.append(data[0][i-22+100-4][0])

    axis=['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(17,9))
    pps=plt.bar(x_pos, x_1, yerr=er_x_1, color='red', width=0.4, label='Day One', capsize=10)
    pps2=plt.bar(x_pos+0.4, x_2, yerr=er_x_2, color='royalblue', width=0.4, label='After 30 days', capsize=10)
    plt.ylabel('Average Scores')
    plt.xlabel('Question Number')
    plt.xticks(x_pos+0.2, axis)
    plt.title('Questionwise Comparison of PHQ Scores(Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0.5),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0.5),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    plt.savefig('graph4.png')
    #plt.show()

    x_1.clear()
    x_2.clear() 
    er_x_1.clear()
    er_x_2.clear()
    num1.clear()
    num2.clear()
    for i in range(32,39):
        x_1.append(data[0][i-22][1])
        er_x_1.append(data[0][i-22][2])
        x_2.append(data[0][i-22+100-4][1])
        er_x_2.append(data[0][i-22+100-4][2])
        num1.append(data[0][i-22][0])
        num2.append(data[0][i-22+100-4][0])

    axis=['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(15,9))
    pps=plt.bar(x_pos, x_1, yerr=er_x_1, color='red', width=0.4, label='Day One', capsize=10)
    pps2=plt.bar(x_pos+0.4, x_2, yerr=er_x_2, color='royalblue', width=0.4, label='After 30 days', capsize=10)
    plt.ylabel('Average Scores')
    plt.xlabel('Question Number')
    plt.xticks(x_pos+0.2, axis)
    plt.title('Questionwise Comparison of GAD Scores(Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0.5),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0.5),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    plt.savefig('graph5.png')
    #plt.show()

    x_1.clear()
    x_2.clear() 
    er_x_1.clear()
    er_x_2.clear()
    num1.clear()
    num2.clear()

    for i in range(40,47):
        x_1.append(data[0][i-22][1])
        er_x_1.append(data[0][i-22][2])
        x_2.append(data[0][i-22+100-4][1])
        er_x_2.append(data[0][i-22+100-4][2])
        num1.append(data[0][i-22][0])
        num2.append(data[0][i-22+100-4][0])

    axis=['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(15,9))
    pps=plt.bar(x_pos, x_1, yerr=er_x_1, color='red', width=0.4, label='Day One', capsize=10)
    pps2=plt.bar(x_pos+0.4, x_2, yerr=er_x_2, color='royalblue', width=0.4, label='After 30 days', capsize=10)
    plt.ylabel('Average Scores')
    plt.xlabel('Question Number')
    plt.xticks(x_pos+0.2, axis)
    plt.title('Questionwise Comparison of Well Being Scores(Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0.5),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0.5),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
    
    plt.savefig('graph6.png')
    #plt.show()

    x_1.clear()
    x_2.clear() 
    er_x_1.clear()
    er_x_2.clear()
    num1.clear()
    num2.clear()

    for i in range(69,86):
        x_1.append(data[0][i-22][1])
        er_x_1.append(data[0][i-22][2])
        x_2.append(data[0][i-22+100-4][1])
        er_x_2.append(data[0][i-22+100-4][2])
        num1.append(data[0][i-22][0])
        num2.append(data[0][i-22+100-4][0])

    axis=['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 
          'Q13', 'Q14','Q15', 'Q16', 'Q17']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(17,9))
    pps=plt.bar(x_pos, x_1, yerr=er_x_1, color='red', width=0.4, label='Day One', capsize=10)
    pps2=plt.bar(x_pos+0.4, x_2, yerr=er_x_2, color='royalblue', width=0.4, label='After 30 days', capsize=10)
    plt.ylabel('Average Scores')
    plt.xlabel('Question Number')
    plt.xticks(x_pos+0.2, axis)
    plt.title('Questionwise Comparison of HDRS Scores(Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 1)),
            xy=(p.get_x() + p.get_width() / 2, 0.5),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 1)),
            xy=(p.get_x() + p.get_width() / 2, 0.5),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
    
    plt.savefig('graph7.png')
    #plt.show()

    x_1.clear()
    x_2.clear() 
    er_x_1.clear()
    er_x_2.clear()
    num1.clear()
    num2.clear()

    for i in range(87,117):
        x_1.append(data[0][i-22][1])
        er_x_1.append(data[0][i-22][2])
        x_2.append(data[0][i-22+100-4][1])
        er_x_2.append(data[0][i-22+100-4][2])
        num1.append(data[0][i-22][0])
        num2.append(data[0][i-22+100-4][0])

    axis=['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 
          'Q13', 'Q14','Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20', 'Q21', 'Q22',
          'Q23', 'Q24', 'Q25', 'Q26', 'Q27', 'Q28', 'Q29', 'Q30']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(25,9))
    pps=plt.bar(x_pos, x_1, yerr=er_x_1, color='red', width=0.4, label='Day One', capsize=10)
    pps2=plt.bar(x_pos+0.4, x_2, yerr=er_x_2, color='royalblue', width=0.4, label='After 30 days', capsize=10)
    plt.ylabel('Average Scores')
    plt.xlabel('Question Number')
    plt.xticks(x_pos+0.2, axis)
    plt.title('Questionwise Comparison of MMSE Scores(Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 1)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 3), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 1)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 3), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
    
    plt.savefig('graph8.png')
    #plt.show()

    #------------ Graph Nine ----------------------#
    x_1.clear()
    x_2.clear() 
    er_x_1.clear()
    er_x_2.clear()
    num1.clear()
    num2.clear()
    y_1.clear()
    y_2.clear()
    er_y_1.clear()
    er_y_2.clear()
    num3.clear()
    num4.clear()

    for i in [31, 39, 46, 86, 117]:
        x_1.append(data[2][i-22][1])
        er_x_1.append(data[2][i-22][2])
        x_2.append(data[2][i-22+100-4][1])
        er_x_2.append(data[2][i-22+100-4][2])
        num1.append(data[2][i-22][0])
        num2.append(data[2][i-22+100-4][0])
        
        y_1.append(data[1][i-22][1])
        er_y_1.append(data[1][i-22][2])
        y_2.append(data[1][i-22+100-4][1])
        er_y_2.append(data[1][i-22+100-4][2])
        num3.append(data[1][i-22][0])
        num4.append(data[1][i-22+100-4][0])

    axis=['PHQ-9', 'GAD-7', 'Well Being', 'HDRS', 'MMSE']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(17,9))
    pps=plt.bar(x_pos, x_1, yerr=er_x_1, color='royalblue', width=0.2, label=' Male Patients Day One', capsize=10)
    pps2=plt.bar(x_pos+0.2, y_1, yerr=er_y_1, color='purple', width=0.2, label='Female Patients Day 1', capsize=10)
    pps3=plt.bar(x_pos+0.4, x_2, yerr=er_x_2, color='red', width=0.2, label='Male Patients After 30 Days', capsize=10)
    pps4=plt.bar(x_pos+0.6, y_2, yerr=er_y_2, color='orange', width=0.2, label='Female Patients After 30 Days', capsize=10)
    plt.ylabel('Average Scores')
    plt.xlabel('Tests')
    plt.xticks(x_pos+0.2, axis)
    plt.title('Gender Wise Comparison of Patient Data(Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
    
    j=0
    for p in pps3:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num3[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
    
    j=0
    for p in pps4:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num4[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    plt.savefig('graph9.png')
    #$plt.show()

#------------ Graphs Ten and Eleven ----------------------#

    x_1.clear()
    x_2.clear() 
    num1.clear()
    num2.clear()
    y_1.clear()
    y_2.clear()
    num3.clear()
    z_1=[]
    z_2=[]
    for j in range(5):
        x_1.append(paired_test[j][0][1])
        x_2.append(paired_test[j][0][2])
        num1.append(paired_test[j][0][0])

        y_1.append(paired_test[j][1][1])
        y_2.append(paired_test[j][1][2])
        num2.append(paired_test[j][1][0])

        z_1.append(paired_test[j][2][1])
        z_2.append(paired_test[j][2][2])
        num3.append(paired_test[j][2][0])
    

    axis=['PHQ-9', 'GAD-7', 'Well Being', 'HDRS', 'MMSE']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(10,7))
    pps=plt.bar(x_pos, z_2, color='red', width=0.2, label='All Patients')
    pps2=plt.bar(x_pos+0.2, x_2, color='royalblue', width=0.2, label='Female Patients')
    pps3=plt.bar(x_pos+0.4, y_2, color='orange', width=0.2, label='Male Patients')
    plt.ylabel('P-Values')
    plt.xlabel('Tests')
    plt.xticks(x_pos+0.2, axis)
    plt.title('P Value Comparison of Patient Data(Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 3)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 3)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps3:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 3)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num3[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
        
    plt.savefig('graph10.png')
    #plt.show()

    axis=['PHQ-9', 'GAD-7', 'Well Being', 'HDRS', 'MMSE']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(12,7))
    pps=plt.bar(x_pos, z_1, color='red', width=0.2, label='All Patients')
    pps2=plt.bar(x_pos+0.2, x_1, color='royalblue', width=0.2, label='Female Patients')
    pps3=plt.bar(x_pos+0.4, y_1, color='orange', width=0.2, label='Male Patients')
    plt.ylabel('T-Satistic')
    plt.xlabel('Tests')
    plt.xticks(x_pos+0.2, axis)
    plt.title('T-Stat Comparison of Patient Data(Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps3:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num3[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
        
    plt.savefig('graph11.png')
    #plt.show()

#------------ Graphs Twelve and Thirteen ----------------------#
## S: F(0,2) M(6,29) && N: F(3,5) M(30,31) ## <-- Collumns
    x_1.clear()
    x_2.clear() 
    er_x_1.clear()
    er_x_2.clear()
    num1.clear()
    num2.clear()
    y_1.clear()
    y_2.clear()
    er_y_1.clear()
    er_y_2.clear()
    num3.clear()
    num4.clear()

    for i in [31, 39, 46, 86, 117]:
        x_1.append(data2[2][i-22][1])
        er_x_1.append(data2[2][i-22][2])
        x_2.append(data2[2][i-22+100-4][1])
        er_x_2.append(data2[2][i-22+100-4][2])
        num1.append(data2[2][i-22][0])
        num2.append(data2[2][i-22+100-4][0])
        
        y_1.append(data2[3][i-22][1])
        er_y_1.append(data2[3][i-22][2])
        y_2.append(data2[3][i-22+100-4][1])
        er_y_2.append(data2[3][i-22+100-4][2])
        num3.append(data2[3][i-22][0])
        num4.append(data2[3][i-22+100-4][0])

    axis=['PHQ-9', 'GAD-7', 'Well Being', 'HDRS', 'MMSE']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(17,9))
    pps=plt.bar(x_pos, x_1, yerr=er_x_1, color='royalblue', width=0.2, label=' Female Patients Day One', capsize=10)
    pps2=plt.bar(x_pos+0.2, y_1, yerr=er_y_1, color='purple', width=0.2, label='Male Patients Day 1', capsize=10)
    pps3=plt.bar(x_pos+0.4, x_2, yerr=er_x_2, color='red', width=0.2, label='Female Patients After 30 Days', capsize=10)
    pps4=plt.bar(x_pos+0.6, y_2, yerr=er_y_2, color='orange', width=0.2, label='Male Patients After 30 Days', capsize=10)
    plt.ylabel('Average Scores')
    plt.xlabel('Tests')
    plt.xticks(x_pos+0.2, axis)
    plt.title('Gender Wise Comparison of Patient Data with N-Type Medecines (Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num3[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
    
    j=0
    for p in pps3:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
    
    j=0
    for p in pps4:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num4[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    plt.savefig('graph12.png')
    #plt.show()

    x_1.clear()
    x_2.clear() 
    er_x_1.clear()
    er_x_2.clear()
    num1.clear()
    num2.clear()
    y_1.clear()
    y_2.clear()
    er_y_1.clear()
    er_y_2.clear()
    num3.clear()
    num4.clear()

    for i in [31, 39, 46, 86, 117]:
        x_1.append(data2[0][i-22][1])
        er_x_1.append(data2[0][i-22][2])
        x_2.append(data2[0][i-22+100-4][1])
        er_x_2.append(data2[0][i-22+100-4][2])
        num1.append(data2[0][i-22][0])
        num2.append(data2[0][i-22+100-4][0])
        
        y_1.append(data2[1][i-22][1])
        er_y_1.append(data2[1][i-22][2])
        y_2.append(data2[1][i-22+100-4][1])
        er_y_2.append(data2[1][i-22+100-4][2])
        num3.append(data2[1][i-22][0])
        num4.append(data2[1][i-22+100-4][0])

    axis=['PHQ-9', 'GAD-7', 'Well Being', 'HDRS', 'MMSE']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(17,9))
    pps=plt.bar(x_pos, x_1, yerr=er_x_1, color='royalblue', width=0.2, label=' Female Patients Day One', capsize=10)
    pps2=plt.bar(x_pos+0.2, y_1, yerr=er_y_1, color='purple', width=0.2, label='Male Patients Day 1', capsize=10)
    pps3=plt.bar(x_pos+0.4, x_2, yerr=er_x_2, color='red', width=0.2, label='Female Patients After 30 Days', capsize=10)
    pps4=plt.bar(x_pos+0.6, y_2, yerr=er_y_2, color='orange', width=0.2, label='Male Patients After 30 Days', capsize=10)
    plt.ylabel('Average Scores')
    plt.xlabel('Tests')
    plt.xticks(x_pos+0.2, axis)
    plt.title('Gender Wise Comparison of Patient Data with S-Type Medecines (Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num3[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
    
    j=0
    for p in pps3:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
    
    j=0
    for p in pps4:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 1),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num4[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.3),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    plt.savefig('graph13.png')
    #plt.show()

    #------------ Graphs Fourteen and Fifteen ----------------------#

    x_1.clear()
    x_2.clear() 
    num1.clear()
    y_1.clear()
    y_2.clear()
    num2.clear()
    z_1.clear()
    z_2.clear()
    num3.clear()
    l_1=[]
    l_2=[]
    num4.clear()

    for j in range(5):
        x_1.append(paired_test2[j][0][1])
        x_2.append(paired_test2[j][0][2])
        num1.append(paired_test2[j][0][0])

        y_1.append(paired_test2[j][1][1])
        y_2.append(paired_test2[j][1][2])
        num2.append(paired_test2[j][1][0])

        z_1.append(paired_test2[j][2][1])
        z_2.append(paired_test2[j][2][2])
        num3.append(paired_test2[j][2][0])

        l_1.append(paired_test2[j][3][1])
        l_2.append(paired_test2[j][3][2])
        num4.append(paired_test2[j][3][0])
    

    axis=['PHQ-9', 'GAD-7', 'Well Being', 'HDRS', 'MMSE']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(15,11))
    pps=plt.bar(x_pos, x_2, color='red', width=0.2, label='S-Type Medecine (Female Patients)')
    pps2=plt.bar(x_pos+0.2, y_2, color='royalblue', width=0.2, label='S-Type Medecine (Male Patients)')
    pps3=plt.bar(x_pos+0.4, z_2, color='orange', width=0.2, label='N-Type Medecine (Female Patients)')
    pps4=plt.bar(x_pos+0.6, l_2, color='purple', width=0.2, label='N-Type Medecine (Male Patients)')
    plt.ylabel('P-Values')
    plt.xlabel('Tests')
    plt.xticks(x_pos+0.3, axis)
    plt.title('P Value Comparison of Patient Data based on Medecine (Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 3)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 3)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps3:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 3)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num3[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps4:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 3)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num4[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
        
    plt.savefig('graph14.png')
    #plt.show()

    axis=['PHQ-9', 'GAD-7', 'Well Being', 'HDRS', 'MMSE']
    x_pos=np.arange(len(axis))   
    plt.figure(figsize=(12,9))
    pps=plt.bar(x_pos, x_1, color='red', width=0.2, label='S-Type Medecine (Female Patients)')
    pps2=plt.bar(x_pos+0.2, y_1, color='royalblue', width=0.2, label='S-Type Medecine (Male Patients)')
    pps3=plt.bar(x_pos+0.4, z_1, color='orange', width=0.2, label='N-Type Medecine (Female Patients)')
    pps4=plt.bar(x_pos+0.6, l_1, color='purple', width=0.2, label='N-Type Medecine (Male Patients)')
    plt.ylabel('T-Satistic')
    plt.xlabel('Tests')
    plt.xticks(x_pos+0.3, axis)
    plt.title('T-Stat Comparison of Patient Data based on Medecine(Day One vs. After 30 Days)')
    plt.legend()

    j=0
    for p in pps:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num1[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps2:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num2[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1

    j=0
    for p in pps3:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num3[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
    
    j=0
    for p in pps4:
        height = p.get_height()
        plt.annotate('{}'.format(round(height, 2)),
            xy=(p.get_x() + p.get_width() / 2, 0),
            xytext=(0, 20), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        plt.annotate('({})'.format(num4[j]),
            xy=(p.get_x() + p.get_width() / 2, 0.0),
            xytext=(0, 0), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
        j=j+1
        
    plt.savefig('graph15.png')
    #plt.show()