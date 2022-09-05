# binsearch.py
# Michael Randazzo
# CSCI 77800 Fall 2022
# collaborators: None
# consulted: ThinkJava

def binarySearch(list, value):
  firstIndex = 0
  lastIndex = len(list) - 1
  middleIndex = int((firstIndex +lastIndex) / 2)
  
  if list[firstIndex] == value:
    return firstIndex
  elif list[lastIndex] == value:
    return lastIndex

  while list[middleIndex] != value:
    if(list[middleIndex] < value):
      firstIndex = middleIndex
      
    else:
      lastIndex = middleIndex
      
    middleIndex = int((firstIndex +lastIndex) / 2)
    if firstIndex == middleIndex or lastIndex == middleIndex:
      return -1

  return middleIndex

list1 = [0, 2, 5, 12, 23, 30, 52, 99]

print(binarySearch(list1, 22))
