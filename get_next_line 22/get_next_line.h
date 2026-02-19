/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 15:49:45 by dganapat          #+#    #+#             */
/*   Updated: 2026/02/19 13:53:04 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

#ifndef BUFFER_SIZE
# define BUFFER_SIZE 1024
# endif

# include <stdlib.h>
# include <unistd.h>

char	*ft_read_file(int fd, char *holder, int *bytes_read);
char	*ft_complete_line(char *holder);
char	*ft_balance(char *holder);

size_t	ft_strlen(const char *str);
char	*ft_strchr(const char *s, int c);
char	*ft_strjoin(char const *s1, char const *s2);
void	ft_memset(void *s, int c, size_t n);
void	*ft_calloc(size_t count, size_t size);

char *get_next_line(int fd);

#endif
