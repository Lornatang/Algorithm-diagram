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


def find_lowest_cost_node(costs, processed):
  lowest_cost = float("inf")
  lowest_cost_node = None
  for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost = cost
      lowest_cost_node = node
  return lowest_cost_node


def dijkstra(graph, costs, parents):
  processed = []
  node = find_lowest_cost_node(costs, processed)
  while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
      new_cost = cost + neighbors[n]
      if costs[n] > new_cost:
        costs[n] = new_cost
        parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs, processed)
  return costs, parents


if __name__ == '__main__':
  graph = dict()
  graph["start"] = {}
  graph["start"]["a"] = 6
  graph["start"]["b"] = 6

  graph["a"] = {}
  graph["a"]["fin"] = 1

  graph["b"] = {}
  graph["b"]["a"] = 3
  graph["b"]["fin"] = 5

  graph["fin"] = {}

  infinity = float("inf")
  costs = {"a": 6, "b": 2, "fin": infinity}

  parents = {"a": "start", "b": "start", "fin": None}

  costs, parents = dijkstra(graph, costs, parents)
  print(costs)  # {'a': 5, 'b': 2, 'fin': 6}
  print(parents)  # {'a': 'b', 'b': 'start', 'fin': 'a'}
