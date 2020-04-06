""" 狄克斯特算法 """

graph = {}
graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}  # 终点为空

infinity = float("inf")  # 无穷大
costs = {'a': 6, 'b': 2, 'fin': infinity}
# 等效
# costs = {}
# costs['a'] = 6
# costs['b'] = 2
# costs['fin'] = infinity

parents = {'a': 'start', 'b': 'start', 'fin': None}
processed = []


def find_lowest_cost_node(costs):
    # 在未处理的节点中找出开销最小的节点
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def main():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            costs[n] = new_cost
            parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


if __name__ == '__main__':
    main()
