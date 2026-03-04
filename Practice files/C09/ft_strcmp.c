/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 17:43:21 by dganapat          #+#    #+#             */
/*   Updated: 2026/01/28 17:49:42 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_strcmp(char *s1, char *s2)
{
	while (*s1 && *s2)
		{
			if (*s1 == *s2)
			{
			s1++;
			s2++;
			}
		}
	return (*s2 - *s1);
		
}
#include <stdio.h>
int	main()
{
	printf("%d\n" , ft_strcmp("Hello", "hello"));
	return (0);
}
