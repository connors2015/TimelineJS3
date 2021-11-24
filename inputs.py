'''
inputs.py
4ier Data Analytics
Nov/23/2021

Author: Chris Connors
'''

import numpy as np
from env import Env
from trade import Trading
import logging

class Inputs:

    def __init__(self, inputEnv, inputTrade) -> None:
        self.env = inputEnv
        self.trade = inputTrade
        self.log = logging.getLogger('run.agent.inputs')        

    def get_inputs_list(self):
        return self.listOfInputs

    '''
    Returns a previous price.
    '''
    def past_price2(self):
        return self.env.get_past_price(2)

    def past_price5(self):
        return self.env.get_past_price(5)

    def past_price10(self):
        return self.env.get_past_price(10)

    def past_price15(self):
        return self.env.get_past_price(15)

    def past_price30(self):
        return self.env.get_past_price(30)

    def past_price60(self):
        return self.env.get_past_price(60)

    def past_price120(self):
        return self.env.get_past_price(120)

    def past_price240(self):
        return self.env.get_past_price(240)

    '''
    Calculate average over distance lengthBack
    inputs: environment (Env), lengthBack (int)
    returns: average (float)
    '''
    def moving_average5(self) -> float:
        return np.average(self.env.get_past_price_list(5))
    
    def moving_average7(self) -> float:
        return np.average(self.env.get_past_price_list(7))

    def moving_average15(self) -> float:
        return np.average(self.env.get_past_price_list(15))

    def moving_average30(self) -> float:
        return np.average(self.env.get_past_price_list(30))

    def moving_average60(self) -> float:
        return np.average(self.env.get_past_price_list(60))

    def moving_average120(self) -> float:
        return np.average(self.env.get_past_price_list(120))

    def moving_average240(self) -> float:
        return np.average(self.env.get_past_price_list(240))

    def moving_average_vol5(self) -> float:
        return np.average(self.env.get_past_volume_list(5))
    
    def moving_average_vol7(self) -> float:
        return np.average(self.env.get_past_volume_list(7))

    def moving_average_vol15(self) -> float:
        return np.average(self.env.get_past_volume_list(15))

    def moving_average_vol30(self) -> float:
        return np.average(self.env.get_past_volume_list(30))

    def moving_average_vol60(self) -> float:
        return np.average(self.env.get_past_volume_list(60))

    def moving_average_vol120(self) -> float:
        return np.average(self.env.get_past_volume_list(120))

    def moving_average_vol240(self) -> float:
        return np.average(self.env.get_past_volume_list(240))



    '''
    Calculates Gradients of past prices
    '''
    def gradient5(self):
        try:
            return sum(np.gradient(self.env.get_past_price_list(5)))
        except ValueError:
            return [x for x in range(5)]

    def gradient10(self):
        try:
            return sum(np.gradient(self.env.get_past_price_list(10)))
        except ValueError:
            return [x for x in range(10)]

    def gradient15(self):
        try:
            return sum(np.gradient(self.env.get_past_price_list(15)))
        except ValueError:
            return [x for x in range(15)]

    def gradient30(self):
        try:
            return sum(np.gradient(self.env.get_past_price_list(30)))
        except ValueError:
            return [x for x in range(30)]

    def gradient60(self):
        try:
            return sum(np.gradient(self.env.get_past_price_list(60)))
        except ValueError:
            return [x for x in range(60)]

    def gradient120(self):
        try:
            return sum(np.gradient(self.env.get_past_price_list(120)))
        except ValueError:
            return [x for x in range(120)]

    def gradient240(self):
        try:
            return sum(np.gradient(self.env.get_past_price_list(240)))
        except ValueError:
            return [x for x in range(240)]

    '''
    Resistance points
    '''
    def high_resistance_point(self) -> int:    
        self.log.debug('complete high_resistance_point function')
        return 10

    def low_resistance_point(self) -> int:
        self.log.debut('complete Low_resistance_point function')
        return 10

        
    '''
    Agent related inputs
    '''
    def total_fees(self) -> float:
        return self.trade.get_total_fees()

    def total_revenue(self) -> float:
        return self.trade.get_total_revenue()

    def number_of_trades(self) -> int:
        return self.trade.get_total_trades()

    def get_capital(self) -> float:
        return self.trade.get_capital()

    '''
    Distance in price between now and when trade started
    '''
    def distance_from_current_price(self) -> float:
        if self.trade.inLong or self.trade.inShort:
            return abs(self.env.get_current_price() - self.trade.get_in_price())
        else:
            return 0
