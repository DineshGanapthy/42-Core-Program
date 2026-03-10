/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 16:07:34 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/10 16:19:13 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_LIST_H
# define FT_LIST_H

//We create a struct type with the two variables required "Data" and "Next."

typedef		struct	s_list
{
	struct	s_list	*next; // It contains a struct s-list pointer to the next node.
	void			*data; // The pointer to the data it contains.
	
}					t_list; // We the call this stucture t_list. 

t_list	*ft_create_elem(void *data);

#endif