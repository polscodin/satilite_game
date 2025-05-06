amount = int(input("how many sats do you want? :"))
print("\n\n")
import pgzrun
import random
def ph ():
    print("placeholder")

ifarrow = True
    
WIDTH = 800
HEIGHT = 450
satilitelist = []
for i in range (amount):
    satilite = Actor ("satellite")# type: ignore
    satilite.x = random.randint(50,WIDTH -50)
    satilite.y = random.randint(50,HEIGHT -50)
    satilitelist.append(satilite)


def draw():
    number = int(1)
    screen.blit("spacebackground",(0,-25)) # type: ignore
    for item in satilitelist:
        item.draw()
        screen.draw.text(str(number),(item.x,item.y+20))
        number+=1
    #end

pgzrun.go()