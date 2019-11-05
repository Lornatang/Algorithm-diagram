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


stations = {"kone": {"id", "nv", "ut"},
            "ktwo": {"wa", "id", "mt"},
            "kthree": {"or", "nv", "ca"},
            "kfour": {"nv", "ut"},
            "kfive": {"ca", "az"}}
print(stations)

states_needed = {'id', 'or', 'ut', 'wa', 'ca', 'az', 'nv', 'mt'}
print(states_needed)

final_stations = set()

while states_needed:
  best_station = None
  states_covered = set()
  for station, states in stations.items():
    covered = states_needed & states
    if len(covered) > len(states_covered):
      best_station = station
      states_covered = covered
  states_needed -= states_covered
  final_stations.add(best_station)

print(final_stations)  # {'kfive', 'kthree', 'kone', 'ktwo'} 选择1235
