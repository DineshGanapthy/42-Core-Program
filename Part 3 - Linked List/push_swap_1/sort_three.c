/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_three.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 15:49:29 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/25 18:43:09 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sort_three(t_stack_node	**a) // A function that sorts three nodes.
{
	t_stack_node	*biggest_node;// Pointer to store pointer to the biggest node.

	biggest_node = find_max(*a); 
	if (biggest_node == *a) // Checks if the current node is the biggest. 3-1-2
		ra(a, false); // If it is rotate the top(aka biggest) node to the bottem of the stack. 1-2-3
	else if ((*a)->next == biggest_node) // To check if the second node is the biggest in the stack. 2-3-1 or 1-3-2
		rra(a, false); // If it is reverse the bottem node to the top of the stack. 1-2-3 or 2-1-3
	if ((*a)->nbr > (*a)->next->nbr) // Check if the first node is bigger then teh second node and if the bottem
									// is the biggest. e.g. 2-1-3 
		sa(a,false); // If so swap top and second node so now it becomes 1-2-3.
}