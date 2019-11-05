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


def bag(goods, size):
  cell = [[0 for col in range(size)] for row in range(len(goods))]

  package_size = [i + 1 for i in range(size)]

  for j in range(size):
    if goods[0][1] <= package_size[j]:
      cell[0][j] = goods[0][0]

  for i in range(1, len(goods)):
    for j in range(size):
      if (package_size[j] - goods[i][1] > 0) and (goods[i][0] + cell[i - 1][package_size[j] - 1 - goods[i][1]]) > \
          cell[i - 1][j]:
        cell[i][j] = goods[i][0] + cell[i - 1][package_size[j] - goods[i][1] - 1]
      elif (package_size[j] - goods[i][1] == 0) and (goods[i][0] > cell[i - 1][j]):
        cell[i][j] = goods[i][0]
      else:
        cell[i][j] = cell[i - 1][j]
  print(cell)  # [[1500, 1500, 1500, 1500], [1500, 1500, 1500, 3000], [1500, 1500, 2000, 3500]]

  return cell[len(goods) - 1][size - 1]


if __name__ == '__main__':
  goods = [[1500, 1], [3000, 4], [2000, 3]]
  print(bag(goods, 4))  # 3500
