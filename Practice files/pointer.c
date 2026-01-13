/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pointer.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/05 16:02:38 by dganapat          #+#    #+#             */
/*   Updated: 2026/01/05 17:31:59 by dganapat         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	ft_ft(int *nbr)
{
	*nbr = 42;
}
void	ft_ultimate(int	***nbr)
{
	***nbr = 43;
}
 void ft_swap(int *a, int *b)
 {
	int holder;

	holder = *a;
	*a = *b;
	*b = holder;
 }
 
/*int		main()
{
	int	a;
	int	b;
	
	a = 25;
	b = 55;

	ft_swap(&a, &b);
	printf("a = %d\n b = %d\n" , a , b);
}*/

int		main(int argc,char **argv)
{
	int	a = argc;
	int i;

	i = 1;

	while (i < a)
	{
		printf("%s\n" , argv[i]);
		i++;
	}
	return (0);
}

/*int		main()
{
	int	var;
	var = 55;

	int	*a = &var;
	int	**b = &a;
	int	***c = &b;

	ft_ultimate(c);
	printf("New Number : %d\n" , var);
}*/
