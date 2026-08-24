'''
Write a program to print the following pattern using nested loops (right-angled triangle of stars)
    
    *
   ***
  *****
*********

'''

n =  int (input ("Enter a No."))
for i in range (1,n+1):
    print(" "* (n-i) ,end="" )
    if (i>1):
        print("*" * (i+(i-1)))
    else:
        print("*" * (i))

    i +=1 