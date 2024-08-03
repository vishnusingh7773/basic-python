input("what is your name= ")
input ("what is your father name=")
input("what is your mother name=")
input("waht is your brother name=")


firstnumber = int(input("write your 1st number"))
secondnumber= int(input("write your 2nd number"))

operator=input("write your operator")

if operator=="add":
               print(firstnumber+secondnumber)


elif operator=="subs":
                  print(firstnumber-secondnumber)


elif operator=="multi":
                      print(firstnumber*secondnumber) 

elif operator=="div":      
                  print(firstnumber%secondnumber)                



else:
        print("'you are wrong'") 