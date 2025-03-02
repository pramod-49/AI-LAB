import random

def initialize_state():
    return {
        "monkey_pos": (0, 0),
        "box_pos": (2, 2),
        "bananas_pos": (1, 1),
        "monkey_on_box": False,
        "bananas": "ceiling",
        "competitor_pos": (0, 2),
    }

def is_goal(state):
    return state["bananas"] == "taken"

def move_agent(state, agent, new_pos):
    if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
        state[agent] = new_pos
        print(f"{agent.capitalize()} moved to {new_pos}.")
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
    elif state["competitor_pos"] == state["bananas_pos"]:
        state["bananas"] = "taken"
        print("Competitor took the bananas!")
    else:
        print("Bananas are still on the ceiling.")

def competitor_action(state):
    actions = [
        lambda: move_agent(state, "competitor_pos", random.choice([(0, 0), (0, 2), (2, 2), (1, 1)])),
        lambda: take_bananas(state),
    ]
    random.choice(actions)()

def reset_state():
    return initialize_state()

state = initialize_state()

while not is_goal(state):
    print("\nMonkey's turn:")
    move_agent(state, "monkey_pos", random.choice([(0, 0), (2, 2), (1, 1)]))
    if state["monkey_pos"] == state["box_pos"]:
        move_box(state)
    if state["monkey_pos"] == state["bananas_pos"]:
        climb_box(state)
        take_bananas(state)

    if is_goal(state):
        break
    print("\nCompetitor's turn:")
    competitor_action(state)

if state["bananas"] == "taken" and state["monkey_on_box"]:
    print("Goal achieved: Monkey has the bananas!")
elif state["bananas"] == "taken" and state["competitor_pos"] == state["bananas_pos"]:
    print("Competitor won: Bananas taken by the competitor!")
else:
    print("Bananas are still on the ceiling.")
