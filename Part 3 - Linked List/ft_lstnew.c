/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/12 16:01:53 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/12 16:08:56 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstnew(void	*content)
{
	t_list	*elem;

	elem = malloc(sizeof(t_list));
	if (elem)
		return (NULL);
	
	elem->content = content;
	elem->next = NULL;

	return (elem);
}
