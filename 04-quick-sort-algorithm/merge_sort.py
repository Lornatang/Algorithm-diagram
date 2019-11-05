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


def merge_sort(arr):
  """ Classic merge sorting algorithm, using recursive methods to achieve.

  Args:
    arr: Unsort array.

  Returns:
    Sort array.

  Examples:
    >>> print(merge_sort([10, 5, 2, 3]))
    [2, 3, 5, 10]

  """
  if len(arr) < 2:
    return arr
  else:
    mid = int(len(arr) / 2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
  result = []
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  result += left[i:]
  result += right[j:]
  return result
