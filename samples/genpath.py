# Python program to print all paths from a source to destination.

import json
import sys
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

	def __init__(self, vertices):
		# No. of vertices
		self.V = vertices
		
		# default dictionary to store graph
		self.graph = defaultdict(list)
		self.route = {}
		self.routelen = 0
		self.beginpath = ''


	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	'''A recursive function to print all paths from 'u' to 'd'.
	visited[] keeps track of vertices in current path.
	path[] stores actual vertices and path_index is current
	index in path[]'''
	def printAllPathsUtil(self, u, d, visited, path):

		# Mark the current node as visited and store in path
		visited[u]= True
		path.append(u)

		# If current vertex is same as destination, then print
		# current path[]
		if u == d:
			# print (path)
			# print(type(path))
			tmppathlen = len(path)
			if tmppathlen < self.routelen or self.routelen == 0:
				self.routelen = tmppathlen
				# self.route = path.copy()
				# self.route = ', '.join([str(elem) for elem in path])
				self.route = {
					"start" : self.beginpath,
					"end" : d,
					"path" : ', '.join([str(elem) for elem in path])
				}

		else:
			# If current vertex is not destination
			# Recur for all the vertices adjacent to this vertex
			for i in self.graph[u]:
				if visited[i]== False:
					self.printAllPathsUtil(i, d, visited, path)
					
		# Remove current vertex from path[] and mark it as unvisited
		path.pop()
		visited[u]= False


	# Prints all paths from 's' to 'd'
	def printAllPaths(self, s, d):

		# Mark all the vertices as not visited
		visited =[False]*(self.V)

		# Create an array to store paths
		path = []

		# Call the recursive helper function to print all paths
		self.printAllPathsUtil(s, d, visited, path)



# Create a graph given in the above diagram
g = Graph(100)

g.addEdge(3, 2, 0.11)
g.addEdge(2, 1, 0.015)
g.addEdge(1, 0, 0.015)
g.addEdge(0, 10, 0.08)
g.addEdge(10, 9, 0.01)
g.addEdge(10, 12, 0.12)
g.addEdge(9, 8, 0.02)
g.addEdge(8, 7, 0,05)
g.addEdge(7, 6, 0.06)
g.addEdge(6, 5, 0.03)
g.addEdge(6, 23, 0.06)
g.addEdge(5, 4, 0.03)
g.addEdge(4, 11, 0.05)
g.addEdge(4, 74, 0.05)
g.addEdge(12, 13, 0.04)
g.addEdge(13, 14, 0.006)
g.addEdge(14, 15, 0.004)
g.addEdge(15, 16, 0.02)
g.addEdge(16, 20, 0.01)
g.addEdge(20, 19, 0.015)
g.addEdge(19, 18, 0.015)
g.addEdge(18, 25, 0.03)
g.addEdge(25, 28, 0.01)
g.addEdge(28, 27, 0.02)
g.addEdge(27, 26, 0.001)
g.addEdge(26, 17, 0.03)
g.addEdge(17, 12, 0.03)
g.addEdge(27, 33, 0.02)
g.addEdge(74, 22, 0.04)
g.addEdge(11, 22, 0.04)
g.addEdge(22, 21, 0.003)
g.addEdge(22, 23, 0.04)
g.addEdge(21, 24, 0.02)
g.addEdge(24, 73, 0.02)
g.addEdge(73, 29, 0.01)
g.addEdge(73, 30, 0.015)
g.addEdge(29, 31, 0.02)
g.addEdge(30, 35, 0.04)
g.addEdge(23, 36, 0.06)
g.addEdge(33, 32, 0.05)
g.addEdge(32, 39, 0.02)
g.addEdge(31, 34, 0.02)
g.addEdge(39, 76, 0.06)
g.addEdge(39, 50, 0.04)
g.addEdge(39, 38, 0.06)
g.addEdge(34, 75, 0.01)
g.addEdge(75, 35, 0.01)
g.addEdge(34, 40, 0.03)
g.addEdge(34, 77, 0.03)
g.addEdge(34, 78, 0.03)
g.addEdge(34, 79, 0.03)
g.addEdge(34, 80, 0.03)
g.addEdge(35, 36, 0.01)
g.addEdge(36, 37, 0.002)
g.addEdge(37, 38, 0.02)
g.addEdge(37, 76, 0.02)
g.addEdge(38, 48, 0.04)
g.addEdge(76, 48, 0.04)
g.addEdge(50, 49, 0.04)
g.addEdge(50, 54, 0.02)
g.addEdge(40, 47, 0.03)
g.addEdge(77, 47, 0.03)
g.addEdge(78, 47, 0.03)
g.addEdge(79, 47, 0.03)
g.addEdge(80, 47, 0.03)
g.addEdge(48, 47, 0.08)
g.addEdge(49, 48, 0.01)
g.addEdge(49, 53, 0.02)
g.addEdge(49, 81, 0.02)
g.addEdge(53, 60, 0.01)
g.addEdge(81, 60, 0.01)
g.addEdge(54, 70, 0.03)
g.addEdge(47, 46, 0.01)
g.addEdge(46, 45, 0.01)
g.addEdge(45, 44, 0.02)
g.addEdge(46, 51, 0.01)
g.addEdge(51, 52, 0.01)
g.addEdge(51, 58, 0.02)
g.addEdge(58, 66, 0.01)
g.addEdge(60, 59, 0.01)
g.addEdge(59, 68, 0.02)
g.addEdge(44, 43, 0.01)
g.addEdge(44, 56, 0.02)
g.addEdge(43, 42, 0.04)
g.addEdge(42, 41, 0.04)
g.addEdge(41, 55, 0.04)
g.addEdge(55, 56, 0.08)
g.addEdge(55, 57, 0.01)
g.addEdge(57, 62, 0.02)
g.addEdge(56, 65, 0.05)
g.addEdge(61, 82, 0.006)
g.addEdge(82, 62, 0.06)
g.addEdge(62, 63, 0.05)
g.addEdge(63, 64, 0.008)
g.addEdge(63, 83, 0.01)
g.addEdge(64, 65, 0.02)
g.addEdge(83, 65, 0.018)
g.addEdge(65, 66, 0.04)
g.addEdge(66, 67, 0.08)
g.addEdge(67, 68, 0.05)
g.addEdge(68, 69, 0.02)
g.addEdge(69, 70, 0.01)
g.addEdge(70, 71, 0.6)
g.addEdge(71, 72, 0.9)
g.addEdge(28, 25, 0.007)

locationmax = 100
location = [None] * locationmax
location[0] = { "name":"ทางเลี้ยวเข้าสนตอ", "tag":"", "x":1191, "y":92}
location[1] = { "name":"ห้องพยาบาลพุทธรักษา", "tag":"ห้องพยาบาล", "x":1271, "y":92}
location[2] = { "name":"ตึกคุณหญิงหรั่ง", "tag":"ตึก, หรั่ง", "x":1366, "y":92}
location[3] = { "name":"สมาคมนักเรียนเก่าโรงเรียนเตรียมอุดมศึกษา", "tag":"สนตอ", "x":1412, "y":92}
location[4] = { "name":"สวนพฤกษศาสตร์", "tag":"เรือนเกษตร, เกษตร, สวน", "x":709, "y":139}
location[5] = { "name":"ตึก 72 พรรษา", "tag":"ตึก, 72", "x":763, "y":139}
location[6] = { "name":"สามแยก72", "tag":"", "x":798, "y":139}
location[7] = { "name":"ห้องน้ำตึก 72 ปี", "tag":"ห้องน้ำ, 72", "x":947, "y":139}
location[8] = { "name":"ตึก 8", "tag":"ตึก, 8", "x":1061, "y":139}
location[9] = { "name":"ห้องน้ำตึก 8", "tag":"ตึก, 8", "x":1141, "y":139}
location[10] = { "name":"สามแยกหญิงหรั่ง", "tag":"", "x":1191, "y":139}
location[11] = { "name":"ตึก 60 ปี", "tag":"ตึก, 60", "x":709, "y":208}
location[12] = { "name":"สามแยกหญิงหรั่งล่าง", "tag":"", "x":1191, "y":208}
location[13] = { "name":"ห้องน้ำตึกคุณหญิงหรั่ง", "tag":"ห้องน้ำ, หรั่ง", "x":1373, "y":208}
location[14] = { "name":"ทางเลี้ยวห้องน้ำหญิงหรั่ง", "tag":"", "x":1373, "y":235}
location[15] = { "name":"ทางเลี้ยงหญิงหรั่งไปประตูฟ้า", "tag":"", "x":1412, "y":235}
location[16] = { "name":"ประตูตึก 50 ปี", "tag":"ประตู, ประตูฟ้า", "x":1412, "y":283}
location[17] = { "name":"โรงอาหารโดมทอง", "tag":"โรงอาหาร, โดมทอง", "x":1191, "y":325}
location[18] = { "name":"โรงอาหารตึก 50 ปี", "tag":"โรงอาหาร, 50", "x":1295, "y":325}
location[19] = { "name":"ตึก 50 ปี", "tag":"ตึก, 50", "x":1359, "y":325}
location[20] = { "name":"ห้องน้ำตึก 55 ปี", "tag":"ห้องน้ำ, 55", "x":1412, "y":325}
location[21] = { "name":"ทางเลี้ยงห้องน้ำ60", "tag":"", "x":678, "y":356}
location[22] = { "name":"สามแยกลานบานเย็น", "tag":"", "x":709, "y":356}
location[23] = { "name":"สนามฟุตบอล", "tag":"สนาม, สนามบอล", "x":798, "y":356}
location[24] = { "name":"ห้องน้ำตึก 60 ปี", "tag":"ห้องน้ำ, 60", "x":678, "y":405}
location[25] = { "name":"ตึก 55 ปี", "tag":"ตึก, 55", "x":1295, "y":405}
location[26] = { "name":"ทางเลี้ยวโดมทอง", "tag":"", "x":1191, "y":441}
location[27] = { "name":"สามแยกโดมทอง", "tag":"", "x":1213, "y":441}
location[28] = { "name":"ทางเลี้ยว55", "tag":"", "x":1297, "y":441}
location[29] = { "name":"ทางเลี้ยวโรงยิม", "tag":"", "x":650, "y":454}
location[30] = { "name":"ตึก 9", "tag":"ตึก, 9", "x":729, "y":454}
location[31] = { "name":"โรงยิม", "tag":"ยิม", "x":650, "y":540}
location[32] = { "name":"ทางเลี้ยว81", "tag":"", "x":990, "y":540}
location[33] = { "name":"ทางเลี้ยวขวาโล่ง", "tag":"", "x":1213, "y":540}
location[34] = { "name":"ทางเลี้ยวโรงใหญ่", "tag":"", "x":638, "y":621}
location[35] = { "name":"สามแยกลาน70", "tag":"", "x":737, "y":621}
location[36] = { "name":"สามแยกห้องน้ำ81", "tag":"", "x":798, "y":621}
location[37] = { "name":"ทางเลี้ยวห้องน้ำ81", "tag":"", "x":798, "y":641}
location[38] = { "name":"ตึก 81 ปี", "tag":"ตึก, 81", "x":848, "y":641}
location[39] = { "name":"สามแยกแปดเอ็ด", "tag":"", "x":990, "y":641}
location[40] = { "name":"โรงใหญ่", "tag":"โรงอาหาร", "x":638, "y":706}
location[41] = { "name":"ห้องน้ำตึกศิลปะ", "tag":"ห้องน้ำ, ศิลปะ", "x":199, "y":739}
location[42] = { "name":"ตึกศิลปะ", "tag":"ตึก, ศิลปะ", "x":334, "y":739}
location[43] = { "name":"ทางเลี้ยวตึกศิลปะ", "tag":"", "x":442, "y":739}
location[44] = { "name":"สามแยกคูบัว", "tag":"", "x":442, "y":782}
location[45] = { "name":"หลังลานเทเล", "tag":"", "x":521, "y":782}
location[46] = { "name":"สามแยกเทเล", "tag":"", "x":592, "y":782}
location[47] = { "name":"ศาลาดนตรีไทย", "tag":"ศาลา, ดนตรี", "x":638, "y":782}
location[48] = { "name":"ทางเลี้ยวซ้ายหอสมุด", "tag":"", "x":848, "y":782}
location[49] = { "name":"หอสมุด", "tag":"ห้องสมุด, หอ", "x":904, "y":782}
location[50] = { "name":"ทางเลี้ยวขวาหอสมุด", "tag":"", "x":990, "y":782}
location[51] = { "name":"สามแยกสวนหิน", "tag":"", "x":592, "y":861}
location[52] = { "name":"สนามวอลเลย์บอล", "tag":"สนาม, วอล, วอลเลย์", "x":635, "y":861}
location[53] = { "name":"สนามบาส", "tag":"สนาม, บาส", "x":904, "y":861}
location[54] = { "name":"ห้องนันทนาการ", "tag":"ห้อง, นันทนาการ", "x":999, "y":861}
location[55] = { "name":"สามแยกตึกหนึ่งบน", "tag":"", "x":199, "y":879}
location[56] = { "name":"ลานเทเล", "tag":"ลาน, เทเลทับบี้", "x":442, "y":879}
location[57] = { "name":"ประชาสัมพันธ์", "tag":"ประชา, ประชาสัมพันธ์", "x":199, "y":929}
location[58] = { "name":"สวนหินปิ่นหทัย", "tag":"สวนหิน, สวน, ปิ่นหทัย", "x":592, "y":929}
location[59] = { "name":"ทางเลี้ยว2.5", "tag":"", "x":884, "y":929}
location[60] = { "name":"ทางเลี้ยวหนามบาส", "tag":"", "x":898, "y":898}
location[61] = { "name":"ประตูพญาไท", "tag":"ประตู, พญาไท", "x":145, "y":1023} 
location[62] = { "name":"สามแยกพญาไท", "tag":"", "x":199, "y":1023}
location[63] = { "name":"ตึก 1", "tag":"ตึก, 1", "x":290, "y":1023}
location[64] = { "name":"ห้องน้ำตึก 1", "tag":"ห้องน้ำ, 1", "x":398, "y":1023} 
location[65] = { "name":"สามแยกพยบ1", "tag":"", "x":442, "y":1023}
location[66] = { "name":"สามแยก2ซ้าย", "tag":"", "x":592, "y":1023}
location[67] = { "name":"ตึก 2", "tag":"ตึก, 2", "x":737, "y":1023}
location[68] = { "name":"สามแยก2ขวา", "tag":"", "x":884, "y":1023}
location[69] = { "name":"ห้องน้ำสนามเทนนิส", "tag":"ห้องน้ำ, เทนนิส, 2.5, ห้องน้ำ 2.5", "x":952, "y":1023}
location[70] = { "name":"สามแยก3", "tag":"", "x":999, "y":1023}
location[71] = { "name":"ตึก 3", "tag":"ตึก, 3", "x":1113, "y":1023}
location[72] = { "name":"ประตูปทุมวัน", "tag":"ปทุมวัน, ประตู, มศว", "x":1274, "y":1023}
location[73] = { "name":"สามแยกตึก9", "tag":"", "x":678, "y":454}
location[74] = { "name":"ลานบานเย็น", "tag":"ลาน, บานเย็น", "x":709, "y":208}
location[75] = { "name":"ลาน 70 ปี", "tag":"ลาน, 70", "x":690, "y":621}
location[76] = { "name":"ห้องน้ำตึก 81 ปี", "tag":"ห้องน้ำ, 81", "x":848, "y":641}
location[77] = { "name":"ลาน ATM", "tag":"ลาน", "x":638, "y":706}
location[78] = { "name":"ตึก 80 ปี", "tag":"ตึก, 80", "x":638, "y":706}
location[79] = { "name":"โรงอาหารตึก 80 ปี", "tag":"โรงอาหาร, 80", "x":638, "y":706}
location[80] = { "name":"ห้องน้ำตึก 80 ปี", "tag":"ห้องน้ำ, 80", "x":638, "y":706}
location[81] = { "name":"สนามเทนนิส", "tag":"สนาม, เทนนิส", "x":904, "y":861}
location[82] = { "name":"รูปปั้นร.5", "tag":"ร.5, รูปปั้น", "x":145, "y":1023}
location[83] = { "name":"ห้องพยาบาลตึก 1", "tag":"ห้องพยาบาล, 1, ห้อง, พยาบาล", "x":398, "y":1023}


# s = 63 ; d = 30
# print ("Following are all different paths from % d to % d :" %(s, d))
# g.printAllPaths(s, d)
# # This code is contributed by Neelam Yadav
# print("short path")
# print(g.route)

pathid = []
points = []


startidx = 0
endidx = 99
filenumber = 0
itemcnt = 0
for x in sys.argv:
    filenumber = (int(x) if itemcnt == 1 else filenumber)
    startidx = (int(x) if itemcnt == 2 else startidx)
    endidx = (int(x) if itemcnt == 3 else endidx)
    itemcnt += 1


# if filenumber == 0:
# 	outputfile = './datax.json'
# else:
outputfile = "./data{}.json".format(filenumber if filenumber> 0 else "")
print (outputfile)

for i, val in enumerate(location):
	if val is not None and len(val["tag"]) > 0 :
		pathid.append(i)
		# print(i, val["name"])

datacnt = 0
with open(outputfile, 'w') as f:
	f.write("[")
	for startIdx in pathid:
		if startIdx >= startidx and startIdx <= endidx:
			for endIdx in pathid:
				if startIdx != endIdx:
					found = False
					for point in points:
						if point[0] == startIdx and point[1] == endIdx:
							found = True
							break

					if not found:
						g.routelen = 0
						g.beginpath = startIdx
						g.printAllPaths(startIdx, endIdx)
						if g.routelen > 0:
							print(g.route)
							f.write(',\n' if datacnt > 0 else '\n' )
							json.dump(g.route,f)
							datacnt = datacnt + 1
							points.append([startIdx, endIdx])

		# 		if datacnt > 100:
		# 			break

		# if datacnt > 100:
		# 	break
	f.write("\n]")
