# Copyright 2019 Lorna Authors. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


"""Using recursive methods"""


def fact(x):
  """ The famous Fibonacci sequence on the Internet

  Args:
    x: Maximum number of columns.

  Returns:
    number

  Examples:
    >>> print(fact(5))
    120

  """
  if x == 1:
    return 1
  else:
    # 3 * 2 * 1
    return x * fact(x - 1)


def factorial(x, result):
  """ Famous Fibonacci sequence, using tail recursion.

  Args:
    x: Maximum number of columns.

  Returns:
    number

  Examples:
    >>> print(factorial(5, 1))
    120

  """
  if x == 1:
    return result
  else:
    return factorial(x - 1, x * result)


print(fact(5))
print(factorial(5, 1))
