'''def recRange(num):
   return 1 if num <= 1 else num + recRange(num - 1)

print(recRange(6))
'''

'''def reverse(strng):
  if len(strng) == 0:
    return strng
  else:
    return reverse(strng[1:])+ strng[0]

print(reverse("testing"))'''

'''
def isPalindrome(strng):
  if len(strng) < 1:
    return True
  else:
    return strng[0] == strng [-1] and isPalindrome(strng[1:-1])

print(isPalindrome("foobar"))
'''

'''
def flatten(arr):
  if arr == []:
      return []
  if type(arr[0]) == list:
    return flatten(arr[0]) + flatten(arr[1:])
  else:
    return [arr[0]] + flatten(arr[1:])

print(flatten([1, [[[[2, 3, [4, 5]]]]]]))
'''

'''
def capitalizeFirst(arr):
  if arr == []:
    return []
  else:
    return [arr[0].title()] + capitalizeFirst(arr[1:])
print(capitalizeFirst(['banana', 'peach', 'pineapple']))
'''

'''
def capitalizeAll(arr):
  res = []
  if len(arr) == 0:
      return res
  else:
    res.append(arr[0].upper())
    return res + capitalizeAll(arr[1:])

print(capitalizeAll(['peach', 'pineapple']))
'''

obj1 = {
  "outer": "gtdfg",
  "obj": {
    "inner": 1,
    "otherObj": {
      "superInner": 2,
      "notANumber": 4,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

'''

def nestedEvenSum(nestedObj, sum=0):
  print(nestedObj)
  keys = list(nestedObj.keys())

  if len(keys) == 0:
    return sum

  if len(keys) == 1:

    if type(nestedObj[keys[0]]) is int and nestedObj[keys[0]] % 2 == 0:
      return sum + 1
    elif type(nestedObj[keys[0]]) is dict:
      return nestedEvenSum(nestedObj[keys[0]], sum)

  if type(nestedObj[keys[0]]) is int and nestedObj[keys[0]] % 2 == 0:
    sum = sum + 1
  elif type(nestedObj[keys[0]]) is dict:
    sum = nestedEvenSum(nestedObj[keys[0]], sum)
  di = nestedObj.copy()
  di.pop(keys[0])
  return nestedEvenSum(di, sum)


print(nestedEvenSum(obj2)) 
'''


obj2 = {
  "a": 9,
  "b": {
    "b": 2,
    "bb": {
      "b": 3,
      "bb": {
        "b": 2
      }
    }
  },
  "c": {
    "c": {
      "c": 2
    },
    "cc": 'ball', "ccc": 5
  },
  "d": 1,
  "e": {
    "e": {
      "e": 2
    }, "ee": 'car'
  }
}

'''
def nestedEvenSum(nestedObj):
  keys = list(nestedObj.keys())
  if len(keys) == 0:
    return nestedObj

  if type(nestedObj[keys[0]]) is int:
    nestedObj[keys[0]] = str(nestedObj[keys[0]])
    if len(keys) == 1:
      return nestedObj

  elif type(nestedObj[keys[0]]) is dict:
    nestedEvenSum(nestedObj[keys[0]])

  di = nestedObj.copy()
  di.pop(keys[0])
  nestedObj.update(nestedEvenSum(di))
  return nestedObj

print(obj2)
print(nestedEvenSum(obj2))

'''
'''
def collectStrings(obj):
  colArr = []
  for k in obj:
    if type(obj[k]) is str:
      colArr.append(obj[k])
    if type(obj[k]) is dict:
      colArr = colArr + collectStrings(obj[k])
  return colArr

print(656565,collectStrings(obj2))

'''
''''
def middleFunction(arr):
  a = []
  for i in arr:
    if i == arr[0] or i == arr[-1]:
      pass
    else:
      a.append(i)
  return a

print(middleFunction([0,0,0,0,0,0,0,0,0,0]))
'''

'''
def bestScores(givenList):
  cp = givenList
  res = sorted(cp, reverse=True)
  fbs = res [0]
  for i in res:
    if i != fbs:
      sbs = i
      return fbs, sbs


print(bestScores([87, 76, 100,98, 99, 12, 7, 87,56, 45, 34, 0, 2]))
'''

storage_data = {
    "9:36:02": 15000,
    "9:36:02": 9000
}


def get_step_day(steps):
    for steps1 in storage_data.values():
      sum_st = steps1+ steps
    return sum_st
    
print(get_step_day(800))
