/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 11:49:31 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/24 16:16:02 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/push_swap.h"

static void swap(t_stack_node **head) // This is the fuction that swap the top node with the second node of teh stack. 
{
	if (!*head || !(*head)->next) // Checking if the top node or the second node of the stack exists.
		return ;
	*head = (*head)->next; // Assigning the new head node to be "B" or the next node.
	(*head)->prev->prev = *head; // The prevoius previous of B which is the previous of A is now pointing to B. 
	(*head)->prev->next = (*head)->next; // Here we are assigning "B" previous which is A and A next = we are assigning to B next whihc is C. 
										// So we are saying A's next is now pointing to C.
	if ((*head)->next) // This is checking if "B" orginally had a next ? "C"
		(*head)->next->prev = (*head)->prev; // If yes we say B's next which is C's previous = is not pointing to B's previous whiich is A.
											// So C's previous is now pointing to A.
	(*head)->next = (*head)->prev; // B's next is now pointing to B's previous which is A, B's next is now A which is performing the swap. 
	(*head)->prev = NULL; // Now We set B's previous to point to NULL.
}

void	sa(t_stack_node **a, bool print) // Swap the first two nodes of stack "a."
{
	swap(a);
	if (!print)
		write(1, "sa\n", 3);
		//ft_printf("sa\n");
}

void	sb(t_stack_node **b, bool print) // Swap the first two nodes of stack "b."
{
	swap(b);
	if (!print)
		write(1, "sb\n", 3);
		//ft_printf("sb\n");
}

void	sa(t_stack_node **a, t_stack_node **b, bool print) // Swap both the first two noes of a & b respectively.
{
	swap(a);
	swap(b);
	if (!print)
		write(1, "ss\n", 3);
		//ft_printf("ss\n");
}
