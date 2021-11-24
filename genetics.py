'''
genetics.py
4ier Data Analytics
Nov/23/2021

Author: Chris Connors
'''
from dataclasses import dataclass


@dataclass
class Genetics:
    numberOfInputs = 3
    numberOfHiddenLayers = 1
    inputList: list
    outputLIst: list


'''
Helper function to combine genetics of two agents

Input: 
byteArray, byteArray

Output:
byteArray
'''
def get_combined_genetics(inputGenetics1, inputGenetics2):
    genetics1 = inputGenetics1
    genetics2 = inputGenetics2
    newGenetics = genetics1 + genetics2
    return newGenetics

def create_new_genetics():
        return Genetics

def main():

    randomMutationChance = 0.0

    return 1