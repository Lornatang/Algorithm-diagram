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


"""47-page exercises in the book"""


def __sum__(arr):
  if not arr:
    return 0
  return arr[0] + __sum__(arr[1:])


def cal_elem(arr):
  if not arr:
    return 0
  else:
    return 1 + cal_elem(arr[1:])


def __max__(arr):
  if len(arr) == 2:
    return arr[0] if arr[0] > arr[1] else arr[1]
  sub_max = __max__(arr[1:])
  return arr[0] if arr[0] > sub_max else sub_max


arr = [1, 2, 3, 4]

print(__sum__(arr))
print(cal_elem(arr))
print(__max__(arr))
