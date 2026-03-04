/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 16:05:08 by dganapat          #+#    #+#             */
/*   Updated: 2026/02/19 12:53:11 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_read_file(int fd, char *holder, int *bytes_read)
{
	char	*buffer;
	char	*temp_start;

	if (!holder)
		holder = ft_calloc(1, sizeof(char));

	*bytes_read = 1;
	buffer = ft_calloc(BUFFER_SIZE + 1, sizeof(char));

	while (!ft_strchr(holder, '\n') && *bytes_read != 0)
	{
		*bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (*bytes_read == -1)
		{
			free(buffer);
			free(holder);
			return (NULL);
		}

		buffer[*bytes_read] = '\0';
		temp_start = holder;
		holder = ft_strjoin(temp_start, buffer);

		free(temp_start);
	}

	free(buffer);
	return (holder);
}

char	*ft_complete_line(char *holder)
{
	int	i;
	char	*complete_line;

	i = 0;
	if (!holder[i])
		return (NULL);
	while (holder[i] && holder[i] != '\n')
		i++;

	complete_line = ft_calloc(i + 2, sizeof(char)); // Need futher explaination on the +2 why +2 and not + 1? 
													//Yes null terminator from calloc but why 2
		if(!complete_line)
			return (NULL);

	i = 0;
	while (holder[i] != '\n' && holder[i])
	{
		complete_line[i] = holder[i];
		i++;
	}

	if (holder[i] == '\n') // Newline so when it prints on the terminal it prints with a newline
	{
		complete_line[i] = holder[i];
		i++;
	}

	return (complete_line);
}

char	*ft_balance(char *holder)
{
	int	i;
	int	j;
	char	*remainder_of_line;

	i = 0;
	j = 0;
	while (holder[i] != '\n' && holder[i])
		i++;

	if (!holder[i])
	{
		free (holder);
		return (NULL);
	}

	remainder_of_line = calloc(ft_strlen(holder) - i + 1, sizeof(char));

	if (!remainder_of_line[i])
		return (NULL);

	i++; // To pass the newline character. 
	while (holder[i])
	{
		remainder_of_line[j] = holder[i];
		i++;
		j++;
	}
	free (holder);
	return (remainder_of_line);
}






char *get_next_line(int fd)
{
	char	*new_line;
	static char	*holder;
	int		bytes_read;

	if (fd < 0 || BUFFER_SIZE <= 0 || (read(fd,0,0) < 0))
		return (NULL);

// This will read the  file in the byes stated by the read fuction including the /n newlines and 
//store it in a string called holder. 
holder = ft_read_file(fd, holder, &bytes_read);
	if (!holder)
		return (NULL);

// This will take the holder string and seperate it everytime it sees a new line. 
new_line = ft_complete_line(holder);

// This will remove the new_line from the holder and continue where it left off from.
//ft_balance(holder); (slightly modidyfing the code, if it doesn't work change back)
holder = ft_balance(holder);

// Safety
if (new_line == NULL && bytes_read == 0)
{
	free (holder);
	return (NULL);
}

// We return a new line as a string onto the terminal.
return (new_line);

}

/*holder = ft_calloc (BUFFER_SIZE + 1, sizeof(char));
	if (!holder)
		return (NULL);

	bytes_read = read(fd, holder, BUFFER_SIZE);

	
	
char	*ft_balance(char *holder, new_line)
{
	int	i;
	int	char_to_skip;

	char_to_skip = ft_strlen(new_line);

	i = 0;
	while (holder[i] != '\n' && i != char_to_skip)
	{
		holder++;
		i++;
	}
	return (holder);

	char *remainder;
	ft_stardup(holder, remainder);
	free (holder);
	return (remainder);
}
*/

