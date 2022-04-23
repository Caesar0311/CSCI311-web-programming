from statsGen import statisticsGenerator

startingValue = 1000         #initial value of the statistic

increasing = True            #if true the value tends to rise
                             #if false it tends to fall

statistics = statisticsGenerator(startingValue, increasing)

while(True):
   x = str(input("Select 1 (update), 0 (quit): "))
   if x == "1": print(statistics.get())	
   if x == "0":
      statistics.end()
      break
