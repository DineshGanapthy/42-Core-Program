/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 15:42:12 by dganapat          #+#    #+#             */
/*   Updated: 2026/02/19 13:42:53 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#include <stdlib.h>
#include <limits.h>
#include <stdint.h>


size_t	ft_strlen(const char *str)
{
	size_t		len;

	len = 0;
	while (str[len] != '\0')
	{
		len++;
	}
	return (len);
}

char	*ft_strchr(const char *s, int c)
{
	int	i;

	i = 0;
	while (s[i] != '\0' )
	{
		if (s[i] == (unsigned char)(c))
			return ((char *)(s + i));
		i++;
	}
	if (s[i] == (unsigned char)(c))
		return ((char *)(s + i));
	return (NULL);
}

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*new_string;
	size_t	string_len;
	int	strlen_s1;
    int	i;

	if (!s1 || !s2)
		return (NULL);
	//if (!s1)
	//	return (ft_strdup(s2));
	//if (!s2)
	//	return (ft_strdup(s1));
	strlen_s1 = ft_strlen(s1);
	string_len = strlen_s1 + ft_strlen(s2) + 1;
	new_string = malloc(sizeof(char) * (string_len));
	if (!new_string)
		return (NULL);
    i = 0;
	while(s1[i])
    {
        new_string[i] = s1[i];
		i++;
    }
	i = 0;
	while(s2[i])
	{
		new_string[strlen_s1 + i] = s2[i];
		i++;
	}

	new_string[string_len] = '\0';
    
    //ft_strlcpy(new_string, s1, string_len);
	//ft_strlcat(new_string, s2, string_len);
	return (new_string);
}

void	*ft_memset(void *s, int c, size_t n)
{
	unsigned char	*s2;

	s2 = (unsigned char *)s;
	while (n > 0)
	{
		*s2 = (unsigned char)c;
		s2++;
		n--;
	}
	return (s);
}

void	*ft_calloc(size_t count, size_t size)
{
	unsigned char		*new_string;
	size_t				total_size;

	if (count == '\0' || size == '\0')
		return (malloc(0));
	total_size = count * size;
	//if (size != 0 && count > SIZE_MAX / size)
	//	return (NULL);
	if ((total_size > 2147483647) || (total_size / size != count))
		return (NULL);
	new_string = malloc(total_size);
	if (new_string == NULL)
		return (NULL);
	ft_memset(new_string, 0, total_size);
	return (new_string);
}

/*void	ft_memset(void *s, int c, size_t n)
{
	unsigned char	*s2;

	s2 = (unsigned char *)s;
	while (n > 0)
	{
		s2[i] = '\0';
		i++;
	}
}*/