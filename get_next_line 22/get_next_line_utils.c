/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 15:42:12 by dganapat          #+#    #+#             */
/*   Updated: 2026/02/11 19:05:28 by dganapat         ###   ########.fr       */
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

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	dstlen;
	size_t	srclen;

	dstlen = ft_strlen(dst);
	srclen = ft_strlen(src);
	if (dstlen > size)
		return (srclen + size);
	dst += dstlen;
	size -= dstlen;
	while (size > 1 && *src != '\0')
	{
		*dst = *src;
		dst++;
		src++;
		size--;
	}
	*dst = '\0';
	return (srclen + dstlen);
}

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	srclen;

	srclen = ft_strlen(src);
	if (size == 0)
		return (srclen);
	while (*src && size - 1)
	{
		*dst = *src;
		dst++;
		src++;
		size--;
	}
	*dst = '\0';
	return (srclen);
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

char	*ft_strdup(const char *s)
{
	char		*new_string;
	size_t		str_len;

	str_len = ft_strlen(s) + 1;
	new_string = malloc(sizeof(char) * str_len);
	if (new_string == NULL)
		return (NULL);
	ft_strlcpy(new_string, s, str_len);
	return ((char *)(new_string));
}

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*new_string;
	size_t	string_len;

	if (!s1 && !s2)
		return (NULL);
	if (!s1)
		return (ft_strdup(s2));
	if (!s2)
		return (ft_strdup(s1));
	string_len = ft_strlen(s1) + ft_strlen(s2) + 1;
	new_string = malloc(sizeof(char) * (string_len));
	if (!new_string)
		return (NULL);
	ft_strlcpy(new_string, s1, string_len);
	ft_strlcat(new_string, s2, string_len);
	return (new_string);
}

void	ft_bzero(void *s, size_t n)
{
	size_t			i;
	unsigned char	*s2;

	i = 0;
	s2 = (unsigned char *)s;
	while (i != n)
	{
		s2[i] = '\0';
		i++;
	}
}

void	*ft_calloc(size_t count, size_t size)
{
	unsigned char		*new_string;
	size_t				total_size;

	total_size = count * size;
	if (size != 0 && count > SIZE_MAX / size)
		return (NULL);
	new_string = malloc(total_size);
	if (!new_string)
		return (NULL);
	ft_bzero(new_string, total_size);
	return (new_string);
}