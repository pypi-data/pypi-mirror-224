#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Author : Trabi
# Copyright (C) 2022-2023 ByQuant.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

#from . import exchange as exchange
#from . import chart as chart
#from . import data as data
#from . import indicator as indicator
#from . import indicators as indicators
#from .metastrategy import *
#from .metabacktest import *

def getExchange(exName):
    #print(exName)
    exName=exName.lower()
    if exName == 'ace': result = exchange.ace()
    elif exName == 'alpaca': result = exchange.alpaca()
    elif exName == 'ascendex': result = exchange.ascendex()
    elif exName == 'bequant': result = exchange.bequant()
    elif exName == 'bigone': result = exchange.bigone()
    elif exName == 'binance': result = exchange.binance()
    elif exName == 'binancecoinm': result = exchange.binancecoinm()
    elif exName == 'binanceus': result = exchange.binanceus()
    elif exName == 'binanceusdm': result = exchange.binanceusdm()
    elif exName == 'bit2c': result = exchange.bit2c()
    elif exName == 'bitbank': result = exchange.bitbank()
    elif exName == 'bitbay': result = exchange.bitbay()
    elif exName == 'bitbns': result = exchange.bitbns()
    elif exName == 'bitcoincom': result = exchange.bitcoincom()
    elif exName == 'bitfinex': result = exchange.bitfinex()
    elif exName == 'bitfinex2': result = exchange.bitfinex2()
    elif exName == 'bitflyer': result = exchange.bitflyer()
    elif exName == 'bitforex': result = exchange.bitforex()
    elif exName == 'bitget': result = exchange.bitget()
    elif exName == 'bithumb': result = exchange.bithumb()
    elif exName == 'bitmart': result = exchange.bitmart()
    elif exName == 'bitmex': result = exchange.bitmex()
    elif exName == 'bitopro': result = exchange.bitopro()
    elif exName == 'bitpanda': result = exchange.bitpanda()
    elif exName == 'bitrue': result = exchange.bitrue()
    elif exName == 'bitso': result = exchange.bitso()
    elif exName == 'bitstamp': result = exchange.bitstamp()
    elif exName == 'bitstamp1': result = exchange.bitstamp1()
    elif exName == 'bittrex': result = exchange.bittrex()
    elif exName == 'bitvavo': result = exchange.bitvavo()
    elif exName == 'bkex': result = exchange.bkex()
    elif exName == 'bl3p': result = exchange.bl3p()
    elif exName == 'blockchaincom': result = exchange.blockchaincom()
    elif exName == 'btcalpha': result = exchange.btcalpha()
    elif exName == 'btcbox': result = exchange.btcbox()
    #elif exName == 'btcex': result = exchange.btcex()
    elif exName == 'btcmarkets': result = exchange.btcmarkets()
    elif exName == 'btctradeua': result = exchange.btctradeua()
    elif exName == 'btcturk': result = exchange.btcturk()
    elif exName == 'buda': result = exchange.buda()
    elif exName == 'bybit': result = exchange.bybit()
    elif exName == 'cex': result = exchange.cex()
    elif exName == 'coinbase': result = exchange.coinbase()
    elif exName == 'coinbaseprime': result = exchange.coinbaseprime()
    elif exName == 'coinbasepro': result = exchange.coinbasepro()
    elif exName == 'coincheck': result = exchange.coincheck()
    elif exName == 'coinex': result = exchange.coinex()
    elif exName == 'coinfalcon': result = exchange.coinfalcon()
    elif exName == 'coinmate': result = exchange.coinmate()
    elif exName == 'coinone': result = exchange.coinone()
    elif exName == 'coinspot': result = exchange.coinspot()
    elif exName == 'cryptocom': result = exchange.cryptocom()
    elif exName == 'currencycom': result = exchange.currencycom()
    elif exName == 'delta': result = exchange.delta()
    elif exName == 'deribit': result = exchange.deribit()
    elif exName == 'digifinex': result = exchange.digifinex()
    elif exName == 'exmo': result = exchange.exmo()
    elif exName == 'flowbtc': result = exchange.flowbtc()
    elif exName == 'fmfwio': result = exchange.fmfwio()
    elif exName == 'gate': result = exchange.gate()
    elif exName == 'gateio': result = exchange.gate() #gateio
    elif exName == 'gemini': result = exchange.gemini()
    elif exName == 'hitbtc': result = exchange.hitbtc()
    elif exName == 'hitbtc3': result = exchange.hitbtc3()
    elif exName == 'hollaex': result = exchange.hollaex()
    elif exName == 'huobi': result = exchange.huobi()
    elif exName == 'huobijp': result = exchange.huobijp()
    elif exName == 'huobipro': result = exchange.huobipro()
    elif exName == 'idex': result = exchange.idex()
    elif exName == 'independentreserve': result = exchange.independentreserve()
    elif exName == 'indodax': result = exchange.indodax()
    elif exName == 'itbit': result = exchange.itbit()
    elif exName == 'kraken': result = exchange.kraken()
    elif exName == 'krakenfutures': result = exchange.krakenfutures()
    elif exName == 'kucoin': result = exchange.kucoin()
    elif exName == 'kucoinfutures': result = exchange.kucoinfutures()
    elif exName == 'kuna': result = exchange.kuna()
    elif exName == 'latoken': result = exchange.latoken()
    elif exName == 'lbank': result = exchange.lbank()
    elif exName == 'lbank2': result = exchange.lbank2()
    elif exName == 'luno': result = exchange.luno()
    elif exName == 'lykke': result = exchange.lykke()
    elif exName == 'mercado': result = exchange.mercado()
    elif exName == 'mexc': result = exchange.mexc()
    elif exName == 'mexc3': result = exchange.mexc3()
    elif exName == 'ndax': result = exchange.ndax()
    elif exName == 'novadax': result = exchange.novadax()
    elif exName == 'oceanex': result = exchange.oceanex()
    elif exName == 'okcoin': result = exchange.okcoin()
    elif exName == 'okex': result = exchange.okex()
    elif exName == 'okex5': result = exchange.okex5()
    elif exName == 'okx': result = exchange.okx()
    elif exName == 'paymium': result = exchange.paymium()
    elif exName == 'phemex': result = exchange.phemex()
    elif exName == 'poloniex': result = exchange.poloniex()
    elif exName == 'poloniexfutures': result = exchange.poloniexfutures()
    elif exName == 'probit': result = exchange.probit()
    elif exName == 'ripio': result = exchange.ripio()
#    elif exName == 'stex': result = exchange.stex()
    elif exName == 'tidex': result = exchange.tidex()
    elif exName == 'timex': result = exchange.timex()
    elif exName == 'tokocrypto': result = exchange.tokocrypto()
    elif exName == 'upbit': result = exchange.upbit()
    elif exName == 'wavesexchange': result = exchange.wavesexchange()
    elif exName == 'wazirx': result = exchange.wazirx()
    elif exName == 'whitebit': result = exchange.whitebit()
    elif exName == 'woo': result = exchange.woo()
    elif exName == 'yobit': result = exchange.yobit()
    elif exName == 'zaif': result = exchange.zaif()
    elif exName == 'zb': result = exchange.zb()
    elif exName == 'zonda': result = exchange.zonda()
    else:
        print('No %s' % (exName))
    return result

