/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/12 16:54:07 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/12 17:03:17 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
		return (NULL);

	while(lst->next)
		lst = lst->next;
	return (last)
}

/*while(lst->next) // If we looped over until we reached the null lst would point to the null every time
				// IF we did it like ft_lstsize. But if we look for the next on the list when we hit the last node
				// it's next point would be pointing to NULL, and we wouldn't enter the while loop again and when we return lst
				// it would the actual last node.
		lst = lst->next;
	return (last)*/