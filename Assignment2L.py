#CS175L

#Roman Dattilo

#restaurant



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

if vegetarian==True and vegan==False and gluten_free==False:
    print("Mama's Fine Italian'")

if vegetarian==True and vegan==False and gluten_free==True:
    print("Main Street")
    print("Pizza Corner Cafe")
    print("Chef's Kitchen")