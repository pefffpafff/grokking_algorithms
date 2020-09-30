#Хеш таблица со всеми соседями
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]['fin'] = 5
graph["b"]["a"] = 3

graph["fin"] = {}

#бесконечность
infinity = float("inf")

#Таблица стоимостей
#costs - расходы
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#Таблица родителей
parents = {}
parents["a"] = 'start'
parents["b"] = 'start'
parents["fin"] = None

#Массив отработонных узлов
processed = []

def find_lowest_cost_node(costs):
	lowest_cost = float("inf")
	lowest_cost_node = None
	#Перебираем все узлы
	for node in costs:
		cost = costs[node]
		#Если это узел с наименьшей стоимостью из уже виденных и он еще не был отработан  
		if cost < lowest_cost and node not in processed:
			#Он назначается новым узлом с науменьшей стоимостью 
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not  None:
	#Получаем стоимость этого узла
	cost = costs[node]
	#Получаем соседей этого узла
	neighbors = graph[node]
	#Перебираем соседей
	#n содержит А
	for n in neighbors.keys():
		#cost содержит В, то есть 2
		#neighbors[n] - расстояние от В до А: 3
		new_cost = cost + neighbors[n]
		#>>>5
		#Сравним их стоимость
		if costs[n] > new_cost:
			costs[n] = new_cost #costs[n] - старая стоимость(6), new_cost - новая стоимость(5)
			#n - A, node - B
			parents[n] = node
	processed.append(node)
	node = find_lowest_cost_node(costs)

print("Стоимость от начала до каждого узла:")
print(costs)