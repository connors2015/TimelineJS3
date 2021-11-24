'''
agent.py
4ier Data Analytics
Nov 23 2021

Author: Chris Connors
'''
import env
import genetics
import inputs
import trade
import neuralnetwork
import random
import uuid
import logging

class Agent:

    def __init__(self, inputSplitTime, inputEnv) -> None:
        '''
        Initialize the agents genetics then create a neural network with them.
        User inputs splitTime argument
        '''
        self.log = logging.getLogger('run.agent')
        self.identifier = uuid.uuid1()
        self.genetics = genetics.create_new_genetics()
        self.neuralNetwork = neuralnetwork.NeuralNetwork(self.genetics, self.identifier)
        self.trade = trade.Trading(inputEnv, self.identifier)
        self.splitTime = inputSplitTime
        self.inputs = inputs.Inputs(inputEnv, self.trade)
        method_list = [method for method in dir(inputs.Inputs) if method.startswith('_') is False]
        self.listOfInputs = random.sample(method_list,self.genetics.numberOfInputs)

        '''
        Variables for keeping track of trading profits, trades, etc.
        '''
        self.profit = 0.0
        self.inTrade = False

    '''
    Agent updates the inputs for it's neural network then calls update to run
    the work and get new output actions
    '''
    def update_inputs(self) -> list:
        '''
        Run the required inputs and store their outputs
        '''
        self.log.debug(self.listOfInputs)
        outputs = []
        for items in self.listOfInputs:
            method = (getattr(self.inputs, items))
            outputs.append(method())
        self.log.debug(outputs)
        return outputs


    def get_genetics(self):
        return self.genetics

    def create_neural_network(self):
        return 1

    def update(self):
        print('buying long')
        self.trade.buy_long()
        print('selling long')
        self.trade.sell_long()

    def print(self):
        print('I\'m agent: ', self.identifier)