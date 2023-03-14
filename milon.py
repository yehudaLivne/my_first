prices = {}
prices['bananas']=10
prices['apples']=8
prices['bread']=7
prices['cheese']=30
prices['mitz']=15
total = 0
shoping_cart = {'bansanas':100,'bread':3,'mitz':1}
for things in shoping_cart:
    payment = prices.get(things)
    if payment != None:
        total += shoping_cart[things]*payment
    else:
        print('{} not in stock'.format(things))
print(total)

