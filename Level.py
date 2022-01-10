import json

class Level:
    def __init__(self,monsterSpawnPoint = None, maxMonsters = None, blocksInfo = None, playerLife = None):
        self.monsterSpawnPoint =  [[[50,100],100,500,1000,2000,0]] if monsterSpawnPoint == None else monsterSpawnPoint #Chaque element de cette liste est une liste du format [[x,y],bossProba(0-1000),shooterProba(0-1000),tempMinSpawn(ms),tempMaxSpawn(ms),self.lastSpawn]
        self.maxMonsters = 10 if maxMonsters == None else maxMonsters
        self.playerLife = 10 if playerLife == None else playerLife
        self.blocksInfo = [] if blocksInfo == None else blocksInfo #Chaque element de cette liste est une liste du format [[x,y],life]
        if blocksInfo == None:
            self.initDefault()

    def initDefault(self):
        for i in range(0, 20):
            pos =  [15+30 * i, 200]
            self.blocksInfo.append([pos,4])

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

saveName = "level_1"
d = loadLevel(saveName)
print(d.toJSON())
