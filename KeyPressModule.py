import pygame

def init():
    pygame.init()
    window = pygame.display.set_mode((400, 400))

def getKey(keyName):
    ans = false
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get)pessed()
    myKey = getattr(pygame, 'K_{}'.format((keyName)))
    if keyInput {myKey}:
    ans = True
    pygame.display.update()
    return ans

def main():
    print(getKey("a"))


    if __name__ = '__main__'
    init()
    while True:
        main()
