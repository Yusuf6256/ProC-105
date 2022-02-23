import csv
import math

with open("data.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data = file_data[0]

#finding mean
def mean(data):
    n=len(data)
    total=0
    
    for x in data:
        total+=int(x)
    
    mean = total/n
    return mean

#squaring and getting the values
square_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2 
    square_list.append(a)

#getting the sum
sum=0
for i in square_list:
    sum = sum+i


#dividing the sum by total values
result = sum/(len(data)-1)

#detting the deviation by takin the sqrt of the result
std_deviation=math.sqrt(result)

print(std_deviation)