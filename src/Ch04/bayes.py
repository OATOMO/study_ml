#coding utf-8
from numpy import *
import re
def loadDataSet():
	"""词表到向量的转换函数"""
	postingList = [['my','dog','has','flea','problems','help','please'],
				   ['maybe','not','take','him','to','dog','park','stupid'],
				   ['my','dalmation','is','so','cute','I','love','him'],
				   ['stop','posting','stupid','worthless','garbage'],
				   ['mr','licks','ate','my','steak','how','to','stop','him'],
				   ['quit','buying','worthless','dog','food','stupid']]
	classVec = [0,1,0,1,0,1]  #1代表侮辱性词汇,0代表正常言论
	return postingList,classVec

#会创建一个包含在所有文档中出现的不重复词的列表
def createVocabList(dataSet):
	vocabSet = set([])						#创建一个空集
	for document in dataSet:
		vocabSet = vocabSet | set(document)	#创建两个集合的并集
	return list(vocabSet)

#输入参数为词汇表及某个文档，输出的是文档向量
def setOfWords2Vec(vocabList,inputSet):
	returnVec = [0]*len(vocabList)			#创建一个所有元素都为0的向量
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else: print("the word : %s is not in my Vocabulary!"%word)
	return returnVec

def bagOfWords2VecMN(vocabList,inputSet):
	"""朴素贝叶斯词带模型"""
	returnVec = [0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] += 1
	return returnVec

"""
input:
	@trainMatrix  :文档矩阵
	@trainCategory:文档类别向量
"""
def trainNB0(trainMatrix,trainCategory):
	"""朴素贝叶斯分类器训练函数"""
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])
	pAbusive = sum(trainCategory)/float(numTrainDocs)  		#P(c1)
	p0Num = ones(numWords); p1Num = ones(numWords)
	p0Denom = 2.0; p1Denom = 2.0
	for i in range(numTrainDocs):
		if trainCategory[i] == 1:
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
		else :
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
	p1Vect = log(p1Num/p1Denom)		#change to log()
	p0Vect = log(p0Num/p0Denom)		#change to log()
	return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
	"""朴素贝叶斯分类函数"""
	p1 = sum(vec2Classify * p1Vec) + log(pClass1)
	p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
	if p1 > p0 :
		return 1
	else:
		return 0

def testingNB():
	listOPosts,listClasses = loadDataSet()
	myVocabList = createVocabList(listOPosts)
	trainMat = []
	for postinDoc in listOPosts:
		trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
	p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
	testEntry = ['love','my','dalmation']
	thisDoc = array(setOfWords2Vec(myVocabList,testEntry))
	print( testEntry,'classified as : ',classifyNB(thisDoc,p0V,p1V,pAb))
	testEntry = ['stupid','garbage']
	thisDoc = array(setOfWords2Vec(myVocabList,testEntry))
	print( testEntry,'classified as : ',classifyNB(thisDoc,p0V,p1V,pAb))



if __name__ == '__main__':
	# listOPosts,listClasses = loadDataSet()
	# myVocabList = createVocabList(listOPosts)
	# print (myVocabList)
	# print (setOfWords2Vec(myVocabList,listOPosts[0]))
	# print (setOfWords2Vec(myVocabList,listOPosts[3]))		
	# trainMat = []
	# for postinDoc in listOPosts:
	# 	trainMat.append(setOfWords2Vec(myVocabList,postinDoc))

	# p0V,p1V,pAb = trainNB0(trainMat,listClasses)
	# print (pAb)
	# print (p1V)
	testingNB()
