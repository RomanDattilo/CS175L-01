#CS175L

#Roman Dattilo

#restaurant
on_go='yes'
while on_go == 'yes':
    

    vegetarian=False
    vegan=False
    gluten_free=False

    answer1=(input("Are any of your friends vegatarian? "))
    if answer1=='yes':
        vegetarian=True

    answer2=(input("Are any of your friends vegan? "))
    if answer2=='yes':
        vegan=True

    answer3=(input("Are any of your friends gluten-free? "))
    if answer3=='yes':
        gluten_free=True


    print("Here are your restaurant choices: ")

    if vegetarian==False and vegan==False and gluten_free==False:
        print("Joe's Gourmet Burgers'")
        print("Mama's Fine Italian'")
        print("Main Street Pizza")
        print("Corner Cafe")
        print("Chef's Kitchen")

    if vegetarian==True and vegan==False and gluten_free==False:
        print("Mama's Fine Italian'")
        print("Main Street Pizza")
        print("Corner Cafe")
        print("Chef's Kitchen")

    
    if vegetarian==False and vegan==False and gluten_free==True:
        print("Main Street Pizza")
        print("Corner Cafe")
        print("Chef's Kitchen")

    

    if vegetarian==True and vegan==False and gluten_free==True:
        print("Main Street Pizza")
        print("Corner Cafe")
        print("Chef's Kitchen")
    else:
        print("Corner Cafe")
        print("Chef's Kitchen")

    on_go= input("If you want to keep going answer yes: ")
     
    

        
        


    




