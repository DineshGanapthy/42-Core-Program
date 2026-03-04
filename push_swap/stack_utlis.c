/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_utlis.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 15:42:23 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/03 15:48:43 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

bool	stack_sorted(t_stack_node *stack)
{
	if (!stack)
		return (1);
	while (stack ->next)
	{
		if (stack->nbr > stack->next->nbr)
			return (false);
		stack = stack->next;
	}
	return (true);
}

t_stack_node	*find_min(t_stack_node *stack)
{
	long			min;
	t_stack_node	*min_node;
	
	if (!stack)
		return (NULL);
	min = LONG_MAX;
	while (stack)
	{
		if (stack-> < min)
		{
			min = stack->nbr;
			min_node = stack;
		}
		stack = stack->next;
	}
	return (min_node);
} 