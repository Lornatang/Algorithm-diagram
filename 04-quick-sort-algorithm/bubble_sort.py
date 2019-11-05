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


def bubble_sort(arr):
  """ Classic bubble sorting algorithm, using recursive methods to achieve.

  Args:
    arr: Unsort array.

  Returns:
    Sort array.

  Examples:
    >>> print(bubble_sort([10, 5, 2, 3]))
    [2, 3, 5, 10]

  """
  for i in range(len(arr) - 1):
    for j in range(i, len(arr)):
      if arr[i] > arr[j]:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
  return arr
