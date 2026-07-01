import random
import typing

def gen_event(names: list, actions: list, total_events: int):
    """Generate events baces on names, actions and number of events"""
    for event_id in range(1, total_events + 1):
        name = random.choice(names)
        action = random.choice(actions)
        yield (print(f"Event {event_id - 1}: Player {name} did action {action}"))

def gen_event_2(names: list, actions: list, total_events: int):
    """Generate events baces on names, actions and number of events"""
    for event_id in range(1, total_events + 1):
        name = random.choice(names)
        action = random.choice(actions)
        yield name, action

def ft_data_stream() -> None:

    names = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]

    """Generate 1000 events"""
    # gen_objects = gen_event(names, actions, 1000)
    # for item in gen_objects:
    #     next(gen_objects)
    
    """Generate a list of 10 tuples"""
    # event_list = []
    # for _ in range(1, 11):
    #     ten_events = gen_event_2(names, actions, 10)
    #     event_list.append(next(ten_events))
    # print("Build list of 10 events:", (event_list))

    """Generate consume events"""
    event_list = []
    for _ in range(1, 11):
        ten_events = gen_event_2(names, actions, 11)
        event_list.append(next(ten_events))
    
    while len(event_list) > 0:
        index = random.randrange(len(event_list))
        print("Got event from list:", event_list[index])
        event_list.pop(index)
        print("Remains in list:", event_list)

if __name__ == "__main__":
    ft_data_stream()


# i = 1
#     for i in range(1, 100):
#         gen_objects = gen_event(names, actions, i)
#         print(next(gen_objects))
#         i += 1

# import random

# def gen_event(names: list, actions: list, total_events: int):
#     """Generate events baces on names, actions and number of events"""
#     for event_id in range(1, total_events + 1):
#         name = random.choice(names)
#         action = random.choice(actions)
#         yield (print(f"Event {event_id - 1}: Player {name} did action {action}"))



# def ft_data_stream() -> None:

#     names = ["alice", "bob", "charlie", "dylan"]
#     actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]
#     gen_objects = gen_event(names, actions, 1000)
#     for item in gen_objects:
#         next(gen_objects)
#     ten_events = gen_event(names, actions, 10)

#  ten_events = gen_event(names, actions, 10)
#     for item in ten_events:
#         next(ten_events)
#         print(f"Build the list of 10 events: {item}")


# if __name__ == "__main__":
#     ft_data_stream()
