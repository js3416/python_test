f = open("salary.txt", "r")
lines = f.readlines()
i=0
salary=[]
value =[]
totalSal=0
totalVal=0
avgSal=0
avgVal=0
for line in lines:
    nStart = line.find('임금 (')+4
    nEnd = line.find('만원')
    salary.append(line[nStart:nEnd])
    #salary[i] = line[nStart:nEnd]
    salary[i] = salary[i].replace(',', '')
    print (int(salary[i]))
    nStart = line.find('전망 (')+4
    nEnd = line.find('%')
    
    value.append(line[nStart:nEnd])
    print (float(value[i]))
    totalSal += int(salary[i])
    totalVal += float(value[i])
    i += 1


avrSalary = totalSal/(i)
avgVal = totalVal/(i)

print("salary total = ", totalSal, "salary avg = ", avrSalary) 
print("value total = ", totalVal, "val avg = ", avgVal)
    



