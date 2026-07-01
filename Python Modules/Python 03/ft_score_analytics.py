import sys

def ft_score_analytics() -> None:
    print("=== Player Score Analysis ===")
    
    # if (len(sys.argv) == 1):
    #     print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...\n")
    #     return
        
    scores_list = []
    for (argument) in sys.argv[1:]:
        try:
            int(argument)
            scores_list.append(int(argument))
        except ValueError:
            print(f"Invalid parameter '{argument}'")
            
    if (len(scores_list) == 0):
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...\n")
    else:
        print(f"Scores proccesed: {scores_list}")
        print(f"Total players: {len(scores_list)}")
        print(f"Total score: {sum(scores_list)}")
        print(f"Average score: {(sum(scores_list))/len(scores_list)}")
        print(f"High score: {max(scores_list)}")
        print(f"Low score: {min(scores_list)}")
        print(f"Score range: {max(scores_list)-min(scores_list)}")

if __name__ == "__main__":
    ft_score_analytics()

    
    
    
    
    
    
    
    
    
    
    
    
    
    # print(f"Program name: {sys.argv[0]}")
    # if len(sys.argv) == 1:
    # 	print("No arguments provided!")
    # 	print(f"Total Arguments: {len(sys.argv)}\n")
    # else:
    # 	i = 1
    # 	print(f"Total recieved: {len(sys.argv) - 1}")
    # 	for (arguments) in sys.argv[1:]:
    # 		print(f"Arguments {i}: {arguments}")
    # 		i += 1
    # 	print(f"Total Arguments: {len(sys.argv)}\n")