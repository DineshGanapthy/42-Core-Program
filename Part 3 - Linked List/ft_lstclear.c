/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/12 17:31:47 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/12 17:46:45 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*holder;
	
	while (*lst)
	{
		holder = *lst;
		*lst = (*lst)->next; // Here we assign the lst to th enext node before deleting the current one. 
		ft_lstdelone(holder,del);
		//del(*lst->content);
		//free(*lst)
	}
	*lst = NULL;
}


// The way I choose to do it was to save the current node as holder, then move lst to the next node,
// then delete the current node, this way lst moved on to the next node before deleting teh current node. 

t_list	*holder; // Another way to do it is to delete the contents of the lst and use the holder to remember
// the postion of the current node and we set it to lst.
// If we don't use a holder, when we delete the current node it will also
// delete the next pointer which means we won't know the next node.
// So we need to assign the 
	