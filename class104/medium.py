import csv
with open("height-weight.csv",newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    number=filedata[i][1]
    newdata.append(float(number))
m=len(newdata)
newdata.sort()
if m % 2==0:
    median1=float(newdata[m//2])
    median2=float(newdata[m//-1])
    median=(median1+median2)
else:
    median=newdata[m//2]
print(median)