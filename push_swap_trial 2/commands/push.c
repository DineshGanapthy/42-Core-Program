/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 11:05:52 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/11 13:42:23 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../inc/push_swap.h"

static	void push(t_stack_node **dst, t_stack_node **src) // A function that pushes the top of one node to another
{
	t_stack_node	*push_node; // A t_stack_node pointer to store teh pointer of the node that is being pushed.

	if (!*src) // Checking if the current stack is empty.
		return ;
	push_node = *src; // The push_node is assigned the top node of the current stack.  
	*src = (*src)->next; // Assigning the new source to be the next node on the list as it will become the new Head node.
	if (*src) // Checks if the new top node exists.
		(*src)->prev = NULL; // Assigning the prev pointer of the new Head node to null, as it should be. 
	push_node->prev = NULL; // Detaching the push node from the stack. (Check this should be next instead of previous)
	if (!*dst) // Checking if the destination stac is empty
	{
		*dst = push_node; // If empty make the push node the head node.
		push_node->next = NULL; // Properly NULL terminate the stack and also making sure this is the last node.
	}
	else
	{
		push_node->next = *dst; // Assigning the pushed node's next pointer pointing to the current first head node.
		push_node->next->prev = push_node; // Assiggning the current head node previous pointer pointing to the pushed node (New Head).
		*dst = push_node; // Making the pushed nod ethe new head o fthe stack.
	}
}

void	pa(t_stack_node **a, t_stack_node **b, bool print) // Pushes B on top of A.
{
	push(a, b);
	if (!print)
		ft_printf("pa\n");
}

void	pb(t_stack_node **b, t_stack_node **a, bool print) // Pushes A on top of B. 
{
	push(b, a);
	if (!print)
		ft_printf("pb\n");
}
