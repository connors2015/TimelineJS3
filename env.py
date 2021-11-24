'''
env.py
4ier Data Analytics
Nov/23/2021

Author: Chris Connors
'''

import logging
from typing import List
from os import listdir
from re import search, I
from pandas import read_csv, DataFrame

'''
Class that recreates and controls the trading environment
'''
class Env:

    def __init__(self, inputAssetName) -> None:
        self.assetName = inputAssetName
        self.currentStep = 0
        self.currentPrice = 0.0
        self.currentVolume = 0.0
        self.pastPrices = []
        self.pastVolumes = []
        self.log = logging.getLogger('run.env')        
        self.data = DataFrame()

    '''
    Search for asset in /data folder
    If not found handle exception gracefully
    '''
    def create_new_environment(self):

        '''
        Search /data directory for files associated with assetName
        '''
        path = '..\simple_bot\candle_stick_data\{0}\/'.format(self.assetName)
        try:
            files = listdir(path)
        except Exception:
            return self.log.exception('No data directory found for %s.', self.assetName)

        try:
            for lines in files:
                if search('^Binance', lines, I):
                    print(lines)
                    path += lines
        except Exception:
            return self.log.exception('No data file found for %s.', self.assetName)

                
        '''
        Read in data file as a pandas DataFrame
        '''
        self.log.info('Reading data file for %s', self.assetName)

        try:
            self.data = read_csv(path)
        except Exception:
            return self.log.exception('Can not read file for %s', str(path))

        self.log.info('Finished reading data file.')


        '''
        Set current price and volume
        '''
        self.currentPrice = float(self.data.iloc[self.currentStep, 4])
        self.currentVolume = float(self.data.iloc[self.currentStep, 5])

        
    def step(self):
        '''
        Moves the environment forward 1 step
        '''
        self.currentStep += 1

        self.pastPrices.append(self.currentPrice)
        self.pastVolumes.append(self.currentVolume)

        try:
            self.currentPrice = float(self.data.iloc[self.currentStep, 4])
            self.currentVolume = float(self.data.iloc[self.currentStep, 5])
        except Exception:
            return self.log.exception('Problem with step function in environment.')


    '''
    Getter functions for various price and volume queries
    '''    
    def get_current_price(self) -> float:
        return self.currentPrice

    def get_current_step(self) -> int:
        return self.currentStep

    def get_past_price(self, unitsToGoBack) -> float:
        if not self.pastPrices:
            return 0
        elif unitsToGoBack > self.currentStep:
            return self.pastPrices[0]
        else:
            return self.pastPrices[-unitsToGoBack]

    def get_past_price_list(self, unitsToGoBack) -> list:
        if unitsToGoBack > self.currentStep:
            return self.pastPrices
        else:
            return self.pastPrices[-unitsToGoBack:]

    def get_past_volume_list(self, unitsToGoBack) -> list:
        if unitsToGoBack > self.currentStep:
            return self.pastVolumes
        else:
            return self.pastVolumes[-unitsToGoBack:]


    def display(self):
        self.log.info('Current Step: %s\tCurrent Price: %s\tCurrent Volume: %s',self.currentStep, self.currentPrice, self.currentVolume)


def main():

    env = Env()
    env.display()

    return 1

if __name__ == '__main__':
    main()