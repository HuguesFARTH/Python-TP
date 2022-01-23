import json
"""
TODO: Gérer l'utilisation de différents niveaux
"""
class Level:

    def __init__(self,monsterSpawnPoint = None, maxMonsters = None, blocksInfo = None, playerLife = None):
        #Chaque element de cette liste est une liste du format [[x,y],bossProba(0-1000),shooterProba(0-1000),tempMinSpawn(ms),tempMaxSpawn(ms),self.lastSpawn]
        self.monsterSpawnPoint =  [[[50,100],100,500,1000,2000,0]] if monsterSpawnPoint == None else monsterSpawnPoint
        self.maxMonsters = 10 if maxMonsters == None else maxMonsters
        self.playerLife = 10 if playerLife == None else playerLife
        #Chaque element de cette liste est une liste du format [[x,y],life]
        self.blocksInfo = [] if blocksInfo == None else blocksInfo
        if blocksInfo == None:
            self.initDefault()

    def initDefault(self):
        self.addBlocks(20)

    def addBlocks(self,amount):
        pos =  [15+30 * amount, 200]
        self.blocksInfo.append([pos,4])
        amount -= 1
        if amount > 0:
            self.addBlocks(amount)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def saveLevel(self,saveName):
        with open("levels/"+saveName+".json", 'w') as f:
            f.write(self.toJSON())

def loadLevel(saveName):
    with open("levels/"+saveName+".json", 'r') as f:
        data = json.load(f)
        print()
        return Level(monsterSpawnPoint = data['monsterSpawnPoint'], maxMonsters = data['maxMonsters'], blocksInfo = data['blocksInfo'], playerLife = data['playerLife'])
    return Level()

# saveName = "level_1"
# d = loadLevel(saveName)
# print(d.toJSON())
