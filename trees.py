#/usr/bin/python3
#决策树

from math import log

#Calculation Shannon entropy
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
    return



if __name__ == '__main__':
    print("trees \n")
