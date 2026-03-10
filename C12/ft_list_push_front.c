/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_push_front.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 17:03:17 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/10 18:19:48 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include "ft_list.h"

// Inserting a new element at the beginning o fthe linked list
void	ft_list_push_front(t_list **begin_list, void *data)
{
	t_list	*node;

	// if the list is not empty, it creates a new element and places it at the beginning.
	if (*begin_list)
		{
			node = ft_create_elem(data);
			node->next = *begin_list;
			*begin_list = node;
		}
	// If the list is empty we create a new element and assign it as the start of the list.
	else
		*begin_list = ft_create_elem(data);

}

// Prints the elements in a linked list
void	print_list(t_list *list)
{
	t_list * current = list;

	while (current != NULL)
	{
		printf("Value : %d\n" , *(int *)current->data);
		current = current->next;
	}
}

int 	main()
{
	// creating the linked list and giving it memory allocation. 
	t_list *linked_list;
	linked_list = (t_list *)malloc(sizeof(t_list));
	
	//if (!linked_list)
	//	return (NULL);
	
	// declaration of values
	int a = 1;
	int b = 2;
	int c = 3;
	int d = 0;

	// Decalaring and assiging pointers
	void *p1 = &a;
	void *p2 = &b;
	void *p3 = &c;
	void *p4 = &d;

	// adding elements to the linked list
	linked_list = ft_create_elem(p1);
	linked_list->next = ft_create_elem(p2);
	linked_list->next->next = ft_create_elem(p3);

	printf("linked list before :\n");
	print_list(linked_list);

	// Inserting the new element
	ft_list_push_front(&linked_list, p4);

	printf("linked kist after :\n");
	print_list(linked_list);

	// freeing the memory allocated.
	free(linked_list);
}