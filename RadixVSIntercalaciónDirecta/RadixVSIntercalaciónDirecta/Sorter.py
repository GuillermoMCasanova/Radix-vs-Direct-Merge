#Universidad de las Fuerzas Armadas ESPE
#Desarrollado por Memo Casanova, Alan Quimbita y Joyce Castro
#Fecha de Creación 09/11/2018
#Fecha de Modificación 16/11/2018

import matplotlib.pyplot as plt
from random import randint
from time import time
import os
import sys
from timeit import timeit
import curses

class Sorter():
    def __init__(self):
        pass

    def generateList(self, size, minValue, MaxValue):
        return list(randint(minValue,MaxValue) for i in range(size))

    def radixSort(self, array):
        arrayA=list(i for i in array if i<0)
        arrayB=list(i for i in array if i>=0)
        if(len(arrayA)>0):
            for i in range(len(str(abs(min(arrayA))))):
                bins = list(list() for x in range(10))
                for j in arrayA:
                    bins[int((j / 10 ** i) % 10)].append(j)
                arrayA = list()
                for section in bins:
                    arrayA.extend(section)
        if(len(arrayB)>0):
            for i in range(len(str(max(arrayB)))):
                bins = list(list() for x in range(10))
                for j in arrayB:
                    bins[int((j / 10 ** i) % 10)].append(j)
                arrayB = list()
                for section in bins:
                    arrayB.extend(section)
        arrayA.extend(arrayB)
        return arrayA

    def merge(self, left, right):
        result = list()
        while(len(left) > 0 and len(right) > 0):
            if (left[0] <= right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if(len(left) > 0):
            result += left
        if(len(right) > 0):
            result += right
        return result

    def mergeSort(self, array):
        left = list()
        right = list()
        if(len(array) <= 1):
            return array
        else:
            middle = int(len(array) / 2)
            middle-=1
            for i in range(middle + 1):
                left.append(array[i])
            for i in range(middle + 1, len(array)):
                right.append(array[i])
            left = self.mergeSort(left)
            right = self.mergeSort(right)
            result = self.merge(left, right)
            return result