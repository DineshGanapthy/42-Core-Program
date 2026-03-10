/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_foreach.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 18:41:05 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/10 19:13:54 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list.h"
#include <stdio.h>
#include <stdlib.h>

void	ft_list_foreach(t_list *begin_list, void (*f)(void *))
{
	t_list	*list_ptr;
		
	while (begin_list != NULL)
	{
		// This sets our create pointer to point to the data stores on the first node;
		list_ptr = begin_list;

		// This derefrences the structures and specificliit thepointing to the data paramter and applies the efunction to that data.  
		(*f)(list_ptr->data);
		 
		// This set the current begin_list to the next node
		begin_list = begin_list->next;
	}
}

void	ft_mul(void *data)
{
	*(int *)data *= 3;
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
	//int d = 0;

	// Decalaring and assiging pointers
	void *p1 = &a;
	void *p2 = &b;
	void *p3 = &c;
	//void *p4 = &d;

	// adding elements to the linked list
	linked_list = ft_create_elem(p1);
	linked_list->next = ft_create_elem(p2);
	linked_list->next->next = ft_create_elem(p3);

	printf("linked list before :\n");
	print_list(linked_list);
	
	ft_list_foreach(linked_list, &ft_mul);

	//printf("linked list before :\n");
	//print_list(linked_list);

	// Inserting the new element
	//ft_list_push_front(&linked_list, p4);

	printf("linked list after  :\n");
	print_list(linked_list);

	//printf("Number of elements : %d\n" , ft_list_size(linked_list));

	// freeing the memory allocated.
	free(linked_list);
}