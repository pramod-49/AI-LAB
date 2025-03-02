def initialize_state():
    return {
        "monkey_pos": (0, 0),
        "box_pos": (2, 2),
        "bananas_pos": (1, 1),
        "monkey_on_box": False,
        "bananas": "ceiling",
    }

def is_goal(state):
    return state["bananas"] == "taken"

def move_monkey(state, new_pos):
    if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
        state["monkey_pos"] = new_pos
        print(f"Monkey moved to {new_pos}.")
    else:
        print("Invalid move.")

def move_box(state):
    if state["monkey_pos"] == state["box_pos"] and not state["monkey_on_box"]:
        state["box_pos"] = state["bananas_pos"]
        print("Monkey moved the box under the bananas.")
    else:
        print("Monkey cannot move the box.")

def climb_box(state):
    if state["monkey_pos"] == state["box_pos"] and not state["monkey_on_box"]:
        state["monkey_on_box"] = True
        print("Monkey climbed onto the box.")
    else:
        print("Monkey cannot climb the box.")

def take_bananas(state):
    if state["monkey_on_box"] and state["box_pos"] == state["bananas_pos"]:
        state["bananas"] = "taken"
        print("Monkey took the bananas!")
    else:
        print("Monkey cannot take the bananas.")

def reset_state():
    return initialize_state()

state = initialize_state()

move_monkey(state, (2, 2))
move_box(state)
move_monkey(state, (1, 1))
climb_box(state)
take_bananas(state)

if is_goal(state):
    print("Goal achieved: Monkey has the bananas!")
else:
    print("Goal not achieved.")
