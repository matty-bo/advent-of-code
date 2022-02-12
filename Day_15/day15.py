def ga(modes, ip, shift, rel_base):
    if modes[-shift] == "0":
        return memory[ip + shift]
    elif modes[-shift] == "1":
        return ip + shift
    elif modes[-shift] == "2":
        return memory[ip + shift] + rel_base


def computer(memory, user_input, ip):
    rel_base = 0
    while ip < len(memory):
        op_code = memory[ip] % 100
        modes = str(memory[ip])[:-2].zfill(3)
        if op_code == 1:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] + memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 2:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] * memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 3:
            memory[ga(modes, ip, 1, rel_base)] = user_input
        elif op_code == 4:
            out = memory[ga(modes, ip, 1, rel_base)]
            return out
        elif op_code == 5:
            if memory[ga(modes, ip, 1, rel_base)] != 0:
                ip = memory[ga(modes, ip, 2, rel_base)]
            else:
                ip += 3
        elif op_code == 6:
            if memory[ga(modes, ip, 1, rel_base)] == 0:
                ip = memory[ga(modes, ip, 2, rel_base)]
            else:
                ip += 3
        elif op_code == 7:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] < memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 8:
            memory[ga(modes, ip, 3, rel_base)] = memory[ga(modes, ip, 1, rel_base)] == memory[ga(modes, ip, 2, rel_base)]
        elif op_code == 9:
            rel_base += memory[ga(modes, ip, 1, rel_base)]
        else:
            assert op_code == 99
            return
        if op_code in [1, 2, 7, 8]:
            ip += 4
        elif op_code in [3, 4, 9]:
            ip += 2


def back(way):
    way -= 1
    way ^= 1
    way += 1
    return way


def ways_to_try(memory,ip):
    ways = []
    for way in [1, 2, 3, 4]:
        status = computer(memory, way, ip)
        if status != 0:
            ways.append(way)
            computer(memory, back(way), ip)
    return ways


def explore(memory, ip=0):
    delta = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
    pos = (0, 0)
    past_moves = []
    to_try = {}
    way = None

    nodes = {pos}
    ox_count = 0
    ox_pos = (None, None)

    while True:
        if pos not in to_try:
            wtt =  ways_to_try(memory, ip)
            if way:
                wtt.remove(back(way))
            to_try[pos] = wtt

        if to_try[pos]:
            backtrack = False
            way = to_try[pos].pop()

        else:
            backtrack = True
            if not past_moves:
                break
            way = back(past_moves.pop())

        status = computer(memory, way, ip)
        pos = tuple(map(sum, zip(pos, delta[way])))

        if not backtrack:
            past_moves.append(way)
            nodes.add(pos)

        if status == 2:
            ox_count = len(past_moves) if ox_count == 0 else min(ox_count, len(past_moves))
            ox_pos = pos

    return nodes, ox_pos, ox_count


def create_graph(nodes):
    delta = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
    graph = {n: [tuple(map(sum, zip(n, delta[way]))) for way in [1, 2, 3, 4]] for n in nodes}

    for parent, children in graph.items():
        for n in children:
            if n not in graph.keys():
                graph[parent].remove(n)
    return graph


def Dijkstras_Oxygen_Path(graph, source):
    distance = {n: 999999999999 for n in graph}
    distance[source] = 0

    dict_node_length = {source: 0}

    while dict_node_length:

        source_node = min(dict_node_length, key=lambda k: dict_node_length[k])
        del dict_node_length[source_node]

        for adjnode in graph[source_node]:
            length_to_adjnode = 1

            if adjnode in distance:
                if distance[adjnode] > distance[source_node] + length_to_adjnode:
                    distance[adjnode] = distance[source_node] + length_to_adjnode
                    dict_node_length[adjnode] = distance[adjnode]

    return max(distance[n] for n in graph)


filename = "day15_data.txt"
with open(filename) as file:
    memory = list(map(int, file.read().split(',')))
nodes, ox_pos, ox_count= explore(memory)
graph = create_graph(nodes)
len_ox_path = Dijkstras_Oxygen_Path(graph, ox_pos)
print(f'Answer 1: {ox_count}')
print(f'Answer 2: {len_ox_path}')
