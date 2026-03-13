/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_stacks.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/04 12:24:21 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/11 16:26:43 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../inc/push_swap.h"

static void rotate_both(t_stack_node **a,
						t_stack_node **b
						t_stack_node *cheapest_node) // A function that rotates both head nodes of stack 'a' and 'b' to bottem 
													// If it's the cheapest move. 
{
	while (*b != cheapest_node->target_node
			&& *a != cheapest_node) // As long as both the head nodes are not the cheapest nodes keep rotating.
			rr(a, b, false);// Rotate a and b.
	current_index(*a); // Refresh current node positions
	current_index(*b);
}

static void rev_rotate_both(t_stack_node **a,
						t_stack_node **b
						t_stack_node *cheapest_node) // A function that rotates both tail nodes of stack 'a' and 'b' to top.
{
	while (*b != cheapest_node->target_node
			&& *a != cheapest_node) // As long as both the head nodes are not the cheapest nodes keep  reverse rotating.
			rrr(a, b, false); // Reverse rotate a and b.
	current_index(*a); // Refresh current node positions
	current_index(*b);
}


static void	move_a_to_b(t_stack_node **a, t_stack_node **b)
{
	t_stack_node	*cheapest_node; 
	
	cheapest_node = get_cheapest(*a);
	if (cheapest_node->above_median && cheapest_node->target_node->above_median)
		rotate_both(a, b, cheapest_node);
	else if (!(cheapest_node->above_median))
			&& !(cheapest_node->target_node->above_median)
			 rev_rotate_both(a, b, cheapest_node);
		prep_for_push(a, cheapest_node, 'a');
		prep_for_push(b, cheapest_node->target_node, 'b');
		pb(b, a, false);
}
static void	move_b_to_a(t_stack_node **a, t_stack_node **b)
{
	prep_for_push(a, (*b)->target_node, 'a');
	pa(a, b, false);
}
static void	min_on_top(t_stack_node **a)
{
	while ((*a)->nbr != find_min(*a)->nbr)
	{
		if(find_min(*a)->above_median)
			ra(a, false);
		else
			rra(a, false);
	}
}
void	sort_stacks(t_stack_node **a, t_stack_node **b) // A function that sort stack 'a.'
{
	int	len_a;
	
	len_a = stack_len(*a); 
	if (len_a-- > 3 && !stack_sorted(*a)) // If stack 'a' has more then three nodes and are not sorted.
		pb(b, a, false);
	if (len_a-- > 3 && !stack_sorted(*a)) // If stack 'a' still has more then three nodes and are not sorted.
		pb(b, a, false);
	while (len_a-- > 3 && !stack_sorted(*a)) // If stack 'a' still has more then three nodes and are not sorted.
	{
		init_nodes_a(*a, *b); // Iniate all nodes from both stacks. 
		move_a_to_b(a, b); // Move cheapest 'a' node into 'b' sorting them as they are being
							// pushed into 'b' until there are only three nodes left in 'b.'
	}
	sort_three(a); 
	while(*b) // Iterate through stack 'b' until end. 
	{
		init_nodes_b(*a, *b); // Iniate all nodes from both stacks.
		move_b_to_a(a, b); // Move nodes from 'b' back into 'a' in the right postition. They should be sorted in 'b.'
	}
	current_index(*a); // Refresh the current position of stack 'a'
	min_on_top(a); // Make sure the smallest number is at the top of stack 'a' it should be stoted. 
}
