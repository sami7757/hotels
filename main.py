import csv
import sys

def hotels():
  csvData = csv.reader(open('hotels.csv','r'))
  csvData.__next__() # skip first row
  state = input("What is the state:\n")
  costOrRating = input("Cost or Rating: cost/rating\n")
  operation = input("Operation: cheapest/highest/average\n")
  hotelCode = 0
  sum = 0.0
  count = 0
  avg = 0.0
  min = sys.maxsize
  max = -sys.maxsize - 1
  for row in csvData: 
    if state.lower() == 'india' or row[2].lower() == state.lower():
      
      if costOrRating.lower() == "cost":
        metric = float(row[3])
      elif costOrRating.lower() == "rating":
        metric = float(row[4])
      if operation.lower() == 'cheapest' and metric < min:
        min = metric
        hotelCode = row[1]
      elif operation.lower() == 'highest' and metric > max:
        max = metric
        hotelCode = row[1]
      elif operation.lower() == 'average':
        sum = sum + metric
        count = count + 1
        avg = sum/count
        
  if operation.lower() == 'average':
    print('Average ' + costOrRating + ' of Hotel in ' + state + ' is ' + str(avg))
  else:
    print('Hotel with ' + operation + ' ' + costOrRating + ' in ' + state + ' is ' + str(hotelCode))


hotels()