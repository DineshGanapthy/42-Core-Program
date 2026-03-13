/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/12 17:56:42 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/12 18:19:25 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list *ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*new_list;
	t_list	*new_node;

	new_list = NULL; // Be careful here as the first node of the new list is now NULL ?
					// do we ahve to change this ? Ask Senior cadet. 

	if (!lst)
		return (NULL);

	while (lst)
	{
		new_node = ft_lstnew(f(lst->content));
		if (!new_node)
		{
			ft_lstclear(&new_list,del);
			return (NULL);
		}
		ft_lstadd_back(new_list, new_node);
		lst = lst->next;
	}
	return (new_list);
}
