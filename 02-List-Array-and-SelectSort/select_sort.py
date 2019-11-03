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

"""Implement select sort by array"""


def find_smallest(arr):
  """ Find the subscript of the smallest element in the array

  Args:
    arr (list): Contains unsorted arrays.

  Returns:
    The small elem index in the array.

  """
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index


def select_sort(arr):
  """ Find the smallest element in the array and add it to the new array
    each time.

  Args:
    arr (list): Contains unsorted arrays.

  Returns:
    Sorted arrays.

  Examples:
    >>> arr = [5, 3, 6, 2, 10]
    >>> print(select_sort(arr))
    [2, 3, 5, 6, 10]

  """
  new_arr = []
  for i in range(len(arr)):
    smallest = find_smallest(arr)
    new_arr.append(arr.pop(smallest))
  return new_arr


arr = [5, 3, 6, 2, 10]

print(select_sort(arr))
