/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/27 13:46:52 by dganapat          #+#    #+#             */
/*   Updated: 2026/02/27 14:01:48 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdbool.h>
// Boolean flags will be used to prin tth elist of our commands.
# include <limits.h>
// which include the interger min and max and macros. 
# include "../libft/inc/libft.h"
# include "../libft/inc/ft_print.h"

typedef struct s_stack_node
{
	int		nbr;
	int		index;
	int		push_cost;
	bool	above_median;
	bool	cheapest;
	
	struct s_stack_node *target_node;
	struct s_stack_node *next;
	struct s_stack_node *previous;
}	t_stack_node; // Just a shoeterned name for our structure we just created.

// Handle errors

// Stack intiation

// Nodes intiation

// Stack Utils

// Commands

// Algorithms

#endif


typedef struct s_stack_node
{
	int		nbr;
	int		index;
	int		push_cost;
	bool	middle_line;
	bool	lowest_move;

	struct s_stack_node *front;
	struct s_stack_node *back;
	
}
