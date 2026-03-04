/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 16:03:16 by dganapat          #+#    #+#             */
/*   Updated: 2026/02/11 19:08:20 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>

int	main()
{
	int	i;
	int	fd;
	char	*line;

	fd = open("thecococlock.txt", O_RDONLY);

	i = 0;
	while (i < 7)
	{
		line = get_next_line(fd);
		printf("line%d : %s" , i ,line);
		free(line);
		i++;
	}
	close(fd);
	return (0);
}