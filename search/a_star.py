from aoc_lib.basic.types import *
from aoc_lib.data_structs.linked_list import GraphNode
from aoc_lib.data_structs.queues import PriorityQueue


def a_star(
    initial_node: T,
    test_goal: Callable[[T], bool],
    get_successors: Callable[[T], list[T]],
    heuristic: Callable[[T], float],
) -> Optional[GraphNode[T]]:
    queue: PriorityQueue[GraphNode[T]] = PriorityQueue()  # where we have yet to go
    queue.push(GraphNode(initial_node, None, 0.0, heuristic(initial_node)))
    visited: dict[T, float] = {initial_node: 0.0}  # where we have been

    # keep going while there is more to visit
    while not queue.empty:
        current_node = queue.pop()
        current_state = current_node.state

        if test_goal(current_state):
            return current_node

        # check where we can go next and haven't visited
        for child in get_successors(current_state):
            # 1 assumes a grid, need a cost function for more sophisticated applications
            new_cost = current_node.cost + 1
            if child not in visited or visited[child] > new_cost:
                visited[child] = new_cost
                queue.push(GraphNode(child, current_node, new_cost, heuristic(child)))

    return None  # went through everything and never found goal

