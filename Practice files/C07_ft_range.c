/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   C07_ft_range.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/26 16:53:59 by dganapat          #+#    #+#             */
/*   Updated: 2026/01/26 17:49:44 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int		*ft_range(int min, int max)
{
	int len;
	int *array;
	int i;
	//int j;

	len = (max - min) + 1;
	i = 0;

	array = malloc(len * sizeof(int));

	//if (array == NULL)
	//	return (NULL);
	if (min >= max)
		return (NULL);

	while (min < max)
	{
		array[i] = min;
		min++;
		i++;
	}
	
	return (array);
}
#include <stdio.h>
//#include <string.h>

int		main()
{
	int min;
	int max;
	int i;
	int static range;

	min = 10;
	max = 0;
	i = 0;
	range = max - min;
	
	while (i < range)
	{
		printf("%d ," , ft_range(min,max)[i]);
		i++;
	}
	printf("\n");
	return (0);
}