
def running_average():
  running_average.accumulator = 0
  running_average.size = 0

  def inner(number):
    running_average.accumulator += number
    running_average.size += 1
    return running_average.accumulator / running_average.size
  return inner

rAvg = running_average()
rAvg(10)
rAvg(11)
rAvg(12)

rAvg2 = running_average()
rAvg2(1)
rAvg2(3)

print(rAvg)
print(rAvg2)
