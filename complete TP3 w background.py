import pygame
import random
import math

'''
***Citation:
***I am using pygame, which I got fro pygame.org!
1) Sprite: https://www.pngkey.com/maxpic/u2q8i1y3i1q8i1o0/ 
-> used this resource to make the background transparent: https://onlinepngtools.com/create-transparent-png 
2) Pygame Template (main loop): http://blog.lukasperaza.com/getting-started-with-pygame/
3) Pygame Template (main loop & implementation of clock): https://www.youtube.com/watch?v=UdsNBIzsmlI 
4) Pygame Text Blit: https://nerdparadise.com/programming/pygame/part5 
'''

#creates the pygame screen:
pygame.init()
canvas = pygame.display.set_mode((300,400))
pygame.display.set_caption("Term Project 1 - 112 RUN")
#while run = True, the loop will run -> the game will run
run = True

#To implement the background change:
class StartScreen(object):
    def __init__(self):
        self.startX = 300
        self.startY = 150 #0, 150
    
    def draw(self):
        #rectangle:
        titleColor = (253, 253, 150)
        pygame.draw.rect(canvas, titleColor, (0,0, 300, 150))
        #print the text:
        font = pygame.font.SysFont("comicsansms", 72)
        text = font.render("112 RUN", True, (0,0,0))
        canvas.blit(text, (150 - text.get_width()//2, 75.5 - text.get_height()//2))

class EasyLevel(pygame.sprite.Sprite):
    def __init__(self):
        self.margin = 10
        self.buttonX = 200
        self.buttonY = 40
        self.easyButtonCoord = (50, 150 + self.margin, self.buttonX, self.buttonY)
        self.rect = pygame.Rect(50, 150 + self.margin, self.buttonX, self.buttonY)
        self.buttonColor = (240,128,128)
        
    def draw(self): #render this text on to the screen
        pygame.draw.rect(canvas, self.buttonColor, self.easyButtonCoord)
        #print the text:
        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render("EASY", True, (0,0,0))
        topX = 50
        topY = 150 + self.margin
        botX = topX + self.buttonX 
        botY = topY + self.buttonY
        middleX = (topX + botX)//2
        middleY = (topY + botY)//2
        canvas.blit(text, (middleX - text.get_width()//2, middleY - text.get_height()//2))

class MediumLevel(pygame.sprite.Sprite):
    def __init__(self):
        self.margin = 10
        self.buttonX = 200
        self.buttonY = 40
        self.mediumButtonCoord = (50, 150 + self.margin*2 + self.buttonY, self.buttonX, self.buttonY)
        #later used for collision
        self.rect = pygame.Rect(50, 150 + self.margin*2 + self.buttonY, self.buttonX, self.buttonY)
        self.buttonColor = (255,127,80)

    def draw(self):
        pygame.draw.rect(canvas, self.buttonColor, self.mediumButtonCoord)
        #print the text:
        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render("MEDIUM", True, (0,0,0))
        topX = 50
        topY = 150 + self.margin*2 + self.buttonY
        botX = topX + self.buttonX
        botY = topY + self.buttonY
        middleX = (topX + botX)//2
        middleY = (topY + botY)//2
        canvas.blit(text, (middleX - text.get_width()//2, middleY - text.get_height()//2))

class HardLevel(pygame.sprite.Sprite):
    def __init__(self):
        self.margin = 10
        self.buttonX = 200
        self.buttonY = 40
        self.hardButtonCoord = (50, 150 + self.margin*3 + self.buttonY*2, self.buttonX, self.buttonY)
        #later used for collision
        self.rect = pygame.Rect(50, 150 + self.margin*3 + self.buttonY*2, self.buttonX, self.buttonY)
        self.buttonColor = (255,255,102)

    def draw(self):
        pygame.draw.rect(canvas, self.buttonColor, self.hardButtonCoord)
        #print the text:
        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render("HARD", True, (0,0,0))
        topX = 50
        topY = 150 + self.margin*3 + self.buttonY*2
        botX = topX + self.buttonX
        botY = topY + self.buttonY
        middleX = (topX + botX)//2
        middleY = (topY + botY)//2
        canvas.blit(text, (middleX - text.get_width()//2, middleY - text.get_height()//2))

class ImpossibleLevel(pygame.sprite.Sprite):
    def __init__(self):
        self.margin = 10
        self.buttonX = 200
        self.buttonY = 40
        self.impossibleButtonCoord = (50, 150 + self.margin*4 + self.buttonY*3, self.buttonX, self.buttonY)
        #later used for collision
        self.rect = pygame.Rect(50, 150 + self.margin*4 + self.buttonY*3, self.buttonX, self.buttonY)
        self.buttonColor = (173,255,47)

    def draw(self):
        pygame.draw.rect(canvas, self.buttonColor, self.impossibleButtonCoord)
        #print the text:
        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render("IMPOSSIBLE", True, (0,0,0))
        topX = 50
        topY = 150 + self.margin*4 + self.buttonY*3
        botX = topX + self.buttonX
        botY = topY + self.buttonY
        middleX = (topX + botX)//2
        middleY = (topY + botY)//2
        canvas.blit(text, (middleX - text.get_width()//2, middleY - text.get_height()//2))
        
#End Screen:
class EndScreen(object):
    def __init__(self):
        self.width = 300
        self.height = 400

    def draw(self):
        #rectangle:
        titleColor = (154, 205, 50)
        pygame.draw.rect(canvas, titleColor, (0,0, 300, 400))
        #print the text:
        font = pygame.font.SysFont("comicsansms", 45)
        text = font.render("GAME OVER", True, (0,0,0))
        canvas.blit(text, (150 - text.get_width()//2, 72.5 - text.get_height()//2))

class WinMessage(object):
    def __init__(self):
        self.width = 300
        self.height = 400

    def draw(self):
        #rectangle:
        #titleColor = (154, 205, 50)
        #pygame.draw.rect(canvas, titleColor, (0,0, 300, 400))
        #print the text:
        font = pygame.font.SysFont("comicsansms", 45)
        text = font.render("You Won", True, (0,0,0))
        canvas.blit(text, (150 - text.get_width()//2, 200 - text.get_height()//2))

class LoseMessage(object):
    def __init__(self):
        self.width = 300
        self.height = 400

    def draw(self):
        #rectangle:
        #titleColor = (154, 205, 50)
        #pygame.draw.rect(canvas, titleColor, (0,0, 300, 400))
        #print the text:
        font = pygame.font.SysFont("comicsansms", 45)
        text = font.render("You Lost", True, (0,0,0))
        canvas.blit(text, (150 - text.get_width()//2, 200 - text.get_height()//2))

#creating a map:
class Map(object):
    def __init__(self, life):
        self.height = 400 
        self.width = 300   
        #self.difficulty will direct to different types of map!
        self.difficulty = ""
        #Will later implement a empty space on the road
        #IMPORTANT: map will always have to have three S's before a turn
        self.easyMap = self.randomMapGenerator("EASY")
        self.mediumMap = self.randomMapGenerator("MEDIUM")
        self.hardMap = self.randomMapGenerator("HARD")
        self.impossibleMap = self.randomMapGenerator("IMPOSSIBLE")
        self.move = 0
        self.mapIndex = 0 #index for map
        #will index through this for every color of the step
        self.listOfColors = [(255, 91, 165), (255, 132, 198), (255, 187, 218), (219, 73, 172), (228, 114, 191), (240, 173, 219), (153, 97, 205), 
        (176, 124, 218), (209, 178, 234), (67, 142, 200), (107, 167, 214), (168, 204, 232), (59, 198, 192), (100, 212, 199), (164, 231, 223)]
        self.life = life #just for now
        self.pastMapLocation = [] #will store the past map coordinates

        #Obstacle Map and Score Map:
        self.obstacleSpriteGroup = pygame.sprite.Group() #hope to use this for pygame.collision
        self.obstacleMap = [] #will be filled later once the user determines the game difficulty level
        self.obstacleGroup = [] #list of obstacle class instances
        
        self.scoreSpriteGroup = pygame.sprite.Group() #hope to use this for pygame.collision
        self.scoreMap = [] #will be filled later once the user determines the game difficulty level
        self.scoreGroup = [] #list of obstacle class instances

        #Map Positions:
        self.mapLeftMostX = 0
        self.mapRightMostX = 0
        self.cameraMode = False
        self.turnDirection = ""
        self.yMapGameOver = False #if y >= 384 pix

    #create an instance of obstacle class
    def mapDeclaration(self, difficulty):
        if difficulty == "EASY":
            #create a obstacle map:
            self.obstacleMap = self.obstacleRandomMap("EASY", self.easyMap)
            #self.obstacleMap includes None, R, L

            #create a list of obstacle class instances: self.obstacleGroup
            for i in range(len(self.obstacleMap)):
                step = self.obstacleMap[i] #step will either be L, R, or None
                if step != None:
                    obstacleInstance = Obstacle(i, step)
                    self.obstacleGroup.append(obstacleInstance)
                    #self.obstacleSpriteGroup.add(obstacleInstance)

            #create a score map:
            self.scoreMap = self.scoreRandomMap("EASY", self.easyMap, self.obstacleMap)
            #create a list of score class instances:
            for j in range(len(self.scoreMap)):
                step = self.scoreMap[j]
                if step != None:
                    scoreInstance = Score(j, step)
                    self.scoreGroup.append(scoreInstance)
            
            return self.easyMap

        elif difficulty == "MEDIUM":
            self.obstacleMap = self.obstacleRandomMap("MEDIUM", self.mediumMap)
            #create a list of obstacle class instances: self.obstacleGroup
            for i in range(len(self.obstacleMap)):
                step = self.obstacleMap[i] #step will either be L, R, or None
                if step != None: 
                    obstacleInstance = Obstacle(i, step)
                    self.obstacleGroup.append(obstacleInstance)

            self.scoreMap = self.scoreRandomMap("MEDIUM", self.mediumMap, self.obstacleMap)
            #create a list of score class instances:
            for j in range(len(self.scoreMap)):
                step = self.scoreMap[j]
                if step != None:
                    scoreInstance = Score(j, step)
                    self.scoreGroup.append(scoreInstance)
                    
            return self.mediumMap

        elif difficulty == "HARD":
            #self.hardMap = self.randomMapGenerator("hard")
            self.obstacleMap = self.obstacleRandomMap("HARD", self.hardMap)
            #create a list of obstacle class instances: self.obstacleGroup
            for i in range(len(self.obstacleMap)):
                step = self.obstacleMap[i] #step will either be L, R, or None
                if step == None: 
                    obstacleInstance = Obstacle(i, step)
                    self.obstacleGroup.append(obstacleInstance)
                    #self.obstacleSpriteGroup.add(obstacleInstance)

            self.scoreMap = self.scoreRandomMap("HARD", self.hardMap, self.obstacleMap)
            #create a list of score class instances:
            for j in range(len(self.scoreMap)):
                step = self.scoreMap[j]
                if step != None:
                    scoreInstance = Score(j, step)
                    self.scoreGroup.append(scoreInstance)
                    #self.scoreSpriteGroup.add(scoreInstance)
            
            return self.hardMap

        elif difficulty == "IMPOSSIBLE":
            self.obstacleMap = self.obstacleRandomMap("IMPOSSIBLE", self.impossibleMap)
            #create a list of obstacle class instances: self.obstacleGroup
            for i in range(len(self.obstacleMap)):
                step = self.obstacleMap[i] #step will either be L, R, or None
                if step == None: 
                    obstacleInstance = Obstacle(i, step)
                    self.obstacleGroup.append(obstacleInstance)
                    #self.obstacleSpriteGroup.add(obstacleInstance)

            self.scoreMap = self.scoreRandomMap("IMPOSSIBLE", self.impossibleMap, self.obstacleMap)
            #create a list of score class instances:
            for j in range(len(self.scoreMap)):
                step = self.scoreMap[j]
                if step != None:
                    scoreInstance = Score(j, step)
                    self.scoreGroup.append(scoreInstance)
                    #self.scoreSpriteGroup.add(scoreInstance)
            
            return self.impossibleMap

        else:
            #will print this more officially on the screen later
            return "Wrong difficulty"

        #randomly generates the obstacle random map --> no obstacle before or after the turn:
    def obstacleRandomMap(self, difficulty, map):
        obstacleMap = []
        self.obstacleList = []
        if difficulty == "EASY": #2 turns
            mapLength = len(map)
            firstTurn = []
            secondTurn = []
            obstacleMap = [None for i in range(mapLength)]
            for i in range(len(map)):
                step = map[i]
                if step != "S": #there's a turn
                    if firstTurn == []: #empty
                        stepTurn = ["S" for j in range(i)]
                        firstTurn.extend(stepTurn)
                        firstTurn.append(step)

                    elif secondTurn == []:
                        stepTurn = ["S" for j in range(i - len(firstTurn))]
                        secondTurn.extend(stepTurn)
                        secondTurn.append(step)

            #firstTurn:
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(0, len(firstTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1
                
            #secondTurn:
            #index = random.randint(len(firstTurn) + 1, len(firstTurn) + len(secondTurn) - 3)
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + 1
                end = len(firstTurn) + len(secondTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1

        elif difficulty == "MEDIUM": #3 turns
            mapLength = len(map)
            obstacleMap = [None for i in range(mapLength)]
            firstTurn = []
            secondTurn = []
            thirdTurn = []
            for i in range(len(map)):
                step = map[i]
                if step != "S": #there's a turn
                    if firstTurn == []: #empty
                        stepTurn = ["S" for j in range(i)]
                        firstTurn.extend(stepTurn)
                        firstTurn.append(step)

                    elif secondTurn == []:
                        stepTurn = ["S" for j in range(i - len(firstTurn))]
                        secondTurn.extend(stepTurn)
                        secondTurn.append(step)

                    elif thirdTurn == []:
                        rest = len(firstTurn) + len(secondTurn)
                        stepTurn = ["S" for j in range(i - rest)]
                        thirdTurn.extend(stepTurn)
                        thirdTurn.append(step)

            #firstTurn:
            #index = random.randint(0, len(firstTurn) - 3)
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(0, len(firstTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1
                
            #secondTurn:
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(len(firstTurn) + 1, len(firstTurn) + len(secondTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1

            #thirdTurn:
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + len(secondTurn) + 1
                end = len(firstTurn) + len(secondTurn) + len(thirdTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                print(f"pair = {pair}")
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1

        elif difficulty == "HARD": #4 turns
            mapLength = len(map)
            obstacleMap = [None for i in range(mapLength)]
            firstTurn = []
            secondTurn = []
            thirdTurn = []
            fourthTurn = []
            for i in range(len(map)):
                step = map[i]
                if step != "S": #there's a turn
                    if firstTurn == []: #empty
                        stepTurn = ["S" for j in range(i)]
                        firstTurn.extend(stepTurn)
                        firstTurn.append(step)

                    elif secondTurn == []:
                        stepTurn = ["S" for j in range(i - len(firstTurn))]
                        secondTurn.extend(stepTurn)
                        secondTurn.append(step)

                    elif thirdTurn == []:
                        rest = len(firstTurn) + len(secondTurn)
                        stepTurn = ["S" for j in range(i - rest)]
                        thirdTurn.extend(stepTurn)
                        thirdTurn.append(step)

                    elif fourthTurn == []:
                        rest = len(firstTurn) + len(secondTurn) + len(fourthTurn)
                        stepTurn = ["S" for j in range(i - rest)]
                        fourthTurn.extend(stepTurn)
                        fourthTurn.append(step)

            #firstTurn:
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(0, len(firstTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1
                
            #secondTurn: 
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(len(firstTurn) + 1, len(firstTurn) + len(secondTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1
            #thirdTurn:
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + len(secondTurn) + 1
                end = len(firstTurn) + len(secondTurn) + len(thirdTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1

            #fourthTurn:
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + len(secondTurn) + len(thirdTurn) + 1
                end = len(firstTurn) + len(secondTurn) + len(thirdTurn) + len(fourthTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1

        elif difficulty == "IMPOSSIBLE": #5 turns
            mapLength = len(map)
            obstacleMap = [None for i in range(mapLength)]
            #turnList will end with a turn!
            firstTurn = []
            secondTurn = []
            thirdTurn = []
            fourthTurn = []
            fifthTurn = []
            for i in range(len(map)):
                step = map[i]
                if step != "S": #there's a turn
                    if firstTurn == []: #empty
                        stepTurn = ["S" for j in range(i)]
                        firstTurn.extend(stepTurn)
                        firstTurn.append(step)

                    elif secondTurn == []:
                        stepTurn = ["S" for j in range(i - len(firstTurn))]
                        secondTurn.extend(stepTurn)
                        secondTurn.append(step)

                    elif thirdTurn == []:
                        rest = len(firstTurn) - len(secondTurn)
                        stepTurn = ["S" for j in range(i - rest)]
                        thirdTurn.extend(stepTurn)
                        thirdTurn.append(step)

                    elif fourthTurn == []:
                        rest = len(firstTurn) + len(secondTurn) + len(thirdTurn)
                        stepTurn = ["S" for j in range(i - rest)]
                        fourthTurn.extend(stepTurn)
                        fourthTurn.append(step)

                    elif fifthTurn == []:
                        rest = len(firstTurn) + len(secondTurn) + len(thirdTurn) + len(fourthTurn)
                        stepTurn = ["S" for j in range(i - rest)]
                        fifthTurn.extend(stepTurn)
                        fifthTurn.append(step)

            #firstTurn:
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(0, len(firstTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1
                
            #secondTurn: 
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(len(firstTurn) + 1, len(firstTurn) + len(secondTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1

            #thirdTurn:
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + len(secondTurn) + 1
                end = len(firstTurn) + len(secondTurn) + len(thirdTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1

            #fourthTurn:
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + len(secondTurn) + len(thirdTurn) + 1
                end = len(firstTurn) + len(secondTurn) + len(thirdTurn) + len(fourthTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1

            #fifthTurn:
            obstaclePlacement = random.randint(0,2)
            obstacleIncrement = 0
            while obstacleIncrement < obstaclePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + len(secondTurn) + len(thirdTurn) + len(fourthTurn) + 1
                end = len(firstTurn) + len(secondTurn) + len(thirdTurn) + len(fourthTurn) + len(fifthTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    if obstacleMap[index] == None:
                        obstacleMap[index] = turn
                        #self.obstacleList.append(pair)
                        obstacleIncrement += 1

        #obstacleMap to self.obstacleList:
        for ind in range(len(obstacleMap)):
            element = obstacleMap[ind]
            if element != None: #turn
                pair = (ind, element)
                if pair not in self.obstacleList:
                    self.obstacleList.append(pair)

        return obstacleMap

    def scoreRandomMap(self, difficulty, map, obstacleMap):
        scoreMap = []
        self.scoreList = []
        if difficulty == "EASY": #2 turns
            mapLength = len(map)
            firstTurn = []
            secondTurn = []
            scoreMap = [None for i in range(mapLength)]
            for i in range(len(map)):
                step = map[i]
                if step != "S": #there's a turn
                    if firstTurn == []: #empty
                        stepTurn = ["S" for j in range(i)]
                        firstTurn.extend(stepTurn)
                        firstTurn.append(step)

                    elif secondTurn == []:
                        stepTurn = ["S" for j in range(i - len(firstTurn))]
                        secondTurn.extend(stepTurn)
                        secondTurn.append(step)
            
            #firstTurn: 
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(0, len(firstTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None: 
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1
                
            #secondTurn:
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + 1
                end = len(firstTurn) + len(secondTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None:
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1

        elif difficulty == "MEDIUM": #3 turns
            mapLength = len(map)
            scoreMap = [None for i in range(mapLength)]
            firstTurn = []
            secondTurn = []
            thirdTurn = []
            for i in range(len(map)):
                step = map[i]
                if step != "S": #there's a turn
                    if firstTurn == []: #empty
                        stepTurn = ["S" for j in range(i)]
                        firstTurn.extend(stepTurn)
                        firstTurn.append(step)

                    elif secondTurn == []:
                        stepTurn = ["S" for j in range(i - len(firstTurn))]
                        secondTurn.extend(stepTurn)
                        secondTurn.append(step)

                    elif thirdTurn == []:
                        rest = len(firstTurn) + len(secondTurn)
                        stepTurn = ["S" for j in range(i - rest)]
                        thirdTurn.extend(stepTurn)
                        thirdTurn.append(step)

            #firstTurn: 
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(0, len(firstTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None: 
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1
                
            #secondTurn:
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + 1
                end = len(firstTurn) + len(secondTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None:
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1

            #thirdTurn:
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + len(secondTurn) + 1
                end = len(firstTurn) + len(secondTurn) + len(thirdTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None:
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1

        elif difficulty == "HARD": #4 turns
            mapLength = len(map)
            scoreMap = [None for i in range(mapLength)]
            firstTurn = []
            secondTurn = []
            thirdTurn = []
            fourthTurn = []
            for i in range(len(map)):
                step = map[i]
                if step != "S": #there's a turn
                    if firstTurn == []: #empty
                        stepTurn = ["S" for j in range(i)]
                        firstTurn.extend(stepTurn)
                        firstTurn.append(step)

                    elif secondTurn == []:
                        stepTurn = ["S" for j in range(i - len(firstTurn))]
                        secondTurn.extend(stepTurn)
                        secondTurn.append(step)

                    elif thirdTurn == []:
                        rest = len(firstTurn) + len(secondTurn)
                        stepTurn = ["S" for j in range(i - rest)]
                        thirdTurn.extend(stepTurn)
                        thirdTurn.append(step)

                    elif fourthTurn == []:
                        rest = len(firstTurn) + len(secondTurn) + len(thirdTurn)
                        stepTurn = ["S" for j in range(i - rest)]
                        fourthTurn.extend(stepTurn)
                        fourthTurn.append(step)

            #firstTurn:
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(0, len(firstTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None:
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1
                
            #secondTurn:
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(len(firstTurn) + 1, len(firstTurn) + len(secondTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None:
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1

            #thirdTurn:
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + len(secondTurn) + 1
                end = len(firstTurn) + len(secondTurn) + len(thirdTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None:
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1

            #fourthTurn:
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + len(secondTurn) + len(thirdTurn) + 1
                end = len(firstTurn) + len(secondTurn) + len(thirdTurn) + len(fourthTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None:
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1

        elif difficulty == "IMPOSSIBLE": #5 turns
            mapLength = len(map)
            scoreMap = [None for i in range(mapLength)]
            #turnList will end with a turn!
            firstTurn = []
            secondTurn = []
            thirdTurn = []
            fourthTurn = []
            fifthTurn = []
            for i in range(len(map)):
                step = map[i]
                if step != "S": #there's a turn
                    if firstTurn == []: #empty
                        stepTurn = ["S" for j in range(i)]
                        firstTurn.extend(stepTurn)
                        firstTurn.append(step)

                    elif secondTurn == []:
                        stepTurn = ["S" for j in range(i - len(firstTurn))]
                        secondTurn.extend(stepTurn)
                        secondTurn.append(step)

                    elif thirdTurn == []:
                        rest = len(firstTurn) + len(secondTurn)
                        stepTurn = ["S" for j in range(i - rest)]
                        thirdTurn.extend(stepTurn)
                        thirdTurn.append(step)

                    elif fourthTurn == []:
                        rest = len(firstTurn) + len(secondTurn) + len(thirdTurn)
                        stepTurn = ["S" for j in range(i - rest)]
                        fourthTurn.extend(stepTurn)
                        fourthTurn.append(step)

                    elif fifthTurn == []:
                        rest = len(firstTurn) + len(secondTurn) + len(thirdTurn) + len(fourthTurn)
                        stepTurn = ["S" for j in range(i - rest)]
                        fifthTurn.extend(stepTurn)
                        fifthTurn.append(step)

            #firstTurn:
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(0, len(firstTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None:
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1
                
            #secondTurn:
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                index = random.randint(len(firstTurn) + 1, len(firstTurn) + len(secondTurn) - 3)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None:
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1

            #thirdTurn:
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + len(secondTurn) + 1
                end = len(firstTurn) + len(secondTurn) + len(thirdTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None:
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1

            #fourthTurn:
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + len(secondTurn) + + len(thirdTurn) + 1
                end = len(firstTurn) + len(secondTurn) + len(thirdTurn) + len(fourthTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None:
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1

            #fifthTurn:
            scorePlacement = random.randint(0,2)
            scoreIncrement = 0
            while scoreIncrement < scorePlacement:
                turn = random.choice(["L", "R"])
                start = len(firstTurn) + len(secondTurn) + len(thirdTurn) + len(fourthTurn) + 1
                end = len(firstTurn) + len(secondTurn) + len(thirdTurn) + len(fourthTurn) + len(fifthTurn) - 3
                index = random.randint(start, end)
                pair = (index, turn)
                if pair not in self.obstacleList:
                    #check if index is already in the self.scoreList:
                    if scoreMap[index] == None:
                        scoreMap[index] = turn
                        #self.scoreList.append(pair)
                        scoreIncrement += 1

        for ind in range(len(scoreMap)):
            element = scoreMap[ind]
            if element != None: #turn
                pair = (ind, element)
                if pair not in self.scoreList:
                    self.scoreList.append(pair)

        return scoreMap

    def randomMapGenerator(self, difficulty):
        difficulty = difficulty.upper()
        mapStarter = ["S" for i in range(4)]

        #turn == 2:
        if difficulty == "EASY":
            turn = 0
            map = [] #empty
            while turn < 2:
                map.extend(mapStarter)
                isTurn = random.choice(["T", None])
                if isTurn != None: #there's a turn!
                    isTurn = random.choice(["L", "R"])
                    map.append(isTurn)
                    turn += 1
                else:
                    map.append("S")

            map.extend(mapStarter) #ends with four S's
            return map

        #turn == 3:
        elif difficulty == "MEDIUM":
            turn = 0
            map = [] #empty
            while turn < 3:
                map.extend(mapStarter)
                isTurn = random.choice(["T", None])
                if isTurn != None: #there's a turn!
                    isTurn = random.choice(["L", "R"])
                    map.append(isTurn)
                    turn += 1
                else:
                    map.append("S")

            map.extend(mapStarter) #ends with four S's
            return map
        
        #turn == 4:
        elif difficulty == "HARD":
            turn = 0
            map = [] #empty
            while turn < 4:
                map.extend(mapStarter)
                isTurn = random.choice(["T", None])
                if isTurn != None: #there's a turn!
                    isTurn = random.choice(["L", "R"])
                    map.append(isTurn)
                    turn += 1
                else:
                    map.append("S")

            map.extend(mapStarter) #ends with four S's
            return map

        #turn == 5 and forever goes on!
        elif difficulty == "IMPOSSIBLE":
            turn = 0
            map = [] #empty
            while turn < 5:
                map.extend(mapStarter)
                isTurn = random.choice(["T", None])
                if isTurn != None: #there's a turn!
                    isTurn = random.choice(["L", "R"])
                    map.append(isTurn)
                    turn += 1
                else:
                    map.append("S")

            map.extend(mapStarter) #ends with four S's
            return map
        
        else:
            #will print this more officially on the screen later
            return "Wrong difficulty"

    # instead of using random module, I am using set:
    def randomColorGenerator(self):
        colorList = []
        setOfColors = set((255, 91, 165), (255, 132, 198), (255, 187, 218), (219, 73, 172), (228, 114, 191), (240, 173, 219), (153, 97, 205), 
        (176, 124, 218), (209, 178, 234), (67, 142, 200), (107, 167, 214), (168, 204, 232), (59, 198, 192), (100, 212, 199), (164, 231, 223))
        for combo in setOfColors:
            colorList.append(combo)
        return colorList

    #Currently, printingMap will only print the map and will only have one player's full motion = one full block
    #rather than having a player to look like it's constantly moving across each step/block
    #spriteInstance for checking collision b/w obstacle
    def printingMap(self, map, spriteInstance, counting):
        #each clock time is -250pix
        #every 50 milliseconds, self.move will increment as it gets called
        if counting == True:
            self.move += 1
        self.mapIndex = self.move//9
        self.change = self.move % 9
        self.increment = self.change

        #Each step will be x = depends y = depends
        xDistance = self.width/8
        xIncrement = xDistance/9
        yDistance = self.height/4
        yIncrement = yDistance/9

        #list shows index of turning direction:
        turningList = []
        for ind in range(len(map)):
            step = map[ind]
            if step != "S":
                turningList.append(ind)

        #this condition requires the last four element to be "S"
        if self.mapIndex < len(map) - 4 and map[self.mapIndex] == "S": 
            firstStep = map[self.mapIndex]
            secondStep = map[self.mapIndex + 1]
            thirdStep = map[self.mapIndex + 2]
            fourthStep = map[self.mapIndex + 3]
            fifthStep = map[self.mapIndex + 4]
            stepList = [firstStep, secondStep, thirdStep, fourthStep, fifthStep]

            #we need to detect if there's a turn in stepList:
            turnStep = 5
            turnDirection = "S"
            for a in range(len(stepList)):
                currStep = stepList[a]
                if currStep != "S":
                    turnStep = a
                    self.turnDirection = currStep #"L" or "R"
                    turnDirection = currStep
                    #if there are all "S", then turnStep is just 4 and turnDirection is "S"

            #check if the increment starts at == 0
            if self.mapIndex == self.mapIndex + turnStep - 1 and self.cameraMode == False:
            #check if the player sprite is off the map: if y >= 384 pix --> self.yMapGameOver = True
                b = 0
                color = self.listOfColors[(self.mapIndex) % len(self.listOfColors)]
                #randomColor = self.randomColorGenerator()
                x1 = b*xDistance - self.increment*xIncrement
                y1 = self.height - b*yDistance + self.increment*yIncrement
                x2 = self.width - b*xDistance + self.increment*xIncrement
                y2 = self.height - b*yDistance + self.increment*yIncrement
                x3 = self.width - (b+1)*xDistance + self.increment*xIncrement
                y3 = self.height - (b+1)*yDistance + self.increment*yIncrement
                x4 = (b+1)*xDistance - self.increment*xIncrement
                y4 = self.height - (b+1)*yDistance + self.increment*yIncrement

                listCoord = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
               
                pygame.draw.polygon(canvas, color, listCoord)

                #print the turnStep:
                ogCoordinate = listCoord
                if turnDirection == "R":
                    x1 = ogCoordinate[1][0]
                    y1 = ogCoordinate[1][1]
                    x2 = self.width
                    y2 = ogCoordinate[1][1]
                    x3 = self.width
                    y3 = ogCoordinate[2][1]
                    x4 = ogCoordinate[2][0]
                    y4 = ogCoordinate[2][1]
                    turnCoordinate = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                    colorIndex = (self.mapIndex + 1) % len(self.listOfColors)
                    color = self.listOfColors[colorIndex]

                elif turnDirection == "L":
                    colorIndex = (self.mapIndex + 1) % len(self.listOfColors)
                    color = self.listOfColors[colorIndex]
                    x1 = 0
                    y1 = ogCoordinate[0][1]
                    x2 = ogCoordinate[0][0]
                    y2 = ogCoordinate[0][1]
                    x3 = ogCoordinate[3][0]
                    y3 = ogCoordinate[3][1]
                    x4 = 0
                    y4 = ogCoordinate[3][1]
                    turnCoordinate = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                
                pygame.draw.polygon(canvas, color, turnCoordinate)

                if ogCoordinate[3][1] >= 384 - yIncrement: #x4, y4
                    self.yMapGameOver = True

            
            elif self.mapIndex == self.mapIndex + turnStep - 1 and self.cameraMode == True:
                angle = math.atan(37.5/100)

                if self.increment == 0:
                    color = self.listOfColors[(self.mapIndex) % len(self.listOfColors)]
                    #randomColor = self.randomColorGenerator()
                    x1 = 0
                    y1 = self.height
                    x2 = self.width
                    y2 = self.height
                    x3 = self.width - xDistance
                    y3 = self.height - yDistance
                    x4 = xDistance
                    y4 = y3
                    listCoord = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                    pygame.draw.polygon(canvas, color, listCoord)

                    color = self.listOfColors[(self.mapIndex + 1) % len(self.listOfColors)]
                    if turnDirection == "R":
                        x1 = self.width
                        y1 = self.height
                        x2 = x1
                        y2 = y1
                        x3 = self.width
                        y3 = self.height - yDistance
                        x4 = listCoord[2][0]
                        y4 = listCoord[2][1]
                        turnCoordinate = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                        pygame.draw.polygon(canvas, color, turnCoordinate)

                    elif turnDirection == "L":
                        x1 = 0
                        y1 = self.height
                        x2 = x1
                        y2 = y1
                        x3 = 0
                        y3 = self.height - yDistance
                        x4 = listCoord[3][0]
                        y4 = listCoord[3][1]
                        turnCoordinate = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                        pygame.draw.polygon(canvas, color, turnCoordinate)

                    self.mapLeftMostX = self.width - 288
                    self.mapRightMostX = 288
                    
                #using theta angle:
                elif self.increment >= 1 and self.increment <3: #two times
                    # main block = block 1
                    blockHeight = ((37.5**2) + (100**2))**0.5
                    angleIncrement = angle/2
                    if turnDirection == "R":
                        
                        x1 = 0
                        y1 = self.height
                        x2 = 300*math.cos(angleIncrement*self.increment)
                        y2 = self.height - 300*math.sin(angleIncrement*self.increment)
                        x4 = blockHeight*math.sin(angle - angleIncrement*self.increment)
                        y4 = self.height - blockHeight*math.cos(angle - angleIncrement*self.increment)
                        x3 = x4 + 225*math.cos(angleIncrement*self.increment) 
                        y3 = y4 - 225*math.sin(angleIncrement*self.increment)
                        self.block1Coord = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                        color = self.listOfColors[(self.mapIndex) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, self.block1Coord)
                        #print(f"self.block1Coord = {self.block1Coord}")

                        # bottom block = block 2 --> index - 1:
                        x1 = 0
                        y1 = self.height
                        x2 = self.block1Coord[1][0] + 37.5*(self.block1Coord[1][1]/100)
                        y2 = self.height
                        x3 = self.block1Coord[1][0]
                        y3 = self.block1Coord[1][1]
                        self.block2Coord = [(x1,y1), (x2,y2), (x3,y3)]
                        color = self.listOfColors[(self.mapIndex - 1) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, self.block2Coord)

                        #turn block = block 3 --> index + 1
                        x1 = self.block1Coord[1][0]
                        y1 = self.block1Coord[1][1]
                        x2 = self.width
                        y2 = self.height - 300*math.tan(angleIncrement*self.increment)
                        x3 = self.width
                        y3 = self.block1Coord[2][1] - (self.width - self.block1Coord[2][0])*math.tan(angleIncrement*self.increment)
                        x4 = self.block1Coord[2][0]
                        y4 = self.block1Coord[2][1]
                        self.block3Coord = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                        
                        color = color = self.listOfColors[(self.mapIndex + 1) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, self.block3Coord)

                        #updating this variable for later use!
                        self.mapLeftMostX = self.block1Coord[3][0]
                        self.mapRightMostX = self.block2Coord[1][0]
                    
                    elif turnDirection == "L":
                        x1 = self.width
                        y1 = self.height
                        x2 = self.width - 300*math.cos(angleIncrement*self.increment)
                        y2 = self.height - 300*math.sin(angleIncrement*self.increment)
                        x4 = self.width - blockHeight*math.sin(angle - angleIncrement*self.increment) #added self.width
                        y4 = self.height - blockHeight*math.cos(angle - angleIncrement*self.increment)
                        x3 = x4 - 225*math.cos(angleIncrement*self.increment) 
                        y3 = y4 - 225*math.sin(angleIncrement*self.increment)
                        self.block1Coord = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                        color = self.listOfColors[(self.mapIndex) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, self.block1Coord)

                        # bottom block = block 2 --> index - 1:
                        x1 = self.width
                        y1 = self.height
                        x2 = self.block1Coord[1][0] - 37.5*(self.block1Coord[1][1]/100)
                        y2 = self.height
                        x3 = self.block1Coord[1][0]
                        y3 = self.block1Coord[1][1]
                        self.block2Coord = [(x1,y1), (x2,y2), (x3,y3)]
                        color = self.listOfColors[(self.mapIndex - 1) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, self.block2Coord)

                        #turn block = block 3 --> index + 1
                        x1 = self.block1Coord[1][0]
                        y1 = self.block1Coord[1][1]
                        x2 = 0
                        y2 = self.height - 300*math.tan(angleIncrement*self.increment)
                        x3 = 0 #self.width
                        y3 = self.block1Coord[2][1] - (self.block1Coord[2][0])*math.tan(angleIncrement*self.increment)
                        x4 = self.block1Coord[2][0]
                        y4 = self.block1Coord[2][1]
                        self.block3Coord = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                        
                        color = color = self.listOfColors[(self.mapIndex + 1) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, self.block3Coord)

                        self.mapLeftMostX = self.block2Coord[1][0]
                        self.mapRightMostX = self.block1Coord[3][0]

                elif self.increment >= 3 and self.increment < 8: #3, 4, 5, 6, 7, 8
                    #at all times:
                    self.mapLeftMostX = 50  
                    self.mapRightMostX = 250

                    subIncrement = self.increment - 3 #0, 1, 2, 3, 4, 5
                    #slope1X = 0
                    slope1Y = abs(self.block1Coord[0][1] - self.block1Coord[3][1])/7
                    slope2X = abs(self.block1Coord[2][0] - self.block1Coord[1][0])/7
                    slope2Y = abs(self.block1Coord[2][1] - self.block1Coord[1][1])/7
                    # main block = block 1
                    if turnDirection == "R":
                        x1 = 0
                        y1 = self.block1Coord[0][1] + slope1Y*subIncrement
                        x2 = self.block1Coord[1][0] + slope2X*subIncrement
                        y2 = self.block1Coord[1][1] + slope2Y*subIncrement
                        x3 = self.block1Coord[2][0] + slope2X*subIncrement
                        y3 = self.block1Coord[2][1] + slope2Y*subIncrement
                        x4 = 0
                        y4 = self.block1Coord[3][1] + slope1Y*subIncrement
                        
                        self.second1Coord = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                        color = self.listOfColors[(self.mapIndex) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, self.second1Coord)

                        # bottom block = block 2 --> index - 1
                        x1 = self.second1Coord[0][0] 
                        y1 = self.second1Coord[0][1]
                        x2 = self.block2Coord[1][0] + slope2X*subIncrement
                        y2 = self.block2Coord[1][1] + slope2Y*subIncrement
                        x3 = self.second1Coord[1][0]
                        y3 = self.second1Coord[1][1]
                        
                        second2Coord = [(x1,y1), (x2,y2), (x3,y3)]
                        color = self.listOfColors[(self.mapIndex - 1) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, second2Coord)

                        # turning block = block 3 --> index + 1
                        x1 = self.second1Coord[1][0] 
                        y1 = self.second1Coord[1][1]
                        x2 = self.block3Coord[1][0] + slope2X*subIncrement
                        y2 = self.block3Coord[1][1] + slope2Y*subIncrement
                        x3 = self.block3Coord[2][0] + slope2X*subIncrement
                        y3 = self.block3Coord[2][1] + slope2Y*subIncrement
                        x4 = self.second1Coord[2][0]
                        y4 = self.second1Coord[2][1]

                        self.second3Coord = [(x1,y1), (x2,y2), (x3,y3), (x4, y4)]
                        color = self.listOfColors[(self.mapIndex + 1) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, self.second3Coord)
                    
                    elif turnDirection == "L":
                        x1 = self.width
                        y1 = self.block1Coord[0][1] + slope1Y*subIncrement
                        x2 = self.block1Coord[1][0] - slope2X*subIncrement
                        y2 = self.block1Coord[1][1] + slope2Y*subIncrement
                        x3 = self.block1Coord[2][0] - slope2X*subIncrement
                        y3 = self.block1Coord[2][1] + slope2Y*subIncrement
                        x4 = self.width
                        y4 = self.block1Coord[3][1] + slope1Y*subIncrement
                        
                        self.second1Coord = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                        color = self.listOfColors[(self.mapIndex) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, self.second1Coord)

                        # bottom block = block 2 --> index - 1
                        x1 = self.second1Coord[0][0] 
                        y1 = self.second1Coord[0][1]
                        x2 = self.block2Coord[1][0] - slope2X*subIncrement
                        y2 = self.block2Coord[1][1] + slope2Y*subIncrement
                        x3 = self.second1Coord[1][0]
                        y3 = self.second1Coord[1][1]
                        
                        second2Coord = [(x1,y1), (x2,y2), (x3,y3)]
                        color = self.listOfColors[(self.mapIndex - 1) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, second2Coord)

                        # turning block = block 3 --> index + 1
                        x1 = self.second1Coord[1][0] 
                        y1 = self.second1Coord[1][1]
                        x2 = self.block3Coord[1][0] - slope2X*subIncrement
                        y2 = self.block3Coord[1][1] + slope2Y*subIncrement
                        x3 = self.block3Coord[2][0] - slope2X*subIncrement
                        y3 = self.block3Coord[2][1] + slope2Y*subIncrement
                        x4 = self.second1Coord[2][0]
                        y4 = self.second1Coord[2][1]

                        second3Coord = [(x1,y1), (x2,y2), (x3,y3), (x4, y4)]
                        color = self.listOfColors[(self.mapIndex + 1) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, second3Coord)

                elif self.increment >= 8: #6, 7, 8, 9

                    if turnDirection == "R":
                        midPointX = self.second1Coord[2][0]/2 + 50
                        newAngle = math.radians(math.degrees(math.atan(37.5/100)) + 10)
                        # main block -> index 
                        x1 = 0
                        y1 = self.height
                        x2 = midPointX 
                        y2 = self.height - midPointX*math.tan(newAngle)
                        x3 = (x2**2 + (self.height - y2)**2)**0.5 / math.cos(newAngle)
                        y3 = self.height
                        listCoord = [(x1,y1), (x2,y2), (x3,y3)]
                        color = self.listOfColors[(self.mapIndex) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, listCoord)

                        # turning block --> index + 1
                        x1 = listCoord[2][0]
                        y1 = listCoord[2][1]
                        x2 = self.width
                        y2 = self.height
                        x3 = self.width
                        y3 = self.height - 300*math.tan(newAngle)
                        x4 = listCoord[1][0]
                        y4 = listCoord[1][1]
                        listCoord = [(x1,y1), (x2,y2), (x3,y3), (x4, y4)]
                        color = self.listOfColors[(self.mapIndex + 1) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, listCoord)

                        yHeight = 300*math.tan(newAngle)
                        newHeight = yHeight - 16
                        self.mapLeftMostX = newHeight*300/yHeight
                        self.mapRightMostX = 0
                    
                    elif turnDirection == "L":
                        midPointX = self.second1Coord[2][0]/2 + 50
                        newAngle = math.radians(math.degrees(math.atan(37.5/100)) + 10)
                        # main block -> index 
                        x1 = self.width
                        y1 = self.height
                        x2 = self.width - midPointX 
                        y2 = self.height - midPointX*math.tan(newAngle)
                        x3 = self.width - (x2**2 + (self.height - y2)**2)**0.5 / math.cos(newAngle)
                        y3 = self.height
                        listCoord = [(x1,y1), (x2,y2), (x3,y3)]
                        color = self.listOfColors[(self.mapIndex) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, listCoord)

                        # turning block --> index + 1
                        x1 = listCoord[2][0]
                        y1 = listCoord[2][1]
                        x2 = 0
                        y2 = self.height
                        x3 = 0
                        y3 = self.height - 300*math.tan(newAngle)
                        x4 = listCoord[1][0]
                        y4 = listCoord[1][1]
                        listCoord = [(x1,y1), (x2,y2), (x3,y3), (x4, y4)]
                        color = self.listOfColors[(self.mapIndex + 1) % len(self.listOfColors)]
                        pygame.draw.polygon(canvas, color, listCoord)
                        
                        yHeight = 300*math.tan(newAngle)
                        newHeight = yHeight - 16
                        self.mapRightMostX = newHeight*300/yHeight
                        self.mapLeftMostX = 0

            else:
                self.mapLeftMostX = self.width - 288
                self.mapRightMostX = 288
                
                for b in range(0, turnStep):
                    color = self.listOfColors[(self.mapIndex + b) % len(self.listOfColors)]
                    #randomColor = self.randomColorGenerator()
                    x1 = b*xDistance - self.increment*xIncrement
                    y1 = self.height - b*yDistance + self.increment*yIncrement
                    x2 = self.width - b*xDistance + self.increment*xIncrement
                    y2 = self.height - b*yDistance + self.increment*yIncrement
                    x3 = self.width - (b+1)*xDistance + self.increment*xIncrement
                    y3 = self.height - (b+1)*yDistance + self.increment*yIncrement
                    x4 = (b+1)*xDistance - self.increment*xIncrement
                    y4 = self.height - (b+1)*yDistance + self.increment*yIncrement
                    listCoord = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                    
                    pygame.draw.polygon(canvas, color, listCoord)
                    
                    #print the turnStep:
                    if b == turnStep - 1 and turnDirection != "S":
                        ogCoordinate = listCoord
                        if turnDirection == "R":
                            x1 = ogCoordinate[1][0]
                            y1 = ogCoordinate[1][1]
                            x2 = self.width
                            y2 = ogCoordinate[1][1]
                            x3 = self.width
                            y3 = ogCoordinate[2][1]
                            x4 = ogCoordinate[2][0]
                            y4 = ogCoordinate[2][1]
                            turnCoordinate = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                            colorIndex = (self.mapIndex + turnStep) % len(self.listOfColors)
                            color = self.listOfColors[colorIndex]

                        elif turnDirection == "L":
                            colorIndex = (self.mapIndex + turnStep) % len(self.listOfColors)
                            color = self.listOfColors[colorIndex]
                            x1 = 0
                            y1 = ogCoordinate[0][1]
                            x2 = ogCoordinate[0][0]
                            y2 = ogCoordinate[0][1]
                            x3 = ogCoordinate[3][0]
                            y3 = ogCoordinate[3][1]
                            x4 = 0
                            y4 = ogCoordinate[3][1]
                            turnCoordinate = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                        pygame.draw.polygon(canvas, color, turnCoordinate)

                    #prints the obstacle:
                    self.featureIndex = self.mapIndex + b
        
                    for score in self.scoreGroup:
                        if score.index == self.featureIndex:
                            score.printingScoreMap(b, x1, y1, x2, y2)

                    for obstacle in self.obstacleGroup:
                        if obstacle.index == self.featureIndex:
                            obstacle.printingObstacleMap(self.obstacleList, self.featureIndex, x1, y1, x2, y2)

                    
        else:
            #then, just print out the straight map:
            for j in range(5):
                color = self.listOfColors[(self.mapIndex + j)% len(self.listOfColors)]
                x1 = j*xDistance - self.increment*xIncrement
                y1 = self.height - j*yDistance + self.increment*yIncrement
                x2 = self.width - j*xDistance + self.increment*xIncrement
                y2 = self.height - j*yDistance + self.increment*yIncrement
                x3 = self.width - (j+1)*xDistance + self.increment*xIncrement
                y3 = self.height - (j+1)*yDistance + self.increment*yIncrement
                x4 = (j+1)*xDistance - self.increment*xIncrement
                y4 = self.height - (j+1)*yDistance + self.increment*yIncrement
                listCoord = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
                #last element of the game
                pygame.draw.polygon(canvas, color, listCoord)

                #prints the obstacle:
                self.featureIndex = self.mapIndex + j
                
                for score in self.scoreGroup:
                    if score.index == self.featureIndex:
                        score.printingScoreMap(j, x1, y1, x2, y2)

                for obstacle in self.obstacleGroup:
                    if obstacle.index == self.featureIndex:
                        #then need to print this:
                        obstacle.printingObstacleMap(self.obstacleList, self.featureIndex, x1, y1, x2, y2)

            self.mapLeftMostX = self.width - 288
            self.mapRightMostX = 288
                        
    def updateScoreCount(self):
        return self.life

#using OOP to create a player sprite
class Player(pygame.sprite.Sprite):
    def __init__ (self, posX, posY):
        self.width = 300 #canvas size
        self.height = 400
        self.posX = posX
        self.posY = posY
        self.playerImages = [pygame.image.load("sprite1.png"), pygame.image.load("sprite2.png"), pygame.image.load("sprite3.png"), 
                                pygame.image.load("sprite4.png"), pygame.image.load("sprite5.png"), pygame.image.load("sprite6.png"),
                                pygame.image.load("sprite7.png"), pygame.image.load("sprite8.png"), pygame.image.load("sprite9.png")]
        #practice circles:
        self.index = 0
        self.spriteSizeX = 32
        self.spriteSizeY = 54
        self.fullSize = (self.posX, self.posY, self.spriteSizeX, self.spriteSizeY)
        self.weight = 1
        self.velocity = 5 #just a random velocity
        self.isJumping = False 
        self.mapLX = 0 #will be used in self.mapPositionFinder
        self.mapRX = 0 
        
    #gets called in Map Class, printingMap and will pass the leftMostX and rightMostX
    #to find collision part for map:
    def isMapCollision(self, mapLeftX, mapRightX):
        self.playerLeftX = self.posX
        self.playerRightX = self.posX + self.spriteSizeX
        
        #printing regularly blocks with be leftMostX = 384*3/4 and RightMostX = self.width - leftMostX
        #incremented camera mode will be different
        
        if self.playerLeftX <= mapLeftX:
            return False

        if self.playerRightX >= mapRightX:
            return False

        return True

    #newPosX, newPosY are already modified in regards to self.posX and self.posY
    def update(self, newPosX, newPosY, playerImagesIndex):
        self.posX = newPosX
        self.posY = newPosY
        self.index = playerImagesIndex % 9
        #updates the self.fullSize box coordinates
        self.fullSize = (self.posX, self.posY, self.spriteSizeX, self.spriteSizeY)
        canvas.blit(self.playerImages[self.index], (self.posX, self.posY))
        #pygame.draw.rect(canvas, (0,0,0), self.fullSize, 2)

    #jumping example: https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/
    def jumpingAction(self):
        #print("isJumping is called :)")
        #calculating the force using the given equation: F = 0.5*m*v**2
        force = 0.5*self.weight*(self.velocity**2)
        self.posX -= force
        self.velocity -= 1
        # object reached its maximum height 
        if self.velocity < 0:   
            # negative sign is added to counter negative velocity 
            self.weight = -1
        # objected reaches its original state 
        if self.velocity == -6:  
            self.velocity = 5
            self.weight = 1
        self.isJumping = True

    def dyingSprite(self, increment, direction, mapInstance):
        #increment increases every time time delay in called!
        if direction == "L":
            angle = -20*increment
        elif direction == "R":
            angle = 20*increment
        playerImage = self.playerImages[increment]
        #new size:
        sizeX = int(32*((9-increment)/9))
        sizeY = int(54*((9-increment)/9))
        #adjust the size:
        image = pygame.transform.scale(playerImage, (sizeX, sizeY))
        #pygame blit w falling:
        image = pygame.transform.rotate(image, angle)
        if direction == "R":
            canvas.blit(image, (self.posX + 32, self.posY))
        elif direction == "L":
            canvas.blit(image, (self.posX - sizeY, self.posY))

    def yDyingSprite(self, increment, direction, mapInstance):
        #redraw the map:
        xDistance = self.width/8
        x1 = 0
        y1 = self.height
        x2 = self.width
        y2 = self.height
        x3 = self.width - xDistance*(16/100)
        y3 = self.height - 16
        x4 = xDistance*(16/100)
        y4 = y3
        listCoord = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
        mapIndex = mapInstance.featureIndex
        color = mapInstance.listOfColors[(mapIndex) % len(mapInstance.listOfColors)]

        pygame.draw.polygon(canvas, color, listCoord)

        if direction == "L":
            #redraw the map
            x1 = 0
            y1 = self.height
            x2 = listCoord[3][0]
            y2 = listCoord[3][1]
            x3 = 0
            y3 = y2
            turnCoord = [(x1,y1), (x2,y2), (x3,y3)]
            color = mapInstance.listOfColors[(mapIndex + 1) % len(mapInstance.listOfColors)]
            pygame.draw.polygon(canvas, color, turnCoord)
                
        elif direction == "R":
            #redraw the map
            x1 = self.width
            y1 = self.height
            x2 = listCoord[2][0]
            y2 = listCoord[2][1]
            x3 = self.width
            y3 = y2
            turnCoord = [(x1,y1), (x2,y2), (x3,y3)]
            color = mapInstance.listOfColors[(mapIndex + 1) % len(mapInstance.listOfColors)]
            pygame.draw.polygon(canvas, color, turnCoord)
        
        angle = 180*increment

        playerImage = self.playerImages[increment]
        #new size:
        sizeX = int(32*((9-increment)/9))
        sizeY = int(54*((9-increment)/9))
        #adjust the size:
        image = pygame.transform.scale(playerImage, (sizeX, sizeY))
        #pygame blit w falling:
        image = pygame.transform.rotate(image, angle)
        
        canvas.blit(image, (self.posX, self.posY))

#"Obstacles" = Rocks
# this will be called in the Map class
class Obstacle(pygame.sprite.Sprite):
    #will be given the obstacle position:
    def __init__ (self, index, position):
        self.position = position #L, R
        #just to be safe, I will check again later!
        self.index = index #correspoding index to the overall map
        self.obstacleImage = pygame.image.load("rock.png")
        self.sizeX = 512 #og size
        self.sizeY = 512 #og size
        self.sizeCoord = [] #self.sizeCoord = (self.posX, self.posY, self.sizeScale, self.sizeScale)
        self.sizeScale = 100
        self.posX = 0
        self.posY = 0
        self.sizeList = [200, 1000]
        self.inc = 0

    #in printingMap method in Map class, the instance of this will be used and this method will be called
    def printingObstacleMap(self, obstacleMap, index, x1, y1, x2, y2):
        self.inc = (self.inc + 1)%2
        self.sizeScale = min(self.sizeList[self.inc], int((x2 - x1)*0.3))
        #find the position of this current obstacle!
        for i in range(len(obstacleMap)):
            pair = obstacleMap[i]
            if pair[0] == index:
                self.position = pair[1]

        if self.position == "L":
            self.posX = x1
            self.posY = y1 - self.sizeScale
        elif self.position == "R":
            self.posX = x2 - self.sizeScale
            self.posY = y2 - self.sizeScale

        self.posX = int(self.posX)
        self.posY = int(self.posY)

        #this will print the obstacle
        self.obstacleImage = pygame.transform.scale(self.obstacleImage, (self.sizeScale, self.sizeScale))
        canvas.blit(self.obstacleImage, (self.posX, self.posY))
        
    def isCollision(self, spriteX, spriteY):
        #find if this collides with the user's sprite:
        #current sprite posX = spriteX,
        spriteLeftX = spriteX
        spriteRightX = spriteX + 32 #32 is the x size of the player sprite
        spriteTopY = spriteY
        spriteBotY = spriteY + 54 #sprite's y size
        if self.posX == 0 and self.posY == 0:
            return False #automatically

        if self.position == "L":
            #check for leftX:
            if spriteLeftX < self.posX + self.sizeScale:
                #check for topY of the block w botY of the player (going from the bottome):
                if spriteTopY - (self.posY + self.sizeScale) < 0 and spriteTopY - (self.posY + self.sizeScale) > self.sizeScale: #it's overlapping
                    return True #there is collision
                #going from the top
                elif spriteBotY - self.posY > 0 and spriteBotY - self.posY < self.sizeScale + 54:
                    return True #there is collision

        elif self.position == "R":
            #only check for rightX:
            if spriteRightX > self.posX:
                #check for topY of the block w botY of the player (going from the bottome):
                if spriteTopY - (self.posY + self.sizeScale) < 0 and spriteTopY - (self.posY + self.sizeScale) > self.sizeScale: #it's overlapping
                    return True #there is collision
                #going from the top
                elif spriteBotY - self.posY > 0 and spriteBotY - self.posY < self.sizeScale + 54:
                    return True #there is collision
        return False

#Need to come back to this!
class Score(pygame.sprite.Sprite):
    #will be given the coin position:
    def __init__ (self, index, position):
        self.position = position #L, R
        self.index = index #correspoding index to the overall map
        self.scoreImage = pygame.image.load("coin.png")
        self.sizeX = 100 #og size
        self.sizeY = 100 #og size
        self.sizeCoord = [] #self.sizeCoord = (self.posX, self.posY, self.sizeScale, self.sizeScale)
        self.sizeScale = 10
        self.posX = 0
        self.posY = 0

    #in printingMap method in Map class, the instance of this will be used and this method will be called
    def printingScoreMap(self, localIndex, x1, y1, x2, y2):
        #localIndex = 0 being the closes to 400
        self.sizeScale = int((x2 - x1)*0.3)

        if self.position == "L":
            self.posX = x1
            self.posY = y1 - self.sizeScale
        elif self.position == "R":
            self.posX = x2 - self.sizeScale
            self.posY = y2 - self.sizeScale

        self.posX = int(self.posX)
        self.posY = int(self.posY)

        #this will print the obstacle
        self.scoreImage = pygame.transform.scale(self.scoreImage, (self.sizeScale, self.sizeScale))
        canvas.blit(self.scoreImage, (self.posX, self.posY))
        
    def distance(self, x1, y1, x2, y2):
        return ((x2-x1)**2 + (y2-y1)**2)**0.5 

    def isCollision(self, spriteX, spriteY):
        #find if this collides with the user's sprite:
        #current sprite posX = spriteX,
        if self.posX == 0 and self.posY == 0:
            return False #automatically

        spriteLeftX = spriteX
        spriteRightX = spriteX + 32 #32 is the x size of the player sprite
        spriteTopY = spriteY
        spriteBotY = spriteY + 54 #sprite's y size
        if self.position == "L":
            #check for leftX:
            if spriteLeftX < self.posX + self.sizeScale:
                #check for topY of the block w botY of the player (going from the bottome):
                if spriteTopY - (self.posY + self.sizeScale) < 0 and spriteTopY - (self.posY + self.sizeScale) > self.sizeScale: #it's overlapping
                    return True #there is collision
                #going from the top
                elif spriteBotY - self.posY > 0 and spriteBotY - self.posY < self.sizeScale + 54:
                    return True #there is collision

        elif self.position == "R":
            #only check for rightX:
            if spriteRightX > self.posX:
                #check for topY of the block w botY of the player (going from the bottome):
                if spriteTopY - (self.posY + self.sizeScale) < 0 and spriteTopY - (self.posY + self.sizeScale) > self.sizeScale: #it's overlapping
                    return True #there is collision
                #going from the top
                elif spriteBotY - self.posY > 0 and spriteBotY - self.posY < self.sizeScale + 54:
                    return True #there is collision
        return False

class gameScreen(object):
    def __init__(self, score, life):
        self.score = score
        self.life = life #will later convert this to a heart png to show lives

    def drawScore(self, score):
        self.score = score #updates the score
        #print the text:
        font = pygame.font.SysFont("comicsansms", 12)
        text = font.render(f"SCORE = {self.score}", True, (0,0,0))
        canvas.blit(text, (50 - text.get_width()//2, 20 - text.get_height()//2))

    def drawLife(self, life):
        self.life = life
        #print the text:
        font = pygame.font.SysFont("comicsansms", 12)
        text = font.render(f"LIFE = {self.life}", True, (0,0,0))
        canvas.blit(text, (250 - text.get_width()//2, 20 - text.get_height()//2))

class Background(object):
    def __init__(self):
        #size = 100 * 64 pixel
        image = pygame.image.load("cloud.png")
        cloudImage = pygame.transform.scale(image, (100, 64))
        self.cloudImageList = [cloudImage for i in range(4)]
        #will start with four:
        self.cloudPosition = []
        for i in range(4):
            if i== 0: #even, then left side of the screen
                posX = 150
                posY = 50

            elif i == 1:
                posX = 25
                posY = 100

            elif i == 2:
                posX = 150
                posY = 250

            elif i == 3:
                posX = 25
                posY = 300
                
            pair = (posX, posY)
            self.cloudPosition.append(pair)
        print(f"cloudPosition = {self.cloudPosition}")

    def drawBackground (self):
        #firstCloud: startPos = (150, 50)
        posX = self.cloudPosition[0][0] + 150/70
        posY = self.cloudPosition[0][1] + 5
        if posY >= 464: #goes out of bound!
            posX = 120
            posY = -64
        newPair = (posX, posY)
        self.cloudPosition[0] = newPair
        #currImage
        currImage = self.cloudImageList[0]
        canvas.blit(currImage, (posX, posY))

        #secondCloud: startPos = (25, 100)
        posX = self.cloudPosition[1][0] - 2
        posY = self.cloudPosition[1][1] + 5
        if posY >= 464: #goes out of bound!
            posX = 50
            posY = -64
        newPair = (posX, posY)
        self.cloudPosition[1] = newPair
        #currentImage
        currImage = self.cloudImageList[1]
        canvas.blit(currImage, (posX, posY))

        #thirdCloud: startPos = (150, 250)
        posX = self.cloudPosition[2][0] + 2
        posY = self.cloudPosition[2][1] + 5
        if posY >= 464: #goes out of bound!
            posX = 100
            posY = -64

        newPair = (posX, posY)
        self.cloudPosition[2] = newPair
        #currentImage
        currImage = self.cloudImageList[2]
        canvas.blit(currImage, (posX, posY))

        #fourthCloud: startPos = (25, 300)
        posX = self.cloudPosition[3][0] - 2
        posY = self.cloudPosition[3][1] + 5
        if posY >= 464: #goes out of bound!
            posX = 70
            posY = -64
        newPair = (posX, posY)
        self.cloudPosition[3] = newPair
        #currentImage
        currImage = self.cloudImageList[3]
        canvas.blit(currImage, (posX, posY))

#main loop starts here:

#declare the start x and y for player's position
centerX = 150
centerY = 330
pastX = 150

#create the initial instance of player
playerInstance = Player(centerX, centerY)

#initializes playerMotionIndex:
playerMotionIndex = 0

#startScreen Mode:
startScreen = True
#making instances of each level button:
titleScreen = StartScreen()
easyLevelButton = EasyLevel() 
mediumLevelButton = MediumLevel()
hardLevelButton = HardLevel()
impossibleLevelButton = ImpossibleLevel()

#gameScreen Mode:
gameMode = False #until startScreen becomes False
impossibleGameMode = False
backgroundInstance = Background()

#gameScreen instance for life and score:
score = 0
life = 3
spriteIncrement = 0 #for rotating
gameInstance = gameScreen(score, life)

#randomly generate the obstacle map:
obstacleCount = 0
obstacleMapG = [] #G stands for global

#creates the instance of Map Class
mapInstance = Map(life)
indexForMap = 0

#gameOver Screen
gameOver = False
gameOverMode = False
endScreenInstance = EndScreen()
turnDirection = "" #for rotating purposes
cameraModeIncrement = 0

#messages:
winMsgInstance = WinMessage()
loseMsgInstance = LoseMessage()
level = ""

while run: #run == True
    #100 milli-seconds (= 10 actions per second)
    pygame.time.delay(100) 

    if gameOverMode == True:
        canvas.fill((255,255,255))
        endScreenInstance.draw()
        if level == "EASY":
            if life >= 0: 
                winMsgInstance.draw()
            else:
                loseMsgInstance.draw()
        
        elif level == "MEDIUM":
            if life >= 0 and score >= 1:
                winMsgInstance.draw()
            else:
                loseMsgInstance.draw()

        elif level == "HARD":
            if life >= 0 and score >= 2:
                winMsgInstance.draw()
            else:
                loseMsgInstance.draw()
        elif level == "IMPOSSIBLE":
            if life >= 1 and score >= 3: # life does not count as the map for IMPOSSIBLE mode will just continuously run!
                winMsgInstance.draw()
            else:
                loseMsgInstance.draw()
        
        pygame.display.flip()

    elif gameOver == True:
        #new player's motion/position
        canvas.fill((135, 206, 235))
        backgroundInstance.drawBackground()
        #this will also check for collision:
        #gameScreen for life and score:
        #update life count 
        gameInstance.drawScore(score)
        gameInstance.drawLife(life)

        if mapInstance.yMapGameOver == True:
            playerInstance.yDyingSprite(spriteIncrement, turnDirection, mapInstance)

        else:
            #print the map:
            mapInstance.printingMap(map, playerInstance, False)
            #ALWYAS HAVE THIS! This updates the screen
            if turnDirection == "R":
                playerInstance.dyingSprite(spriteIncrement, "R", mapInstance)
            elif turnDirection == "L":
                playerInstance.dyingSprite(spriteIncrement, "L", mapInstance)

        spriteIncrement += 1
        if spriteIncrement == 9:
            gameOverMode = True

        pygame.display.flip() 
            

    elif startScreen == True:
        #this will print the start screen
        canvas.fill((255,255,255))
        titleScreen.draw()
        easyLevelButton.draw()
        mediumLevelButton.draw()
        hardLevelButton.draw()
        impossibleLevelButton.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                #mouse click
                #if easyLevelButton is clicked --> call isClicked()
                if easyLevelButton.rect.collidepoint(pos): 
                    #easyLevelButton.isClicked()
                    map = mapInstance.mapDeclaration("EASY")
                    startScreen = False
                    gameMode = True
                    level = "EASY"
                elif mediumLevelButton.rect.collidepoint(pos):
                    map = mapInstance.mapDeclaration("MEDIUM")
                    startScreen = False
                    gameMode = True
                    level = "MEDIUM"
                elif hardLevelButton.rect.collidepoint(pos):
                    map = mapInstance.mapDeclaration("HARD")
                    startScreen = False
                    gameMode = True
                    level = "HARD"
                elif impossibleLevelButton.rect.collidepoint(pos):
                    map = mapInstance.mapDeclaration("IMPOSSIBLE")
                    startScreen = False
                    impossibleGameMode = True
                    level = "IMPOSSIBLE"

    elif impossibleGameMode == True:
        playerMotionIndex += 1 #every 0.1 second, the player's motion changes
        if life == 3:
            gameOverMode = True
            
        if mapInstance.cameraMode == True:
            if mapInstance.increment >= 8:
                mapInstance.cameraMode = False

        #pygame.event.get() is a list of all the actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
            
        #list of pressed keys
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]: 
            centerX -= 10 #changes the position of the player
            #updates the location of the player    
            playerInstance.update(centerX, centerY, playerMotionIndex)
            
            #loop through every obstacle instances in obstacle group:
            for instance in mapInstance.obstacleGroup:
                
                if instance.isCollision(centerX, centerY):
                    #pastX = centerX
                    centerX = 150 #back to original place
                    life -= 1
                    
                    turnDirection = "L"
                    if life == -1:
                        gameOverMode = True
                    
            #loop through every score instances in score group:
            for instance in mapInstance.scoreGroup:
                if instance.isCollision(centerX, centerY): #passes along the sprite's position
                    centerX = 150
                    score += 1

            #check if the sprite player is out of game map
            if playerInstance.isMapCollision(mapInstance.mapLeftMostX, mapInstance.mapRightMostX) == False: #go to the game over screen!
                #this will draw the game over screen
                life = - 1
                turnDirection = "L"
                gameOver = True

        if keys[pygame.K_RIGHT]:
            centerX += 10 #changes the position of the player
            #updates the location of the player    
            playerInstance.update(centerX, centerY, playerMotionIndex)
            #loop through every obstacle instances in obstacle group:
            for instance in mapInstance.obstacleGroup:
                if instance.isCollision(centerX, centerY):
                    #pastX = centerX
                    centerX = 150 #original centerX
                    life -= 1
                    turnDirection = "R"
                    if life == -1:
                        gameOverMode = True
                    
            #loop through every score instances in score group:
            for instance in mapInstance.scoreGroup:
                if instance.isCollision(centerX, centerY):
                    centerX = 150
                    score += 1
            
            #check if the sprite player is out of game map
            if playerInstance.isMapCollision(mapInstance.mapLeftMostX, mapInstance.mapRightMostX) == False: #go to the game over screen!
                #this will draw the game over screen
                life = -1
                turnDirection = "R"
                gameOver = True

        if keys[pygame.K_a]: 
            if mapInstance.turnDirection == "L" and mapInstance.increment == 0:
            #this means that the camera mode will activate!
                mapInstance.cameraMode = True

        if keys[pygame.K_d]: 
            if mapInstance.turnDirection == "R" and mapInstance.increment == 0:
            #this means that the camera mode will activate!
                mapInstance.cameraMode = True
                
        if mapInstance.yMapGameOver == True:
            life = -1
            gameOver = True

        #new player's motion/position
        canvas.fill((135, 206, 235))
        backgroundInstance.drawBackground()
        #print the map:
        #this will also check for collision:
        mapInstance.printingMap(map, playerInstance, True) #this will officially print the map
        indexForMap += 1 #increments every 50 milliseconds
        if indexForMap//9 == len(map):
            #this will increase the scoreMap and obstacleMap:
            print("BACK TO SQUARE 1")
            indexMap = 0
            mapInstance.obstacleMap = mapInstance.obstacleRandomMap("IMPOSSIBLE", map)
            mapInstance.scoreMap = mapInstance.scoreRandomMap("IMPOSSIBLE", map, mapInstance.obstacleMap)
            print(f"IMPOSSIBLE map's obstacleMap = {mapInstance.obstacleMap}")
            print(f"IMPOSSIBLE map's scoreMap = {mapInstance.scoreMap}")
        #updates the location of the player    
        playerInstance.update(centerX, centerY, playerMotionIndex)
        #gameScreen for life and score:
        #update life count 
        gameInstance.drawScore(score)
        gameInstance.drawLife(life)
        #ALWYAS HAVE THIS! This updates the screen
        pygame.display.flip()

    elif gameMode == True:
        playerMotionIndex += 1 #every 0.1 second, the player's motion changes
        backgroundInstance.drawBackground()

        if mapInstance.cameraMode == True:
            if mapInstance.increment >= 8:
                mapInstance.cameraMode = False

        #pygame.event.get() is a list of all the actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False

        #list of pressed keys
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]: 
            centerX -= 10 #changes the position of the player
            #updates the location of the player    
            playerInstance.update(centerX, centerY, playerMotionIndex)
    
            #loop through every obstacle instances in obstacle group:
            for instance in mapInstance.obstacleGroup:
                if instance.isCollision(centerX, centerY):
                    #pastX = centerX
                    centerX = 150 #back to original place
                    life -= 1
                    turnDirection = "L"
                    if life == -1:
                        gameOverMode = True
                    
            #loop through every score instances in score group:
            for instance in mapInstance.scoreGroup:
                if instance.isCollision(centerX, centerY): #passes along the sprite's position
                    centerX = 150
                    score += 1

            #check if the sprite player is out of game map
            if playerInstance.isMapCollision(mapInstance.mapLeftMostX, mapInstance.mapRightMostX) == False: #go to the game over screen!
                #this will draw the game over screen
                life = - 1
                turnDirection = "L"
                gameOver = True

        if keys[pygame.K_RIGHT]:
            centerX += 10 #changes the position of the player
            #updates the location of the player    
            playerInstance.update(centerX, centerY, playerMotionIndex)
            #loop through every obstacle instances in obstacle group:
            for instance in mapInstance.obstacleGroup:
                if instance.isCollision(centerX, centerY):
                    #pastX = centerX
                    centerX = 150 #original centerX
                    life -= 1
                    turnDirection = "R"
                    if life == -1:
                        gameOverMode = True
                    
            #loop through every score instances in score group:
            for instance in mapInstance.scoreGroup:
                if instance.isCollision(centerX, centerY):
                    centerX = 150
                    score += 1
            
            #check if the sprite player is out of game map
            if playerInstance.isMapCollision(mapInstance.mapLeftMostX, mapInstance.mapRightMostX) == False: #go to the game over screen!
                #this will draw the game over screen
                life = -1
                turnDirection = "R"
                gameOver = True

        if keys[pygame.K_a]: 
            if mapInstance.turnDirection == "L" and mapInstance.increment == 0:
            #this means that the camera mode will activate!
                mapInstance.cameraMode = True

        if keys[pygame.K_d]: 
            if mapInstance.turnDirection == "R" and mapInstance.increment == 0:
            #this means that the camera mode will activate!
                mapInstance.cameraMode = True
                
        if mapInstance.yMapGameOver == True:
            life = -1
            gameOver = True

        #new player's motion/position
        canvas.fill((135, 206, 235))
        backgroundInstance.drawBackground()
        #print the map:
        #this will also check for collision:
        mapInstance.printingMap(map, playerInstance, True) #this will officially print the map
        indexForMap += 1 #increments every 50 milliseconds
       
        if indexForMap//9 == len(map):
            gameOverMode = True
        #updates the location of the player    
        playerInstance.update(centerX, centerY, playerMotionIndex)
        #gameScreen for life and score:
        #update life count 
        gameInstance.drawScore(score)
        gameInstance.drawLife(life)
        #ALWYAS HAVE THIS! This updates the screen
        pygame.display.flip() 

#successfully quits the game without an error
pygame.quit()