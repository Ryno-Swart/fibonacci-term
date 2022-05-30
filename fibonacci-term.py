# -----------------------------------------------------------
# Fibonacci challange problem presented by Corigine.
#
# Finds the index of the first term in the Fibonacci sequence
# to contain N digits.
# 
# GNU GENERAL PUBLIC LICENSE Version 3
# 30 May 2022
# Ryno Swart, South Africa
# rswart1995@gmail.com
# -----------------------------------------------------------

import numpy as np
import sys

SQRT_5       = np.sqrt(5, dtype=np.float64)
GOLDEN_RATIO = (1.0 + SQRT_5)/2.0 # Positive solution to x^2 - x - 1 = 0.

def fibonacci_term(num):
  """Finds the index of the first term in the Fibonacci sequence
  to contain num digits.
  
  See README.md @ https://github.com/Ryno-Swart/fibonacci-term for detailed derivation.
  
  Parameters:
  num         - The number of digits of the Fibonacci term
  
  Raises:
  TypeError   - If the type of num is not an integer.
  ValueError  - If the value of num is not greater than zero. Or,
                if the value of num exceeds 1e14 (to prevent
                inaccuracies caused by 52-bit floating point mantissa)
  
  Returns:
  The index of first Fibonacci number with num digits.
  """
  if not np.issubdtype(type(num), np.integer):
    raise TypeError('Argument \'num\' must be of integer type')
  if num < 1:
    raise ValueError('Argument \'num\' must be greater than or equal to one (1)')
  if num > 1e14: # TODO: Refine upper limit. This is a conservative estimate. (but why would you ever need bigger?)
    raise ValueError('Argument \'num\' must be less than or equal to (1e14)')
  if num == 1:
    return 1 # Special case for small indices due to Fibonacci approximation
  return np.int64(np.ceil((num - 1 + np.log10(SQRT_5))/np.log10(GOLDEN_RATIO)))

if __name__ == "__main__":
  # Sanitise user input
  if len(sys.argv) != 2:
    print('Exactly one (1) argument required.')
    print('Usage: Supply a number to find the first index of the Fibonacci sequence with the corresponding number of digits.')
    exit()
  try:
    input = np.int64(sys.argv[1])
  except ValueError:
    print('Input value must be an integer.')
    exit()
  except OverflowError:
    print('Overflow. Input value must be between (-2^63) and (2^63 - 1), inclusive.')
    exit()
  print(input)
  
  # Run program
  try:
    print(fibonacci_term(input))
  except Exception as e:
    print(e)