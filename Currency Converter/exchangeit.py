"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Emily Shader
Date:   02/16/2025
"""

import currency

src = str(input('3-letter code for original currency: '))
dst = str(input('3-letter code for the new currency: '))
amt = float(input('Amount of the original currency: '))

newamt = round(currency.exchange(src,dst,amt),3)

print('You can exchange ' + str(amt) +' '+ src + ' for ' + str(newamt) +' '+ str(dst) + '.')