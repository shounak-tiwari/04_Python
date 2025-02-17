x = 'my first name is {fristname} and last name is {lastname}'

dct = {'fristname':'Akash','lastname' : 'Tiwari'}

print(x.format_map(dct))