import pygame


pygame.init()

def chkavail():

    f = open('../data_files/availability.txt', 'r')

    i = 0
    arr = []
    dump = []
    for rows in f:

        arr += rows


    for i in range(12):

        arr[i] = int(arr[2*i])

    return arr




