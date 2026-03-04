/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   GNL.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 16:20:22 by dganapat          #+#    #+#             */
/*   Updated: 2026/01/29 16:24:37 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// open includes found in man 2 open
//
// only flag needed for gnl:
//
////////////////
/// O_RDONLY ///
////////////////
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

// read include found in man 2 read
#include <unistd.h>

// printf include
#include <stdio.h>

// EXIT_SUCCESS include
#include <stdlib.h>
int	get_s_var(int i) {
	static int num = 1;
	num += i + num;
	return num;
}

int	main() {
	// open demo
	char *filename = "dinesh.txt";
	int fd = open(filename, O_RDONLY);

	// read demo
	ssize_t bytes_read;
	int num_bytes = 6;
	char buf[7];
	buf[6] = '\0';

	bytes_read = read(fd, buf, num_bytes);
	printf("open and read demo - dinesh\n");
	printf("%s\n", buf);
	
	// static variable demo
	printf("static var example\n");
    
	get_s_var(1);
    get_s_var(1);
    get_s_var(1);
    get_s_var(1);
    get_s_var(1);
    get_s_var(1);
    
	printf("\n");
	
	// malloc and free demo
	char *str;

	str = malloc(6);
	str[0] = '1';
	str[1] = '2';
	str[2] = '3';
	str[3] = '4';
	str[4] = '5';
	str[5] = '\0';
	printf("%s\n", str);
	free(str);

	return EXIT_SUCCESS;
}
