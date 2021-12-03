import random as r
import array as A
Maxlen =int(input())
if(Maxlen<5):
    print("INVALID")

else:
    a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    b = ["A","B","C","D","E","F","G","H","I","J",'K',"L",'M',"N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    c=["%","@","!","$","*","#","+","-","|","^"]
    d= ["1","2","3","4","5","6","7","8","9","0"]
    rand_temp = a+b+c+d

    r_a = r.choice(a)
    r_b = r.choice(b)
    r_c = r.choice(c)
    r_d = r.choice(d)

    q= r_a+r_b+r_c+r_d

    for x in range(Maxlen-4):
        q=q+r.choice(rand_temp)
        q_l=A.array("u",q)
        r.shuffle(q_l)

    password=""
    for i in q_l:
        password=password+i

    print(password)


    