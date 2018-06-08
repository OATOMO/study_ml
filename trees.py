#/usr/bin/python3
#决策树

from math import log

#Calculation Shannon entropy
#entropy 越高,则混合的数据也就越多
def calcShannonEnt(dataSet):
    """计算给定数据集的香农熵"""
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():      #labelCount.keys()中不包含currentLabel
            labelCounts[currentLabel] = 0               #为所有可能的分类创建字典
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]/numEntries)       #以2为底,求对数
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

def createDataSet():
    dataSet = [[1,1,'yes'], 
               [1,1,'yes'],
               [0,0,'no' ],
               [0,0,'no' ],
               [1,0,'no' ],]
    labels = ['no surfacing','filppers']
    return dataSet,labels

"""
@dataSet:待划分的数据集
@asix   :划分数据集的特征
@value  :特征的返回值
"""
def splitDataSet(dataSet,axis,value):
    """按照给定特征划分数据集"""
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])     #extend()函数用于在列表末尾一次性追加另一个序列的多个值
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    """选择最好的数据集划分方式"""
    numFeature = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0;baseFeature = -1
    for i in range(numFeature):                         
        featList = [example[i] for example in dataSet]   #创建唯一的分类标签列表
        uniqueVals = set(featList)                       #所以数据的第i列特征
        newEntropy = 0.0
        for value in uniqueVals:                         #计算每种划分方式的信息熵
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):                     #计算最好的信息增益  
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

if __name__ == '__main__':
    print("trees \n")
    myDat,labels=createDataSet()
    #myDat[0][-1] = 'maybe'
    #print ("shannonEnt -> %f\n"%(calcShannonEnt(myDat)))
    #print (splitDataSet(myDat,0,1))
    #print (splitDataSet(myDat,0,0))
    print (chooseBestFeatureToSplit(myDat))
