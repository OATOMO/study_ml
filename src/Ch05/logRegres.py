#coding utf-8
#!/usr/bin/python3
from math import * 
from numpy import *
"""
优点：计算代价不高，易于理解和实现。
缺点：容易欠拟合，分类精度可能不高。
适用数据类型：数值型和标称型数据。
 * 	Sigmoid函数看起来很像一个阶跃函数,Sigmoid函数的输入记为z，由下面公式得出：
	z = w0x0 + w1x1 + w2X2 + ... wnxn
"""

def loadDataSet():
	dataMat = [];labelMat = []
	fr = open('testSet.txt')
	for line in fr.readlines():
		lineArr = line.strip().split()
		dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])	#[偏置,特征1,特征2]
		labelMat.append(int(lineArr[2]))
	return dataMat,labelMat

def sigmoid(inX):
	return 1.0/(1+exp(-inX))

"""
	@weights	:权重
	@alpha		:步长
	@maxCycles	:迭代次数
"""
def gradAscent(dataMatIn,classLabels):
	"""logistic回归梯度优化算法"""
	dataMatrix = mat(dataMatIn)			#转换为numpy矩阵数据类型
	labelMat = mat(classLabels).transpose() 
	m,n = shape(dataMatrix)   	;print ("(m x n = %d x %d)"%(m,n))
	alpha = 0.001					#步长α
	maxCycles = 500
	weights = ones((n,1))
	# m1,n1 = shape(weights)   	;print ("(m1 x n1 = %d x %d)"%(m1,n1))
	for k in range(maxCycles):
		h = sigmoid(dataMatrix*weights)	
		error = (labelMat-h)	#这里是在计算真实类别与预测类别的差值，接下来就是按照该差值的方向调整回归系数
		weights = weights + alpha * dataMatrix.transpose() * error
	return weights

def stocGradAscent0(dataMatrix,classLabels):
	"""随机梯度上升算法"""
	m,n = shape(dataMatrix)
	alpha = 0.01
	weights = ones(n)
	for i in range(m):
		h = sigmoid(sum(dataMatrix[i]*weights))
		error = classLabels[i]-h
		weights = weights + alpha * error * dataMatrix[i]
	return weights

def stocGradAscent1(dataMatrix,classLabels,numIter = 150):
	"""改进的随机梯度上升算法"""
	m,n = shape(dataMatrix)
	weights = ones(n)
	for j in range(numIter):	
		dataIndex = range(m)
		for i in range(m):
			alpha = 4/(1.0+j+i) + 0.01
			randIndex = int(random.uniform(0,len(dataIndex)))
			h = sigmoid(sum(dataMatrix[randIndex]*weights))
			error = classLabels[randIndex] - h
			weights = weights + alpha * error * dataMatrix[randIndex]
			# del(dataIndex[randIndex])
			del(list(dataIndex)[randIndex])
	return weights

def plotBestFit(wei):
	"""画出数据集和logistic回归最佳拟合直线函数"""
	import matplotlib.pyplot as plt
	# weights = wei.getA()
	dataMat,labelMat=loadDataSet()
	dataArr = array(dataMat)
	n = shape(dataArr)[0]
	xcord1 = [];ycord1 = []
	xcord2 = [];ycord2 = []
	for i in range(n):
		if int(labelMat[i]) == 1:
			xcord1.append(dataArr[i,1]);ycord1.append(dataArr[i,2])
		else:
			xcord2.append(dataArr[i,1]);ycord2.append(dataArr[i,2])
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xcord1,ycord1,s = 30,c='red',marker='s')
	ax.scatter(xcord2,ycord2,s = 30,c='green')
	x = arange(-3.0,3.0,0.1)
	y = (-weights[0] - weights[1]*x)/weights[2]	#0 = w0+w1x+w2y
	ax.plot(x,y)
	plt.xlabel('X1');plt.ylabel('X2');
	plt.show()


if __name__ == '__main__':
	dataArr,labelMat=loadDataSet()
	# weights =  gradAscent(dataArr,labelMat)
	# plotBestFit(weights)

	# weights = stocGradAscent0(array(dataArr),labelMat)
	# plotBestFit(weights)
	# print (weights,type(weights))

	weights = stocGradAscent1(array(dataArr),labelMat,500)
	plotBestFit(weights)
	