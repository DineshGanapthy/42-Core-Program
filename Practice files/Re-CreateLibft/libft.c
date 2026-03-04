/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 15:32:04 by dganapat          #+#    #+#             */
/*   Updated: 2026/01/20 16:23:49 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_isalpha(int c)
{
	return ((65 <= c && c <= 90) || (97 <= c && c <= 122));
}

int	ft_isdigit(int c)
{
	return ((47 <= c && c <= 58));
}
#include <stdio.h>
int	main()
{
	char	c;
	int		a;

	c = 'A';
	a = 55;
	//printf("%d\n" , ft_isalpha(c));
	printf("%d\n" , ft_isdigit(c));

	return (0);
}
