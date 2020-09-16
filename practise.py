import json
import os
# def pop(list):
#     length = len(list)
#     for i in range(length):
#         for j in range(length - i - 1):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#             else:
#                 pass
#     return list


# def bin_search(list, target):
#     mid = len(list) // 2
#     if list[mid] == target:
#         return True
#     if len(list) == 1 and list[0] !=target:
#         return False
#     if target > list[mid]:
#         return bin_search(list[mid + 1:], target)
#     else:
#         return bin_search(list[:mid], target)


# class Queue():
#     def __init__(self):
#         self.data = deque()
#
#     def size(self):
#         return len(self.data)
#
#     def dequeue(self):
#         self.data.popleft()
#
#     def enqueue(self, x):
#         self.data.append(x)


# def fab(n):
#     while n > 0:
#         if n == 1:
#             return 1
#         return n * fab(n-1)

# class Node:
#
#     def __init__(self, elem, next=None):
#         self.elem = elem
#         self.next = next
#
#
# class SingleLinkList:
#
#     def __init__(self, node=None):
#         self.__head = node
#
#     def isEmpty(self):
#         return self.__head is None
#
#     def add(self, item):
#         node = Node(item)
#         node.next = self.__head
#         self.__head = node
#
#     def append(self, item):
#         node = Node(item)
#         if self.isEmpty():
#             self.__head = node
#         else:
#             cur = self.__head
#             while cur.next is not None:
#                 cur = cur.next
#             cur.next = node
#
#     def insert(self, pos, item):
#         cur = self.__head
#         cur_index = 1
#         while cur_index < pos-1:
#             cur = cur.next
#             cur_index = cur_index + 1
#         node = Node(item)
#         node.next = cur.next
#         cur.next = node
#
#     def count(self):
#         cur = self.__head
#         count = 1
#         while cur.next is not None:
#             count = count + 1
#             cur = cur.next
#         return count
#
#     def travel(self):
#         cur = self.__head
#         while cur is not None:
#             print(cur.elem, end=' ')
#             cur = cur.next
#         print('')
#
#
# if __name__ == '__main__':
#     sll = SingleLinkList()
#
#     print(sll.isEmpty())
#
#     sll.append(1)
#     sll.append(2)
#     sll.append(4)
#     sll.append(3)
#     sll.add(9)
#     sll.append(5)
#
#     print(sll.count())
#
#     sll.insert(3, 8)
#     sll.append(0)
#     sll.travel()

