/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 17:37:23 by dganapat          #+#    #+#             */
/*   Updated: 2026/01/28 17:43:04 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_strlen(char *str)
{
	char *start = str;
	char *end;
	while(*str)
	str++;
	end = str;

return (end - start);
}

/*#include <stdio.h>
int	main()
{
	printf("%d\n" , ft_strlen("Hello World"));
	return (0);
}*/