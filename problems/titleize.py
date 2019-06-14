def titleize(string):
  '''
  'this is awesome' -> 'This Is Awesome'
  'oNLY cAPITALIZe fIRSt' -> "ONLy CAPITALIZe FIRSt"
  '''
  return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))

print(titleize("oNLY cAPITALIZe"))
print(titleize("this is awesome"))
print(titleize("jdp JDP JdP"))
