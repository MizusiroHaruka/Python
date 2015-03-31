print('Please think of a number between 0 and 100!')
lo=0
hi=100
mi=0
e=''
while e != 'c' or lo>hi:           #end at get a correct answer 
    mi=(lo+hi)>>1
    print('Is your secret number '+str(mi)+'?')
    e = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    while e!='h' and e!='l' and e!='c':               #if e is not 'h' or 'l' or 'c',then...
        print('Sorry, I did not understand your input.')     #sorry
        print('Is your secret number '+str(mi)+'?')       #continue query
        e = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if e== 'h':
        hi=mi
    elif e=='l':
        lo=mi
    elif e=='c':
        break                
print('Game over. Your secret number was: '+str(mi))
        