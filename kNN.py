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
    print("\ndataSetSize :\n",dataSetSize)
    diffMat = tile(inX,(dataSetSize,1)) - dataSet   
    print("\ndiffMat :\n",diffMat)
    sqDiffMat = (diffMat**2)
    sqDistances = sqDiffMat.sum(axis=1)             #axis＝1表示按照行的方向相加  
    distances = sqDistances**0.5                    #开方
    sortedDistIndicies = distances.argsort()
    print("\nsortedDistIndicies :\n",sortedDistIndicies)
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
        print("\nclassCount :\n",classCount)
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True) #从大到小排序classCount第1个域的值
    print("\nsortedClassCount :\n",sortedClassCount)
    return sortedClassCount[0][0]

