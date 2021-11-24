'''
neuralnetwork.py
4ier Data Analytics
Nov/23/2021

Author: Chris Connors
'''
import genetics
import inputs
#from keras.layers import LSTM, Dense

class NeuralNetwork():

    def __init__(self, input_genetics, inputIdentifier) -> None:
        self.identifier = inputIdentifier
        self.genetics = input_genetics
        self.numberOfInputs = self.genetics.numberOfInputs
        self.numberOfHiddenLayers = self.genetics.numberOfHiddenLayers
        self.chosenInputsList = list

    def create_neural_network():
        '''
        Choose random inputs from enumerated list

        Create neural network to take in those inputs

        Add hidden layers

        Outputs should be BUY, SELL, HOLD(?)
        '''
        LSTM(self.numberOfInputs)

        ##DON'T FORGET TO SAVE THE MODEL SOMEWHERE
        return 1


    def train_network():
        return 1

    def update_network():
        '''Network should be able to call inputs of varying numbers'''
        return 1

    def get_outputs():
        return 1