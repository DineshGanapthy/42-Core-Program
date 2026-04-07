*This project has been created as part of the 42 curriculum by dganapat.*

 
**Instruction :-**  

To compile all the files, you need to get into the push_swap directory and type “make all.” The compilation instructions/script have been written in my makefile in order for the object files to be created. Once all the object files have been created type this in the terminal./push_swap “55 3 4” and input all the desired numbers to be sorted. These are the two instructions needed for compilation and execution of the program. 

The specific compilation instruction requires using the cc with these flags  -Wall -Wextra -Werror. Additionally the makefile also contains $(NAME), all, clean, fclean and re. Again all these specific instructions have been included in the make file. 

**Description :-**

The problem is to sort a set of numbers in ascending order in the most efficient way using two stacks and specific commands such as push, swap, rotate and reverse rotate. The objective is to create an algorithm that performs this efficiently. 

Firstly I will provide a general overview of my code before going into detail function by function. 

I have chosen to use the turk sort algorithm and will explain how it works. 

Initially I will take all the input numbers and place it in stack A. Next I will begin moving most of the numbers from stack A onto Stack B in descending order until there are three numbers left in stack A. 

Then I would sort the three numbers in stack A and move all the numbers from stack B to stack A in ascending order. Finally I will make sure the top number is the smallest number and the bottom the largest via command rotation. This is a brief overview and lets go over the details.

Firstly when presented with a list of numbers I will place it all in stack A in the order it is received. Next I will push most of the numbers to stack B until stack A is left with only three numbers. In this process I will push the first two numbers randomly but after that all the numbers will be pushed in descending order based on their push cost, this is the heart of the algorithm which will be explained later on . 

First I will start by declaring two data structures - Stack A and Stack B - and setting them to null, which just means they are empty. Next we will run the input arguments - which is the list of numbers inputted through the terminal - through the error function. We use our “init_stack_a” and argv[1] to take the argument of numbers and first check for errors. It has to be able to take two types of arguments , command line arguments or strings. If it is a string we will use our famous function ‘ft_split” to split the numbers into an array of numbers. 

The specific error function we use “error_syntax” which checks if there is a sign in front of the number and if all the characters are numbers. If there are errors the function returns “1” and frees stack A and outputs an error statement in the terminal. 

Next if this text is passed we will convert all numbers to long, using “ft_atol” which means ascii to long. Similarly to our function in libft but just changed to a long instead of an integer. Next we check if the number is greater or smaller then INT_MAX and INT_MIN. If it is, we free stack A. Next we check for duplicates using the “error_duplicate” function where we just look at two numbers that are the same. Again if they are we free stack A or else we keep going on. Next we create a node and add this number to it and fill up all the other variables required in that node e.g. next, index, cheapest, previous etc. 

Now a number is successfully added to stack A, we do it for all numbers. Next we check if stack A is sorted, if it's not we will sort it, using the “sort_three” algorithm for three numbers or just swap the two numbers if there are two numbers. The “sort_three” algorithm works like this, it checks if the first/top node is the biggest, if it is it will rotate it and place it at the bottom of the stack. Next it will check if the middle number is the biggest and then reverse rotate the bottom to the top. And finally it will check if the top number is bigger then the second number and it will swap the top and second number. This will sort the three numbers. 

Now here is the heart of the algorithm in this function called “sort_stacks.” This function first counts the number of nodes in stack A and according to the amount of nodes in stack A it acts accordingly. If stack A has more than three nodes and it pushes the first two nodes to stack B after the first two have been pushed, the remaining nodes being pushed to stack B will be pushed descending order accordingly by using these two functions “init_nodes_a” and “move_a_to_b”. “Inti_nodes_a” involves 5 functions in it, the first being ‘current_index” this just to create an index number for all the nodes and also to let it know if it’s above or below the median line. ‘Set_target_a’ this function matches each node in stack A with its best match(closest) match in stack B. ‘cost_analysis_a’ this function calculates the cost of moving a node and its adjacent target node in B to the top of each of these stacks and adds this number together. Finally ‘set_cheapest’ is a function to find the cheapest cost by iterating through the stack and finding the node with the lowest push cost. Now this is what the ‘init_nodes_a’ processes. Then after all this is calculated we use the function ‘move_a_to_b’ to move the cheapest value to stack B, this is so we use the least amount of moves possible and the program is more efficient. We keep doing this until we have only three nodes in stack A and then it comes out of the loop and we put stack a in the ‘sort_three’ function. 

Now all this is done we move all the nodes from stack B back to stack A in descending order using the process. Using ‘init_nodes_b’ and ‘move_b_to_a.’ Now when all the nodes have been pushed back to stack A we use function ‘current_index’ to refresh the position of and indexes of stack A. Finally we make sure the smallest nodes (number) is on the top of the stack A using the function min_on_top(a). Once this is done all the numbers in stack A are now sorted from smallest to biggest and we are done. Each time a command is used such as push, swap, rotate to reverse rotate, its command is printed on to the terminal for the user to view. 
push swap

**Resources :-** 

I used three main resources, firstly I used google to research time and space complexities and learned how they are related to algorithm efficiencies. Next I skimmed a few medium articles on push_swap and different ways I could approach it. I finally settled with an author called  - “A. Yigit Ogun” that implemented a turk sort algorithm and I learned the general concept and the outline of the algorithm from reading his article. Next I watched a tutorial by thuggonaut aka “Twee Quematon” and learned the details of implementing this algorithm. I followed along and used it as a guide to write my algorithm. 

Push Swap — A journey to find most efficient sorting algorithm - https://medium.com/@ayogun/push-swap-c1f5d2d41e97

Push Swap Tutorial - https://www.youtube.com/watch?v=wRvipSG4Mmk

AI Usage : When using google to search for time and space complexity the top came up with an AL generated summary and result. Apart from this search result AI was not used at all in the entire project. 
