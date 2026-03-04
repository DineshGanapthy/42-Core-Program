/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Re-CreateC07.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 17:06:19 by dganapat          #+#    #+#             */
/*   Updated: 2026/01/26 16:52:25 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int		ft_strlen(char	*str)
{
	int		len;

	len = 0;
	while (str[len])
		len++;
	return (len);
}
char	*ft_strcpy(char *src, char *dst)
{
	//int		i;
	while (*src)
	{
		*dst = *src;
		src++;
		dst++;
	}

	*dst = '\0';
	return (dst);
}

char	*ft_strdup(char	*str)
{
	int	str_len;
	char	*new_string;

	str_len = ft_strlen(str) + 1;
	new_string = malloc(str_len * sizeof(char));

	if (new_string == NULL)
		return (NULL);
	ft_strcpy(str, new_string);
	return (new_string);
}


#include <stdio.h>
#include <string.h>

int		main()
{
	char	*s1;
	//char	*s2;
	
	s1 = "Hello World";

	printf("Orginal : %s\n" , strdup(s1));
	printf("My Function : %s\n" , ft_strdup(s1));
	//free(new_string);

	return (0);
}