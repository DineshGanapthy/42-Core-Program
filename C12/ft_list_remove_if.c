/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_remove_if.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 19:18:55 by dganapat          #+#    #+#             */
/*   Updated: 2026/03/10 20:04:51 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)(), void (*free_fct)(void *))
{
	t_list	*list_ptr = begin_list
	t_list	*prev = NULL;

	while (list_ptr)
	{
		// Check if the curren telement needs to be removed
		if ((*cmp)(list_ptr->data, data_ref) == 0)
		{
			//check if the lelment that needs to be removed is first on the list
			if(!prev)
				//Updates the start of teh list
				*begin_list = list_ptr->next;
			else
			// Updates the "Next" pointer of the previous element
				prev->next = list_ptr->next;

			// Cleans and releases the content of the current element
			(*free_fct)(list_ptr->data);
			free(list_ptr);

			//Finish the while
			list_ptr = NULL;
		}
		else
		{
		// "prev" now points to the current element 
		prev = list_ptr;
		
		// "list_ptr" points to the next element  
		list_ptr = list_ptr->next;
		}
	}
}