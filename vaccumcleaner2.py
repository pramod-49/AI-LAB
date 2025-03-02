class TableDrivenAgent:
    def __init__(self):

        self.table = {
            ('clean', 'left'): 'stay idle',
            ('dirty', 'left'): 'clean',
            ('clean', 'right'): 'stay idle',
            ('dirty', 'right'): 'clean',
        }

    def perceive_and_act(self, floor_status, position):

        action = self.table.get((floor_status, position), 'Invalid state')
        return action



if __name__ == "__main__":

    agent = TableDrivenAgent()


    percepts = [
        ('dirty', 'left'),
        ('clean', 'left'),
        ('dirty', 'right'),
        ('clean', 'right'),
    ]


    for percept in percepts:
        floor_status, position = percept
        action = agent.perceive_and_act(floor_status, position)
        print(f"Percept: {percept} => Action: {action}")
