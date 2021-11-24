'''
trading.py
4ier Data Analytics
Nov/23/2021

Author: Chris Connors
'''

import env
import logging
from enum import Enum

class TradeType(Enum):
    IN_LONG = 0
    IN_SHORT = 1
    OUT_LONG = 2
    OUT_SHORT = 3

class Trading:

    def __init__(self, inputEnviroment, inputIdentifier) -> None:
        self.env = inputEnviroment
        self.identifier = inputIdentifier
        self.inLong = False
        self.inShort = False
        self.inLongPrice = 0.0
        self.inShortPrice = 0.0
        self.outLongPrice = 0.0
        self.outShortPrice = 0.0
        self.totalFees = 0.0
        self.feePercent = 0.001
        self.totalRevenue = 0.0
        self.totalProfit = 0.0
        self.inTradeStep = 0
        self.outTradeStep = 0
        self.capital = 100
        self.assetAmount = 0.0
        self.totalTrades = 0
        self.log = logging.getLogger('run.agent.trade')

    def buy_long(self) -> bool:

        if not self.inLong and not self.inShort:

            self.inLong = True
            self.inLongPrice = self.env.get_current_price()     
            self.inTradeStep = self.env.get_current_step()

            '''
            Calculate fees and subtract them from capital
            '''       
            feesOwed = self.capital * self.feePercent
            self.capital -= feesOwed
            self.totalFees += feesOwed

            '''
            Set new assetAmount and set capital to zero
            '''
            self.assetAmount = (self.capital / self.inLongPrice)
            self.capital = 0

            self.log.info('Agent: %s\tTrade Type: %s\t In Step: %s\tIn Long Price: %s\tFees paid: %f\tAsset Amount: %f', \
                str(self.identifier), TradeType(0), self.inTradeStep, self.inLongPrice, feesOwed, self.assetAmount)  

            return True

        else:
            return False

    def buy_short(self) -> bool:

        if not self.inShort and not self.inLong:

            self.inShort = True
            self.inShortPrice = self.env.get_current_price()
            self.inTradeStep = self.env.get_current_step()

            '''
            Calculate fees and subtract them from capital
            '''
            feesOwed = self.capital * self.feePercent
            self.capital -= feesOwed

            '''
            Set new assetAmount and set capital to zero
            '''
            self.assetAmount = (self.capital / self.inShortPrice)
            self.capital = 0    

            self.log.info('Agent: %s\tTrade Type: %s\t In Step: %s\tIn Short Price: %s\tFees paid: %f\tAsset Amount: %f', \
                str(self.identifier), TradeType(1), self.inTradeStep, self.inShortPrice, feesOwed, self.assetAmount)      

            return True

        else:
            return False
 
    def sell_long(self):
        if self.inLong:
            '''
            Get out of a long position
            Record env current price as outLongPrice
            '''
            self.inLong = False
            self.outLongPrice = self.env.get_current_price()
            self.outTradeStep = self.env.get_current_step()

            '''
            Calculate revenue, calculate fees in asset (BTC/ETH/etc), calculate new capital
            '''
            revenue = self.outLongPrice - self.inLongPrice
            feesOwed = self.assetAmount * self.feePercent

            self.assetAmount -= feesOwed
            self.capital = (self.outLongPrice * self.assetAmount)


            '''
            Add to cumulative revenue set capital to zero
            '''
            self.totalRevenue += revenue
            self.assetAmount = 0
            self.totalTrades += 1



            self.log.info('Agent: %s\tTrade Type: %s\t In Step: %s\tIn Long Price: %s\tOut Step: %s\tOut Long Price: %s\tRevenue: %f\tFees paid: %f\tCapital: %f', \
                str(self.identifier), TradeType(2), self.inTradeStep, self.inLongPrice, self.outTradeStep, self.outLongPrice, revenue, feesOwed, self.capital)


            self.inTradeStep = 0
            self.outTradeStep = 0

    def sell_short(self):
        if self.inShort:
            '''
            Get out of a short position
            Record env current price as outShortPrice
            '''
            self.inShort = False
            self.outShortPrice = self.env.get_current_price()
            self.outTradeStep = self.env.get_current_step()
            
            '''
            Calculate revenue and fees. Subtract fees from assetAmount. Calculate new capital for shorting.
            To calculate new capital, take the fees from the assetAmount, then turn asset amount into dollars.
            Take original dollars and add asset amount dollars.
            '''
            revenue = self.inShortPrice - self.outShortPrice
            feesOwed = self.assetAmount * self.feePercent
            self.assetAmount -= feesOwed

            dollarDifference = (self.assetAmount * self.inShortPrice) - (self.assetAmount * self.outShortPrice)
            self.capital += (self.assetAmount * self.inShortPrice) + dollarDifference


            '''
            Add to total revenue, 
            '''
            self.totalRevenue += revenue
            self.assetAmount = 0
            self.totalTrades += 1
            

            self.log.info('Agent: %s\tTrade Type: %s\tIn Step: %s\tIn Short Price: %s\tOut Step: %s\tOut Short Price: %s\tRevenue: %f\tFees paid: %f\tCapital: %f', \
                str(self.identifier), TradeType(3), self.inTradeStep, self.inShortPrice, self.outTradeStep, self.outShortPrice, revenue, feesOwed, self.capital)


            self.inTradeStep = 0
            self.outTradeStep = 0

    def get_total_fees(self) -> float:
        return self.totalFees

    def get_in_price(self) -> float:
        if self.inLong:
            return self.inLongPrice
        elif self.inShort:
            return self.inShortPrice
        else:
            return 0.0

    def get_total_profit(self) -> float:
        return self.totalProfit

    def get_total_revenue(self) -> float:
        return self.totalRevenue

    def get_total_trades(self) -> int:
        return self.totalTrades

    def get_capital(self) -> float:
        return self.capital
