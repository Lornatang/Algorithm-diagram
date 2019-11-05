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


from collections import deque


# 需编写函数person_is_seller，判断一个人是不是芒果销售商，如下所示。
def person_is_seller(name):
  return name[-1] == 'm'  # 这个函数检查人的姓名是否以m结尾：如果是，他就是芒果销售商。。


def bfs(graph, name):
  search_queue = deque()
  search_queue += graph[name]  # graph["you"]是一个数组，其中包含你的所有邻居，如["alice", "bob","claire"]。这些邻居都将加入到搜索队列中。

  searched = []
  while search_queue:
    person = search_queue.popleft()
    if person not in searched:
      if person_is_seller(person):
        print(person + " is a mango seller!")
        return True
      else:
        search_queue += graph[person]
        searched.append(person)
  return False


if __name__ == '__main__':
  graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "jonny"],
           "anuj": [], "peggy": [], "thom": [], "jonny": []}

  print(graph)

  bfs(graph, "you")  # thom is a mango seller!
