# Me falta crear un versión iterativa, pero que no esté tan limitado y sea tan lento!!
# https://www.geeksforgeeks.org/iterative-tower-of-hanoi/
'''
Iterative Algorithm:

1. Calculate the total number of moves required i.e. "pow(2, n)
   - 1" here n is number of disks.
2. If number of disks (i.e. n) is even then interchange destination
   pole and auxiliary pole.
3. for i = 1 to total number of moves:
     if i%3 == 1:
    legal movement of top disk between source pole and
        destination pole
     if i%3 == 2:
    legal movement top disk between source pole and
        auxiliary pole
     if i%3 == 0:
        legal movement top disk between auxiliary pole
        and destination pole
'''
# https://en.wikipedia.org/wiki/Tower_of_Hanoi#Iterative_solution
