__author__ = 'shilpagulati'



import sys
import math
import heapq
from copy import deepcopy
# reading input File

IrisData=[]

no_clusters=int(sys.argv[2])
input=open(sys.argv[1])
for line in input:
    temp = []
    line = line.strip('\n')
    line = line.split(',')
    for each in line:
        temp.append(each)
    IrisData.append(temp)
# print IrisData

#compute  distances between 2 points

def distance(point1,point2):
    dist = 0.0
    dist = math.sqrt(sum((point1[i] - point2[i])**2 for i in range(0,len(point1))))
    return dist


# compute centroid of points
def Centroid(points):

    values=[]
    for eachP in points:

        values.append(GivenClusterDict[eachP])
    length_coordinate=len(values)
    length = len(values[0])
    temp = []
    for j in range(0,length):
            coord = 0
            for each in values:

                coord += each[j]
            temp.append(coord/length_coordinate)

    return temp



# make a dictionary of clusters and heap of all distances.

ClusterDict = {}
count = 0
for k in range(0, len(IrisData)):
    count += 1
    temp = []
    for i in range(0, len(IrisData[k])-1):
        temp.append(float(IrisData[k][i]))
    ClusterDict[str(k)] = temp


GivenClusterDict = deepcopy(ClusterDict)

# store all the clusters

ClusterList=[]
for key in ClusterDict.iterkeys():
        ClusterList.append(key)



# make heap based on clusters in the list

def makeheap(Clusterlist, Clusterdict):

    DistanceHeap=[]

    for i in range(0,len(Clusterlist)):
            for j in range(i+1,len(Clusterlist)):


                heapq.heappush(DistanceHeap,[distance(Clusterdict[Clusterlist[i]],Clusterdict[Clusterlist[j]]),str(Clusterlist[i]),str(Clusterlist[j])])
    return  DistanceHeap

def Clustering(Clusterlist,Clusterdict):

    while len(Clusterlist) > no_clusters:

        DistanceHeap = makeheap(Clusterlist, Clusterdict)


        smallestP = heapq.heappop(DistanceHeap)



        centroidPoints=[]
        if smallestP[1] in Clusterlist and smallestP[2] in Clusterlist:

            Clusterlist.remove(smallestP[1])
            Clusterlist.remove(smallestP[2])
            Clusterlist.append(smallestP[1]+"_"+smallestP[2])
            centroidPoints = Clusterlist[-1].split("_")

            Clusterdict[smallestP[1]+"_"+smallestP[2]] = Centroid(centroidPoints)

            del Clusterdict[smallestP[1]]
            del Clusterdict[smallestP[2]]

        else:

            heapq.heappop()
            continue
    return Clusterlist


FinalCluster = Clustering(ClusterList,ClusterDict)
totalPredicted = 0.0
predictedCorrect = 0.0

FinalOutput = []
for each in FinalCluster:
    each = each.split("_")

    each = [int(x) for x in each]
    each.sort()
    FinalOutput.append(each)
    for i in range(0, len(each)):
        for j in range(i+1,len(each)):
            if IrisData[each[i]][-1] == IrisData[each[j]][-1]:
                predictedCorrect += 1
    for k in range(0,len(each)):
        for m in range(k+1,len(each)):
                totalPredicted += 1



totalCorrect = 0.0
for i in range(0,len(IrisData)):
    for j in range(i+1,len(IrisData)):
        if IrisData[i][-1] == IrisData[j][-1]:
            totalCorrect += 1
if totalPredicted==0.0:
    precision=0.0
else:

    precision = predictedCorrect/totalPredicted

print precision
if totalCorrect==0.0:
    recall=0.0
else:


    recall = predictedCorrect/totalCorrect
print recall
for each in FinalOutput:
    print each









