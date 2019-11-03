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

"""Implement a simple binary search"""


def binary_search(lists, item):
  """ implements binary search for list

  Args:
    lists (list): Python List
    item (int, float, str): Element of list

  Returns:
    Elem exist return `elem index` for list, else return `None`

  Examples:
    >>> Lists = [1, 3, 5, 7, 9]
    >>> print(binary_search(my_list, 3))
    1
    >>> print(binary_search(my_list, -1))
    None

  """
  low = 0  # first index
  high = len(lists) - 1  # end index
  while low <= high:
    mid = (low + high) // 2  # get list middle index
    guess = lists[mid]
    if guess == item:
      return mid
    # if guese elem > item, the highest element index is sub one
    if guess > item:
      high = mid - 1
    else:
      # if guese elem > item, the lowest element index is add one
      low = mid + 1

  return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # 1
print(binary_search(my_list, -1))  # None
