/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   C07_ft_ultimare_range.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/26 17:44:37 by dganapat          #+#    #+#             */
/*   Updated: 2026/01/26 18:03:05 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int		ft_ultimate_range(int **range, int min, int max)
{
	int len;
	int lenofrange;
	int i;
	//int j;

	lenofrange = (max - min);
	len = lenofrange + 1;
	i = 0;

	*range = malloc(len * sizeof(int));

	if (min >= max)
	{
		*range = NULL;
		return (0);
	}
	while (min < max)
	{
		*range[i] = min;
		min++;
		i++;
	}
	
	return (lenofrange);
}
#include <stdio.h>
//#include <string.h>

int		main()
{
	int min;
	int max;
	int *range;

	min = 1;
	max = 10;	
	printf("%d\n," , ft_ultimate_range(&range,min,max));

	return (0);
}