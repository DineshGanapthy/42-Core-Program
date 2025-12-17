/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 14:41:55 by dganapat          #+#    #+#             */
/*   Updated: 2025/11/02 14:15:17 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char* str)
{
	int	i;
	int	sign;
	long	result;

	i = 0;
	sign = 1;
	result = 0;
	while ((str[i] >= 9 && str[i] <= 13)|| str[i] == ' ')
			i++;
		if (str[i] == '-' || (str[i] == '+'))
		{
			if (str[i] == '-')
				sign = sign * -1;
			i++;
		}
	while (str[i] >= 47 && str[i] <= 58)
	{
		result = (result * 10) + (str[i] - '0');
		i++;
	}
	return (int)(sign *result);
}	
/*int         main()
{
	const char *s1 = "			-2436457654";
	
	printf("New s1 : %d\n" , ft_atoi(s1) );
	printf("New s1 : %d\n" , atoi(s1) );

	return (0);
}*/
