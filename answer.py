# need a number of room variable
num_rooms = 0
# dictionary for room handling. O(1) searching
graph = {}
bot_rooms = []
start_room = {}
dr_barts_room = {}


def room_maker(s_line: str) -> dict:
    line_arr = s_line.split()
    room = {}
    adjacent = []
    room['name'] = line_arr[0]
    room['bot in?'] = line_arr[1]
    i = 2
    while i < len(line_arr):
        adjacent.append(line_arr[i])
        i = i+1
    adjacent.sort()  # assure alphabetically correct order
    room['edges'] = adjacent
    return room


def find_dr_bart(start: dict) -> dict:
    traversed = []
    queue = []
    for ed in start['edges']:
        queue.append(ed)
    traversed.append(start)
    while len(queue) != 0:
        vertex = graph[queue[0]]
        queue = queue[1:len(queue)]
        if vertex not in traversed:
            traversed.append(vertex)
            for ed in vertex['edges']:
                queue.append(ed)
    return traversed[-1]


def bot_find_dr_bart(start: dict, dr_bart: dict, rooms: dict):
    traversed = []
    queue = [[start['name']]]
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in traversed:
            node_dict = rooms[node]
            neighbors = node_dict['edges']

            for n in neighbors:
                new_path = list(path)
                new_path.append(n)
                queue.append(new_path)
                if start['name'] == n:  # checking to make sure we don't loop back to the beginning
                    new_path = [n]

                if n == dr_bart['name']:
                    answer = ", ".join(new_path)
                    return answer

            traversed.append(node)


if __name__ == '__main__':
    filename: str = input()
    with open(filename) as data_file:
        lines: list[str] = data_file.readlines()
        for line in lines:
            if line == lines[0]:
                num_rooms = int(line)
                continue
            else:
                room_dict = room_maker(line)
                graph[room_dict['name']] = room_dict
                if line == lines[1]:
                    start_room = room_dict
                if room_dict['bot in?'] != 'empty':
                    bot_rooms.append(room_dict['name'])

    bot_rooms.sort()  # because we need to report in alphabetical order
    # now we have the data we need
    dr_barts_room = find_dr_bart(start_room)
    for r in bot_rooms:
        print(bot_find_dr_bart(graph[r], dr_barts_room, graph))

