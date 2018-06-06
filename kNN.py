from numpy import * 
import operator

def createDataSet():
    group = array([  [1.0,1.1],[1.0,1.0],[0,0],[0,0.1]  ])
    labels = ['A','A','B','B']
    return group,labels


'''
对未知类别属性的数据集中的每个点依次执行以下操作：
(1) 计算已知类别数据集中的点与当前点之间的距离；
(2) 按照距离递增次序排序；
(3) 选取与当前点距离最小的k个点；
(4) 确定前k个点所在类别的出现频率；
(5) 返回前k个点出现频率最高的类别作为当前点的预测分类
'''
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]                    #dataSet的列数
    # print("\ndataSetSize :\n",dataSetSize)
    diffMat = tile(inX,(dataSetSize,1)) - dataSet   
    # print("\ndiffMat :\n",diffMat)
    sqDiffMat = (diffMat**2)
    sqDistances = sqDiffMat.sum(axis=1)             #axis＝1表示按照行的方向相加  
    distances = sqDistances**0.5                    #开方
    sortedDistIndicies = distances.argsort()
    # print("\nsortedDistIndicies :\n",sortedDistIndicies)
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
        #print("\nclassCount :\n",classCount)
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True) #从大到小排序classCount第1个域的值
    #print("\nsortedClassCount :\n",sortedClassCount)
    return sortedClassCount[0][0]

def file2matrix(filename):
    rf = open(filename)
    arrayOLines = rf.readlines()        
    numberOfLines = len(arrayOLines)            #得到文件行数 
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()                     #截取掉所有的回车字符
        listFormLine = line.split('\t')         #用字符'\t'分割元素列表
        returnMat[index,:] = listFormLine[0:3]
        classLabelVector.append(int(listFormLine[-1]))  #-1表示最后一个元素
        index+=1
    return returnMat,classLabelVector 



# newValue = (oldValue-min)/(max-min) (归一化 0 - 1)
def autoNorm(dataSet):
    """自动将数字特征值转化到0到1之间"""
    minVals = dataSet.min(0)        #np.min(0)每列中的最小值 np.min(1)每行中的最小值
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]            # dataSet.shape[0] 列数,dataSet.shape[1] 行数
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals


def datingClassTest():
    """测试分类器"""
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('/opt/git_Atom/study_ml/Data/Ch02/datingTestSet2.txt')
    normMat,ranges,minvals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],4)
        print ("the classifier came back with :%d ,the real answer is:%d\n"%(classifierResult,datingLabels[i]))
        if(classifierResult != datingLabels[i]):
            errorCount += 1.0
    print ("the total error rate is %f\n"%(errorCount/float(numTestVecs)))

def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffmiles = float(input("frequent filer miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix('/opt/git_Atom/study_ml/Data/Ch02/datingTestSet2.txt')
    normMat,ranges,minvals = autoNorm(datingDataMat)
    inArr = array([ffmiles,percentTats,iceCream])
    classifierResult = classify0((inArr-minvals)/ranges,normMat,datingLabels,3)
    print ("You will probably like this person :",resultList[classifierResult-1])

#手写数字识别
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect
