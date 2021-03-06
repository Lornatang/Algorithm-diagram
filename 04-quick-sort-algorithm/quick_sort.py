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


def quick_sort(arr):
  """ Classic fast sorting algorithm, using recursive methods to achieve.

  Args:
    arr: Unsort array.

  Returns:
    Sort array.

  Examples:
    >>> print(quick_sort([10, 5, 2, 3]))
    [2, 3, 5, 10]

  """
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]

    greater = [i for i in arr[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([10, 5, 2, 3]))
