# string function

import numpy as np

print("Two Array")
print(np.char.add(['Sanjeev'], ['Gohil']))
print(np.char.add(['Sanjeev', 'Harishbhai'], ['Gohil']))
print(np.char.multiply('Sanjeev', 3))
print(np.char.capitalize('sanjeev gohil'))
print(np.char.title('sanjeev gohil'))
print(np.char.upper('sanjeev gohil'))
print(np.char.lower('SANJEEV GOHIL'))
print(np.char.center('sanjeev', 20, '$'))
print(np.char.split('sanjeev gohil'))
print(np.char.split('sanjeev, gohil', sep=","))
print(np.char.splitlines('sanjeev gohil'))
print(np.char.strip('Hello How Are You!', 'H'))
print(np.char.strip(['Hello How Are You!'], 'H'))
print(np.char.strip(['Hello', 'How Are You!'], 'H'))
print(np.char.join(':', 'DMY'))
print(np.char.join([':', '-'], ['DMY', 'YMD']))
print(np.char.join([':'], ['DMY', 'YMD']))
print(np.char.replace("Sanju Gohil", "Sanju", "Sanjeev"))
