import numpy as np
import random
BRAKE = 0
ACCELERATE = 1
LEFT5 = 2
RIGHT5 = 3
name = "c3po_Louis_Deseure"
epsilon = 0.0
def setup():
    global name
    print (name, "driver setup..")

    return 0
def simplify_d4d5(d):
    if (d in range(0, 40)):
        d = 0
        return d
    if (d in range(40, 60)):
        d = 1
        return d
    if (d in range(60, 80)):
        d = 2
        return d
    else:
        d = 3
        return d


def simplify_d2d3(d):
    if (d in range(0, 100)):
        d = 0
        return d
    if (d in range(100, 200)):
        d = 1
        return d
    if (d in range(200, 300)):
        d = 2
        return d
    else:
        d = 3
        return d


def simplify_d1(d):
    if (d in range(0, 150)):
        d = 0
        return d
    if (d in range(150, 250)):
        d = 1
        return d
    if (d in range(250, 400)):
        d = 2
        return d
    else:
        d = 3
        return d

def simplified(d1, d2, d3, d4, d5):
    d1 = simplify_d1(d1)
    d2 = simplify_d2d3(d2)
    d3 = simplify_d2d3(d3)
    d4 = simplify_d4d5(d4)
    d5 = simplify_d4d5(d5)
    indice = (d1 * (4 ** 4)) + (d2 * (4 ** 3)) + (d3 * (4 ** 2)) + (d4 * (4 ** 1)) + (d5 * (4 ** 0))
    return indice

def drive(d1, d2, d3, d4, d5,velocity,acceleration):
    tab = np.load('New_Qtable_Louis_Deseure2.npy')
    #tab = np.zeros(((1024,3)))
    tab2 = tab[simplified(d1, d2, d3, d4, d5)]
    choice = np.argmax(tab2)+1

    if random.uniform(0, 1) < epsilon:
        choice = random.randint(1,3)

    if (velocity >= 6):
        choice = BRAKE
    elif (velocity <= 2):
        choice = ACCELERATE

    return choice