/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rev_rotate.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 11:21:36 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/24 16:16:21 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/push_swap.h"

static void rev_rotate(t_stack_node **stack) // A function taht moes the last to first and moves everthing downwards on the stack.
{
	t_stack_node	*last_n; // A pointer to store the pointer to the last node

	if (!stack || !(*stack)->next) // To check if the stack is empty or if there is only one node.
		return ;
	last_n = find_last_n(*stack); // To find the last node and set it to last_n.
	last_n->prev->next = NULL; // Assigning th esecond last's node's next pointer to point ot NULL.
	last_n->next = *stack; // Getting the last's next to point to the current head node. 
	last_n->prev = NULL; // assigning the last's pervious to point to null.
	*stack = last_n; // assigning the head node to the last node. 
	last_n->next->prev = last_n; // gettting number 1 or the second node's previous to point to the new head node.
}

void	rra(t_stack_node **a, bool print) // reverse roate a, last becomes first. first becomes second, second last becomes last. 
{
	rev_rotate(a);
	if (!print)
		write(1, "rra\n", 4);
		//ft_printf("rra\n");
}

void	rrb(t_stack_node **b, bool print) // rev roate b, everyhing moves down one.
{
	rev_rotate(b);
	if (!print)
		write(1, "rrb\n", 4);
		//ft_printf("rrb\n");
}

void	rrr(t_stack_node **a, t_stack_node **b, bool print) // rev rotate a & b. 
{
	rev_rotate(a);
	rev_rotate(b);
	if (!print)
		write(1, "rrr\n", 4);
		//ft_printf("rrr\n");
}
