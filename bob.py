s=raw_input("please input a string:")
count=0
start=0
end=len(s)
while s.find('bob',start,end)!=-1:
    start=s.find('bob',start,end)+2
    count+=1
print("Number of vowels: "+str(count))