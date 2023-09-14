def sum_odd_numbers():
    sum=0
    T = int(input())
    list=[]
    for i in range(T):
        numbers = int(input())
        list.append(numbers)
    for x in list:
        if x%2!=0:
          sum+=x
    print(sum)
sum_odd_numbers()