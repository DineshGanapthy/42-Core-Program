/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 16:05:08 by dganapat          #+#    #+#             */
/*   Updated: 2026/01/31 12:22:41 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char *get_next_line(int fd)
{
	char	*holder;
	int		bytes_read;

	if (fd < 0 || BUFFER_SIZE < = 0 || read(fd,0,0) < 0)
		return (NULL);

	holder = ft_calloc (BUFFER_SIZE + 1, sizeof(char));
	if (!holder)
		return (NULL);

	bytes_read = read(fd, holder, BUFFER_SIZE);
	
}