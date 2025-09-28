print("Welcome to Python Pizza Delivery!")
print(" ")
print('''                                     ._
                                   ,(  `-.
                                 ,': `.   `.
                               ,` *   `-.   \
                             ,'  ` :+  = `.  `.
                           ,~  (o):  .,   `.  `.
                         ,'  ; :   ,(__) x;`.  ;
                       ,'  :'  itz  ;  ; ; _,-'
                     .'O ; = _' C ; ;'_,_ ;
                   ,;  _;   ` : ;'_,-'   i'
                 ,` `;(_)  0 ; ','       :
               .';6     ; ' ,-'~
             ,' Q  ,& ;',-.'
           ,( :` ; _,-'~  ;
         ,~.`c _','
       .';^_,-' ~
     ,'_;-''
    ,,~
    i'
    :''')
print(" ")

size = input("What size pizza do you want? (S, M, or L) ")
add_pepperoni = input("Do you want pepperoni? (Y or N) ")
extra_cheese = input("Do you want extra cheese? (Y or N) ")

bill = 0

if size == "S" or size == "s":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
elif size == "L" or size == "l":
    bill += 25
else: 
    print("Invalid size")

if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "S" or size == "s":
        bill += 2
    else:
        bill += 3
else:
    print("Invalid choice")


if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1
else:
    print("Invalid choice")


print(f"Your final bill is: ${bill}.")

