def get_sum(start, end):
    sum=0
    for i in range(start, end+1):
        sum=sum+i
    return sum
print(get_sum(1, 10))


start=int(input("시작값을 입력하시오: "))
end=int(input("끝값을 입력하시오: "))
baesu=int(input("배수를 입력하시오: "))
def baesu_sum(start,end,baesu):
    sum=0
    i=start
    while i <=end:
        if i%baesu==0:
            sum=sum+i
        i=i+1
    return sum
print("합계", baesu_sum(start, end, baesu))

import turtle as t
t.shape("turtle")
def square(length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
t.up()
t.goto(-200,0)
t.down()
square(100)

t.up()
t.goto(0,0)
t.down()
square(100)

t.up()
t.goto(200,0)
t.down()
square(100)
    
