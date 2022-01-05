class Level:
    def __init__(self):
        self.monsterSpawnPoint = [50,100] #Chaque element de cette liste est une liste du format [[x,y],bossProba(0-1000),shooterProba(0-1000),tempMinSpawn(ms),tempMaxSpawn(ms),self.lastSpawn]
        self.maxMonsters = 10
        self.blocksInfo = [] #Chaque element de cette liste est une liste du format [[x,y],life]
        self.initDefault()

    def initDefault(self):
        for i in range(0, 20):
            pos =  [15+60 * i, 200]
            self.blocksInfo.append([pos,4])
