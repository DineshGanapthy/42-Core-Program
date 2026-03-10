/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_create_elem.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:47:53 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/10 17:39:05 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include "ft_list.h"

/*typedef		struct s_list
{
	struct	s_list	*next;
	void	*data;
}			t_list;*/

// We are creating a t_list element which is a type of struture.
t_list	*ft_create_elem(void *data)
{
	t_list	*elem;

	//We do a memory allocation here
	elem = (t_list *)malloc((sizeof(t_list)));
	if (!elem)
		return (NULL);

	// Assigneing values to the sturctures variables
	elem->data = data;
	elem->next = NULL;

	//We return the creates element
	return (elem);
}

/*int		main(void)
{
	int		a;

	a = 42;
	// We are creating the list here
	t_list	*list;

	//We are assigning the list new elements. 
	list = ft_create_elem(&a);

	// We are printing the elements of the list
	printf("Value of elem->data : %d\n" , *(int *)list->data);
	printf("Value of elem->next : %p\n" , (void *)list->next);

	// We are freeing the allocated memory
	free(list);
}*/