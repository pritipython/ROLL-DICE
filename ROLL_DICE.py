'''This is for rolling dice'''
'''roll dice'''
import random as r #Import random Module for Shuffling.
i=[[6,1],[3,4],[5,2]]# i is initial Position of Dice.
print('initial values: ',i)
print(f"""                      back:{i[1][1]}
                +---------------------+
               /                     /|
              /        Top:{i[0][0]}        / |
             /                     /  |
            /                     /   |right:{i[2][1]}
           +---------------------+    |
           |                     |    |
           |                     |    |
    left:{i[2][0]} |                     |    |
           |                     |    +
           |      front:{i[1][0]}        |   /
           |                     |  /
           |                     | /
           +---------------------+
                    bottom:{i[0][1]}
                    
****************Let's Play******************                                       """)
print("\nR-roll right\nL-roll left\nU-roll up\nD-roll down\nQ-quit")
r.shuffle(i)
print(i)
def dice_final():
    """dice() function returns the final position of dice."""
    res = (f"""                      back:{i[1][1]}
                +---------------------+
               /                     /|
              /        Top:{i[0][0]}        / |
             /                     /  |
            /                     /   |right:{i[2][1]}
           +---------------------+    |
           |                     |    |
           |                     |    |
    left:{i[2][0]} |                     |    |
           |                     |    +
           |      front:{i[1][0]}        |   /
           |                     |  /
           |                     | /
           +---------------------+
                    bottom:{i[0][1]}""")
    while True:
        if select=='r':
            i[0][0],i[2][1],i[0][1],i[2][0]=i[2][0],i[0][0],i[2][1],i[0][1]
            return res
        if select=='l':
            i[2][0],i[0][0],i[2][1],i[0][1]=i[0][0],i[2][1],i[0][1],i[2][0]
            return res
        if select=='u':
            i[0][0],i[1][1],i[1][0],i[0][1]=i[1][0],i[0][0],i[0][1],i[1][1]
            return res
        if select=='d':
            i[1][0],i[0][0],i[0][1],i[1][1]=i[0][0],i[1][1],i[1][0],i[0][1]
            return res
def right_roll():
    """This function rotates dice to the Right side"""
    i[0][0],i[2][1],i[0][1],i[2][0]=i[2][0],i[0][0],i[2][1],i[0][1]
    return i
def left_roll():
    """This function rotates dice to the Left side"""
    i[2][0],i[0][0],i[2][1],i[0][1]=i[0][0],i[2][1],i[0][1],i[2][0]
    return i
def up_roll():
    """This function rotates dice to the Up side"""
    i[0][0],i[1][1],i[1][0],i[0][1]=i[1][0],i[0][0],i[0][1],i[1][1]
    return i
def down_roll():
    """This function rotates dice to the Down side"""
    i[1][0],i[0][0],i[0][1],i[1][1]=i[0][0],i[1][1],i[1][0],i[0][1]
    return i
while True:
    select = ((input('pick your move: ').strip()[0]).lower())
    if select == 'r' :
        print(right_roll())
    elif select == 'l':
        print(left_roll())
    elif select == 'u':
        print(up_roll())
    elif select == 'd':
        print(down_roll())
    elif select == 'q':
        print("")
        print("**********Hey!!! This is Your Final Dice**********")
        print()
        print(dice_final())
        print("*******************Thank You*********************")
        break
    else:
        print("This is Invalid move \nPlease Enter R/L/U/D to Rotate or Q to Quit.")
