

	

import urllib2
import time 
import jason
import random

QUERY = "http://localhost:8080/query?id={}"

N = 500

def getDataPoint(quote):

  stock = quote[stock]
  bid_price = float(quote['top_bid']['price'])
  ask_price = float(quote['top_ask']['price'])
  price = bid_price
  return stock, bid_price, ask_price, stock
