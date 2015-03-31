s=raw_input("please input a string:")
lo=hi=lo_c=hi_c=max_len=0
i=1
le=len(s)
while i<le:
    if s[i]<s[i-1]:
        hi=i-1
        if max_len<hi-lo+1:
            lo_c=lo
            hi_c=hi
            max_len=hi-lo+1
        lo=i
    i+=1
hi=i-1
if max_len<hi-lo+1:
    lo_c=lo
    hi_c=hi
    max_len=hi-lo+1
print("Number of vowels: "+s[lo_c:hi_c+1])