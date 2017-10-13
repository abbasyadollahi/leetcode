class Solution(object):
	def mergeSort(self, mylist):
		"""
		:type list: List[int]
		:rtype: List[int]
		"""

		list_length = len(mylist)

		if list_length == 1:
			return mylist

		list1 = mylist[:list_length//2]
		list2 = mylist[list_length//2:]

		list1 = self.mergeSort(list1)
		list2 = self.mergeSort(list2)

		return self.merge(list1, list2)


	def merge(self, list1, list2):
		"""
		:type list1: List[int]
		:type list2: List[int]
		:rtype: List[int]
		"""

		sorted_list = []

		while len(list1) != 0 and len(list2) != 0:
			if list1[0] < list2[0]:
				sorted_list.append(list1.pop(0))
			else:
				sorted_list.append(list2.pop(0))

		while len(list1) != 0:
			sorted_list.append(list1.pop(0))

		while len(list2) != 0:
			sorted_list.append(list2.pop(0))

		return sorted_list
