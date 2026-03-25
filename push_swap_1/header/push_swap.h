/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/27 13:46:52 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/24 16:14:06 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdbool.h>
// Boolean flags will be used to prin tth elist of our commands.
# include <limits.h>
// which include the interger min and max and macros. 
# include <unistd.h>
//# include "../libft/inc/libft.h"
//# include "../libft/inc/ft_print.h"

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
int				error_syntax(char *str_n);
int				error_duplicate(t_stack_node *a, int n);
void			free_stack(t_stack_node **stack);
void			free_errors(t_stack_node **a);

// Standard input
char			**ft_split(char *s, char c);

// Stack intiation
void			init_stack_a(t_stack_node **a, char **argv);

// Nodes intiation
void			current_index(t_stack_node *stack);
void			init_nodes_a(t_stack_node *a, t_stack_node *b);
void			init_nodes_b(t_stack_node *a, t_stack_node *b);
void			set_cheapest(t_stack_node *stack);
t_stack_node    *get_cheapest(t_stack_node *stack);
void    		prep_for_push(t_stack_node **stack, t_stack_node *top_node, char stack_name);

// Stack Utils
int				stack_len(t_stack_node	*stack);
t_stack_node	*find_last(t_stack_node	*stack);
t_stack_node	*find_min(t_stack_node *stack);
t_stack_node	*find_max(t_stack_node *stack);
bool			stack_sorted(t_stack_node *stack);

// Commands
void			pa(t_stack_node **a, t_stack_node **b, bool print);
void			pb(t_stack_node **b, t_stack_node **a, bool print);
void			sa(t_stack_node **a, bool print);
void			sb(t_stack_node **b, bool print);
void			sa(t_stack_node **a, t_stack_node **b, bool print);
void			ra(t_stack_node **a, bool print);
void			rb(t_stack_node **b, bool print);
void			rr(t_stack_node **a, t_stack_node **b, bool print)
void			rra(t_stack_node **a, bool print);
void			rrb(t_stack_node **b, bool print);
void			rrr(t_stack_node **a, t_stack_node **b, bool print);

// Algorithms
void			sort_three(t_stack_node	**a);
void			sort_stacks(t_stack_node **a, t_stack_node **b);

#endif


/*typedef struct s_stack_node
{
	int		nbr;
	int		index;
	int		push_cost;
	bool	middle_line;
	bool	lowest_move;

	struct s_stack_node *front;
	struct s_stack_node *back;
	
}*/
