def expo_mod(num,e,n):
    #turning the exponent 'e' into binary
    l=[] #a list to store the even numbers that compose the exponent 
    q=e//2
    r=e%2
    l.append(r)
    while (q>=1):
        r=q%2
        l.append(r)
        q=q//2

    for _ in range(len(l)):
        if not (l[_]==0):
            l[_]=2**_

    #removing zero's from the list
    list_lenght=len(l)
    i=0
    while i<list_lenght:      
        if l[i]==0: 
            l.pop(i)
            list_lenght-=1
            i=0
        else:
            i+=1
   
    #calculating modular exponentiation
    i=1
    j=0
    max_list=max(l)
    last=(num**i)%n #for the first iteration
    while i <= max_list:
        if not (i==1):#2nd iteration and above
            last=(last**2)%n
        if i == l[j]:
            l[j]=last
            j+=1
        if i==1:
            i+=1
        else:
            i=i*2
        
    final_result=1 #multiplying results and applying mod 
    for i in l:
            final_result=(final_result*i)%n
    return final_result
        
            

if __name__ == "__main__":
    final=expo_mod(100,233,437)#change the values to your desired values
    print(f"the final result is *{final}*")