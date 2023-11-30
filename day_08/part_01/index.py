from pathlib import Path

path = Path(__file__).parents[1] / "input.txt"
contents = path.read_text()

directions, nodes = contents.split("\n\n")
nodes = [node.split(" = ") for node in nodes.splitlines()]
nodes = {label: node[1:-1].split(", ") for label, node in nodes}

current_node = nodes["AAA"]
step_count = 0

while current_node is not nodes["ZZZ"]:
    for dir in directions:
        if dir == "L":
            index = 0
        elif dir == "R":
            index = 1

        next_label = current_node[index]
        current_node = nodes[next_label]
        step_count += 1

print(step_count)
