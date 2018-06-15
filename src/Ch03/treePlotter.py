#/usr/bin/python3
#决策树
import matplotlib.pyplot as plt 
#from pylab import *    
#mpl.rcParams['font.sans-serif'] = ['SimHei']   


decisionNode = dict(boxstyle="sawtooth",fc="0.8") 	#定义文本框和箭头格式
leafNode = dict(boxstyle="round4",fc="0.8")
arrow_arge = dict(arrowstyle="<-")

"""
绘制带箭头的注解
@nodeTxt:TEXT
@center:文字中心
@parentPt:箭头起始位置
@nodeType:样式
"""
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
	createPlot.axl.annotate(nodeTxt,xy=parentPt,xycoords="axes fraction",
							xytext=centerPt,textcoords="axes fraction",va="center",
							ha="center",bbox=nodeType,arrowprops=arrow_arge)

def createPlot():
	fig = plt.figure(1,facecolor="white")
	fig.clf()
	createPlot.axl = plt.subplot(111,frameon=False)
	plotNode('a decision node',(0.5,0.1),(0.1,0.5),decisionNode)
	plotNode('a leaf node',(0.8,0.1),(0.3,0.8),leafNode)
	plt.show()

#获取叶节点的数目
def getNumLeafs(myTree):
	numLeafs = 0
	firstStr = list(myTree.keys())[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':
			numLeafs += getNumLeafs(secondDict[key])
		else: numLeafs += 1
	return numLeafs

#获取数的层数
def getTreeDepth(myTree):
	maxDepth = 0
	firstStr = list(myTree.keys())[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			thisDepth = 1 + getTreeDepth(secondDict[key])
		else : thisDepth = 1
		if thisDepth > maxDepth: maxDepth = thisDepth
	return maxDepth

def retrieveTree(i):
	listOfTrees = [{'no surfacing':{0:'no',
									1:{'flippers':{0:'no',
												   1:'yes'}}}},
					{'no surfacing':{0:'no',
									1:{'flippers':{0:{'head':{0:'no',1:'yes'}},
												   1:'no'}}}}]	
	return listOfTrees[i]											   

def plotMidText(cntrPt,parentPt,txtString):
	"""在父子节点之间填充文本信息 """
	xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
	yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
	createPlot.axl.text(xMid,yMid,txtString)

def plotTree(myTree,parentPt,nodeTxt):
	numLeafs = getNumLeafs(myTree)  			#计算宽与高
	depth = getTreeDepth(myTree)
	firstStr = list(myTree.keys())[0]
	cntrPt = (plotTree.xOff + (1.0+float(numLeafs))/2.0/plotTree.totalW,plotTree.yOff )
	plotMidText(cntrPt,parentPt,nodeTxt)
	plotNode(firstStr,cntrPt,parentPt,decisionNode)
	secondDict = myTree[firstStr]
	plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			plotTree(secondDict[key],cntrPt,str(key))
		else:
			plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
			plotNode(secondDict[key],(plotTree.xOff,plotTree.yOff),cntrPt,leafNode)
			plotMidText((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
	plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

def createplot(inTree):
	fig = plt.figure(1,facecolor='white')
	fig.clf()
	axprops = dict(xticks=[],yticks=[])
	createPlot.axl = plt.subplot(111,frameon=False,**axprops)
	plotTree.totalW = float(getNumLeafs(inTree))
	plotTree.totalD = float(getTreeDepth(inTree))
	plotTree.xOff = -0.5/plotTree.totalW;   plotTree.yOff = 1.0;
	plotTree(inTree,(0.5,1.0),'')
	plt.show()




if __name__ == '__main__':
	print (plt.style.available)		#获取所有的自带样式 
	plt.style.use("seaborn-ticks") 			#使用自带的样式进行美化 
	#createPlot();
	#print (getNumLeafs({'filppers': {0: 'no', 1: 'yes'}}))
	myTree = retrieveTree(0)
	# print ("myTree\n",myTree) 
	# print("getNumLeafs(myTree)\n",getNumLeafs(myTree))
	# print("getTreeDepth(myTree)\n",getTreeDepth(myTree))
	# createplot(myTree)
	
