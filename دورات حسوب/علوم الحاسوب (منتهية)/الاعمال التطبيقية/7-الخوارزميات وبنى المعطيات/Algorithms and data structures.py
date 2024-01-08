# 02. القوائم المترابطة Linked Lists----------------------------------------------------------------
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.key = key
    
# def search(root, key):
#     if root.key == key or root is None:
#         return root
#     if root.key < key:
#         return search(root.right, key)
    
#     return search(root.left, key)
# r = Node(5)
# r.right = Node(7)
# r.right.right = Node(9)
# r.left = Node(3)
# r.left.left = Node(1)
# r.left.right = Node(100)
# print(search(r, 3).right.key)

# num = 12
# print(0)
# print(1)
# arr = []
# pre_1 = 0
# pre_2 = 1
# for i in range(num):

#     arr.append(pre_1 + pre_2 )
#     print(arr[i])
#     pre_1 = arr[i]
#     pre_2 = arr[i-1]


# --------------------------------------------------
# def search(arr, n, x):
#     for i in range(0,n):
#         if (arr[i] == x):
#             return i
#     return -1
    
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = len(arr)
# x = 11
# result = search(arr, n, x)
# if (result == -1):
#     print("not fuond")
# else:
#     print("number is ", result)
# print(n)

# --------------------------------------------------
# def binarySearch(arr, l, r, x):
#     count = 0
#     while l <= r:
#         count += 1
#         mid = l + (r-l)/2
#         mid = int(mid)
#         print(count)
#         if (arr[mid] == x):
#             return mid
#         elif (arr[mid] < x):
#             l = mid + 1
#         elif (arr[mid] > x):
#             r = mid - 1
#     return -1
    
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r = len(arr)-1
# l = 0
# x = 11
# result = binarySearch(arr, l, r, x)
# if (result == -1):
#     print("not fuond")
# else:
#     print("number is ", result)
# # print(n)


# --------------------------------------------------
# def bubbleSort(arr):
#     count = sort = 0
    
#     for i in range(len(arr)):
#         ceck = sort

#         for j in range(len(arr) - i - 1):
#             count += 1
#             if arr[j] > arr[j + 1]:
#                 sort+= 1
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
#         if ceck == sort:  
#                 break
        
#     print("count: ",count)
#     print("sort: ", sort)
#     print("------------")

# arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
# bubbleSort(arr)
# for i in range(len(arr)):
#     print(arr[i])


# --------------------------------------------------
# def selectionSort(arr):
#     count = sort = 0
    
#     for i in range(0, len(arr)):
#         min_idx = i
        
#         for j in range(i+1, len(arr)):
#             count += 1
#             if arr[min_idx] > arr[j]:
#                 sort+= 1
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
#     print("count: ",count)
#     print("sort: ", sort)
#     print("------------")

# arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
# selectionSort(arr)
# for i in range(len(arr)):
#     print(arr[i])




# --------------------------------------------------
# arr1 = arr2 = []
# def margeSort(arr):
#     if len(arr) != 1:
#         mid = len(arr)//2
#         arr1 = margeSort(arr[:mid])
#         arr2 = margeSort(arr[mid:])
#     print(arr)
#     print(arr1)
#     print(arr2)
    
# arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
# margeSort(arr)

# arr1 = arr2 = []
# def margeSort(arr):
#     if len(arr) != 1:
#         mid = len(arr)//2
#         arr1 = margeSort(arr[:mid])
#         arr2 = margeSort(arr[mid:])
#         print(arr)
#         print(arr1)
#         print(arr2)
    
# arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
# margeSort(arr)



# --------------------------------------------------
# def sqrtBruteForce(x):
#     if x == 0 or x == 1: return x


#     result = x + 1; mid = x; count = 0; start = True
#     while start:
#         count += 1
#         if result > x:
#             mid = mid//2
#             result = mid * mid
#             if result == x: start = False
#         else:
#             mid = mid - 1
#             while result < x:
#                 mid += 1
#                 count += 1
#                 result = mid * mid
#             start = False

#     print("count =", count)
#     print("result = ", result)
#     print("mid = ", mid)


# def sqrtBinarySearch2(x):
#     if x == 0 or x == 1:
#         return x
#     count = 0
#     start, end = 1, x
#     result = 0
#     while start <= end:
#         count += 1
#         mid = (start + end) // 2
#         if mid * mid == x:
#             return mid
#         elif mid * mid < x:
#             start = mid + 1
#             result = mid
#         else:
#             end = mid - 1

#     print("count =", count)
#     print("result = ", result)
#     print("mid = ", mid)


# sqrtBruteForce(20000000000000)
# print("----------------")
# sqrtBinarySearch2(20000000000000)


# --------------------------------------------------

# def mergeSort(arr): 
# 	if len(arr) >1: 
# 		mid = len(arr)//2 #إيجاد منتصف المصفوفة
# 		L = arr[:mid] # تقسيم محتويات المصفوفة
# 		R = arr[mid:] # إلى نصفين
# 		# print('L = ', L)
# 		# print('R = ', R)
# 		mergeSort(L) # ترتيب النصف الأول
# 		mergeSort(R) # ترتيب النصف الثاني

# 		i = j = k = 0
		
# 		# نسخ البيانات إلى مصفوفتين مؤقتتين
# 		while i < len(L) and j < len(R): 
# 			if L[i] < R[j]: 
# 				arr[k] = L[i] 
# 				i+=1
# 				print("Array: ", arr)
# 			else: 
# 				arr[k] = R[j] 
# 				j+=1
# 				print("Array: ", arr)
# 			k+=1
		
# 		# التأكد من بقاء أي عنصر في المصفوفتين المؤقتتين
# 		while i < len(L): 
# 			arr[k] = L[i] 
# 			i+=1
# 			k+=1
# 			print("Array--: ", arr)
		
# 		while j < len(R): 
# 			arr[k] = R[j] 
# 			j+=1
# 			k+=1
# 			print("Array--: ", arr)
			

# # طباعة المصفوفة
# def printList(arr): 
# 	for i in range(len(arr)):		 
# 		print(arr[i],end=" ") 
# 	print() 

# # اختبار الدوال السابقة
# if __name__ == '__main__': 
# 	arr = [12, 11, 13, 5, 6, 7] 
# 	print ("Given array is", end="\n") 
# 	printList(arr) 
# 	mergeSort(arr) 
# 	print("Sorted array is: ", end="\n") 
# 	printList(arr)


# --------------------------------------------------

# class Graph:
#     def __init__(self,numvertex):
#         self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
#         self.numvertex = numvertex
#         self.vertices = {}
#         self.verticeslist =[0]*numvertex

#     def set_vertex(self,vtx,id):
#         if 0<=vtx<=self.numvertex:
#             self.vertices[id] = vtx
#             self.verticeslist[vtx] = id

#     def set_edge(self,frm,to,cost=0):
#         frm = self.vertices[frm]
#         to = self.vertices[to]
#         self.adjMatrix[frm][to] = cost
#         # لا تضف هذا السطر إن كنت تستخدم الرسوم البيانية الموجّهة
#         self.adjMatrix[to][frm] = cost

#     def get_vertex(self):
#         return self.verticeslist

#     def get_edges(self):
#         edges=[]
#         for i in range (self.numvertex):
#             for j in range (self.numvertex):
#                 if (self.adjMatrix[i][j]!=-1):
#                     edges.append((self.verticeslist[i],self.verticeslist[j],self.adjMatrix[i][j]))
#         return edges
        
#     def get_matrix(self):
#         return self.adjMatrix
            
# G =Graph(6)
# G.set_vertex(0,'a')
# G.set_vertex(1,'b')
# G.set_vertex(2,'c')
# G.set_vertex(3,'d')
# G.set_vertex(4,'e')
# G.set_vertex(5,'f')
# G.set_edge('a','e',10)
# G.set_edge('a','c',20)
# G.set_edge('c','b',30)
# G.set_edge('b','e',40)
# G.set_edge('e','d',50)
# G.set_edge('f','e',60)
# print("Vertices of Graph")
# print(G.get_vertex())
# print("Edges of Graph")
# print(G.get_edges())
# print("Adjacency Matrix of Graph")
# print(G.get_matrix())



# --------------------------------------------------

# يستخدم هذا الصنف لتمثيل قائمة المجاورة الخاصّة بعقدة معينة
class AdjNode: 
	def __init__(self, data): 
		self.vertex = data 
		self.next = None


# يمثل هذا الصنف رسمًا بيانياً. 
# الرسم البياني هو قائمة تتضمن قوائم المجاورة.
# عدد الرؤوس سيكون هو حجم المصفوفة.

class Graph: 
	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [None] * self.V 

	# دالة لإضافة ضلع إلى الرسم البياني غير الموجّه
	def add_edge(self, src, dest): 
		# إضافة العقدة إلى العقدة المصدرية
		node = AdjNode(dest) 
		node.next = self.graph[src] 
		self.graph[src] = node 

		# إضافة العقدة المصدرية إلى الهدف الذي هو رسم بياني غير موجّه
		node = AdjNode(src) 
		node.next = self.graph[dest] 
		self.graph[dest] = node 

	# دالة لطباعة الرسم البياني
	def print_graph(self): 
		for i in range(self.V): 
			print("Adjacency list of vertex {}\n head".format(i), end="") 
			temp = self.graph[i] 
			while temp: 
				print(" -> {}".format(temp.vertex), end="") 
				temp = temp.next
			print(" \n") 


# اختبار الشيفرة السابقة
if __name__ == "__main__": 
	V = 5
	graph = Graph(V) 
	graph.add_edge(0, 1) 
	graph.add_edge(0, 4) 
	graph.add_edge(1, 2) 
	graph.add_edge(1, 3) 
	graph.add_edge(1, 4) 
	graph.add_edge(2, 3) 
	graph.add_edge(3, 4) 

	graph.print_graph()