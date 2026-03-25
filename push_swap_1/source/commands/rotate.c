/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 11:31:30 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/24 16:16:29 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/push_swap.h"

static void rotate(t_stack_node **stack) // A fuction to rotate the stacks top node to the bottom and move
										// everthing up by one. 
{
	t_stack_node	*last_node; // A t_stack_node pointer to store the pointer to the last node. 

	if (!*stack || !(*stack)->next) // To check if the stack is empty or if there is one node. 
		return ;
	last_node = find_last(*stack); // find last node in stack and assign it to last_node.
	last_node->next = *stack; // Pointing the last nodes next pointer to the current head pointer. Making 5's next point to 1.
	*stack = (*stack)->next; // Assigning the head node as the second node in the stack.
	(*stack)->prev = NULL; // Assigning the new head's previous pointer to NULL. (detaching it from the previous top)
	last_node->next->prev = last_node; // Saying the old head (1) which is now the new last node's(1) previous pointer 
										//is now pointing to the old last_node(5). 1's prev is 5.
	last_node->next->next = NULL; // Now we are assigning the new last nodes's next pointer to NuLL to properly NULL terminate the stack. 
}

void	ra(t_stack_node **a, bool print) // rotate a first to last, second to first, last to sencond last,
{
	rotate(a);
	if (!print)
		write(1, "ra\n", 3);
		//ft_printf("ra\n");
}

void	rb(t_stack_node **b, bool print) // rorate b, evertything up by one.
{
	rotate(b);
	if (!print)
		write(1, "rb\n", 3);
		//ft_printf("rb\n");
}

void	rr(t_stack_node **a, t_stack_node **b, bool print) // rotate a and b
{
	rotate(a);
	rotate(b);
	if (!print)
		write(1, "rr\n", 3);
		//ft_printf("rr\n");
}

