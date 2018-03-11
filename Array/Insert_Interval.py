#Method 1 - O(n)
#put each interval in its correct position

def insert(self, intervals, newInterval):
      result = []
      ln=len(intervals)
      ck=False

      #when intervals is empty, simply add the new interval to the result
      if ln==0:
          result.append([newInterval.start,newInterval.end])
          return result

      #add new interval in correct position
      for i in intervals:
          if newInterval.start <= i.start:
              if newInterval.end <= i.end:
                  result.append([newInterval.start,newInterval.end])
                  ck=True
                  break
              else:
                  result.append([newInterval.start,max(newInterval.end,i.end)])
                  ck=True
                  break
          elif newInterval.start <= i.end:
              result.append([i.start,max(newInterval.end,i.end)])
              ck=True
              break
          else:
              result.append([i.start,i.end])


      pos = len(result)

      #checking if new interval is added to result or not. if not then it comes at the end of intervals
      if not ck:
          result.append([newInterval.start,newInterval.end])
          return result


      #append left out intervals in correct position
      for j in range(pos-1,ln):
          l = len(result)
          if intervals[j].start > result[l-1][1]:
              result.append([intervals[j].start,intervals[j].end])
          else:
              result[l-1][0] = min(result[l-1][0],intervals[j].start)
              result[l-1][1] = max(result[l-1][1],intervals[j].end)
              
      return result


#Method 2 - O(n)
#This reduces extra space needed by method 1 and pretty simple logic too
#get intervals before new interval and add it to result
#merge the intervals with new interval
#append remaining intervals to result

def insert(self, intervals, newInterval):
      result = []
      l=len(intervals)
      i=0

      #get intervals before new interval
      while i<l and intervals[i].end<newInterval.start:
          result.append([intervals[i].start,intervals[i].end])
          i=i+1

      #merge intervals
      while i<l and intervals[i].start<=newInterval.end:
          newInterval.start = min(newInterval.start,intervals[i].start)
          newInterval.end   = max(newInterval.end,intervals[i].end)
          i=i+1
      result.append([newInterval.start,newInterval.end])

      #append remaining intervals
      while i<l:
          result.append([intervals[i].start,intervals[i].end])
          i=i+1

      return result
