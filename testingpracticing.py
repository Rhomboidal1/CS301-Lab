'''
Created on Feb 25, 2016

@author: Rhomboidal
'''
import math

#math.sqrt( (1/(n-1)) * sum()
L=[2,4,4,4,5,5,7,9]
var1 = range(len(L))
var_sq = range(len(var1))
std_dev = 0
def mean(L):
    tot=sum(L)
    '''for x in xrange(0,len(L)):
        tot=L[x]+tot
    print tot
    print len(L)
    print type(tot)
    if type(tot) == int:
        val = tot / len(L)
        print val
        return val
    elif type(tot) == float:
        val = float(tot)/len(L)
        print val
        return val'''
    val = tot / len(L)
    return val
def variance(L):
    for x in xrange(0, len(L)):
        temp = (L[x] - mean(L))
        var1[x] = temp
    return var1
def variance_sq(var1):
    for x in xrange(0, len(var1)):
        temp2 = (var1[x]**2)
        var_sq[x] = temp2
    return var_sq
def std(L):
    var_sq = variance_sq(variance(L))
    sumvarsq = sum(var_sq)
    print sumvarsq
    print len(var1)
    std_dev = math.sqrt((1/(float(len(var1)-1)))*float(sumvarsq))
    return std_dev
def remove_outliers(L, sd):
    std_dev_ro = std(L)
    withindev = (sd*std_dev_ro)
    varian = variance(L)
    mean_ro = mean(L)
    for x in sorted(varian, reverse=True):
        print 'index:' + str(x)
        print abs(x)
        if (abs(x))>(sd*std_dev_ro):
            print 'Current list:' + str(L)
            temp_index = L[x]
            temp_list = []
            temp_list.append(temp_index)
            print temp_list
            print 'New list:' + str(L)
        elif (abs(varian[x]))<=(sd*std_dev_ro):
            print L
            print L[x]
            print x
            print 'No change'
            
        '''if (abs(varian[x]))>(sd*std_dev_ro):
            print 'Current list:' + str(L)
            print std_dev_ro
            del L[x]
            print 'New list:' + str(L)
        elif (abs(varian[x]))<=(sd*std_dev_ro):
            print L
            print L[x]
            print x
            print 'No change'''
    return L
print L
print mean(L)
print variance(L)
print variance_sq(var1)
print std(L)
print remove_outliers(L, 1)