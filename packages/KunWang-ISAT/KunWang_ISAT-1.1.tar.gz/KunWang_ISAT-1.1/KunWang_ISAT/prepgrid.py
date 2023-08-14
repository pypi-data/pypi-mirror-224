from . import source

class Prepgrid:
    def __init__(self):
        # lat in lcc project
        self.__latin1 = float(33.0)
        self.__latin2 = float(42.0)
        #number of domian
        self.__caseName = '3nestdomain'
        self.__domNum = 3
        #shpfile in ecah domain
        self.__shpath = './shp/mainlandchina.shp,./shp/JJJ.shp,./shp/beijing.shp'.split(',')
        # grid space in ecah domian
        self.__dx = '27000,9000,3000'.split(',')
        # add grid in each domian,
        #xl:left in x direction;xr:right in xdirection;yd:down;yt:top 
        # attention the added grid different directoin muse be equal,eg xladd=xradd
        #in other domian added grid must be  a multiple of dx_parent/dx_son
        self.__xladd = '2,3,3'.split(',')
        self.__xradd = '2,3,3'.split(',')
        self.__ytadd = '2,3,3'.split(',')
        self.__ydadd = '2,3,3'.split(',')
        self.__modelClip = '1,1,1'.split(',')
        self.__domName = 'china,JJJ,beijing'.split(',')


    ### set and get ### 
    def setLatin1(self, latin1):
        self.__latin1 = latin1
    def getLatin1(self):
        return self.__latin1
    
    def setLatin2(self, latin2):
        self.__latin2 = latin2
    def getLatin2(self):
        return self.__latin2
    
    def setCaseName(self, caseName):
        self.__caseName = caseName
    def getCaseName(self):
        return self.__caseName
    
    def setDomNum(self, domNum):
        self.__domNum = domNum
    def getDomNum(self):
        return self.__domNum
    
    def setShpath(self, shpath):
        self.__shpath = shpath.split(',')
    def getShpath(self):
        return self.__shpath
    
    def setDx(self, dx):
        self.__dx = dx.split(',')
    def getDx(self):
        return self.__dx
    
    def setXladd(self, xladd):
        self.__xladd = xladd.split(',')
    def getXladd(self):
        return self.__xladd
    
    def setXradd(self, xradd):
        self.__xradd = xradd.split(',')
    def getXradd(self):
        return self.__xradd
    
    def setYtadd(self, ytadd):
        self.__ytadd = ytadd.split(',')
    def getYtadd(self):
        return self.__ytadd
    
    def setYdadd(self, ydadd):
        self.__ydadd = ydadd.split(',')
    def getYdadd(self):
        return self.__ydadd
    
    def setModelClip(self, modelClip):
        self.__modelClip = modelClip.split(',')
    def getModelClip(self):
        return self.__modelClip
    
    def setDomName(self, domName):
        self.__domName = domName.split(',')
    def getDomName(self):
        return self.__domName
    ### set and get ### 

    def run(self):
        source.main(self.__shpath, self.__latin1, self.__latin2, self.__domNum, self.__dx, self.__xladd, 
             self.__xradd, self.__ytadd, self.__ydadd, self.__modelClip, self.__domName, self.__caseName)

