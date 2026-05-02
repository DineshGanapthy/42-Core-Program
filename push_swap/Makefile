# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 14:26:54 by dganapat          #+#    #+#              #
#    Updated: 2026/04/07 12:09:34 by dganapat         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Standard
NAME				= push_swap

# Compiler and Cflags
CC					= cc
CFLAGS				= -Wall -Werror -Wextra
RM					= rm -f

# Source Files
SRC =	push.c \
		rotate.c \
		rev_rotate.c \
		swap.c \
		sort_three.c \
		sort_stacks.c \
		handle_errors.c \
		init_a_to_b.c \
		init_b_to_a.c \
		push_swap.c \
		split.c \
		stack_init.c \
		extra_utils.c \
		stack_utils.c  


OBJS = $(SRC:.c=.o)

all:	$(NAME)

%.o:	%.c
	$(CC) $(CFLAGS) -c $< -o $@

$(NAME):	$(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)


clean:
	rm -f $(OBJS) 

fclean: clean
	rm -f $(NAME)

re: clean all

.PHONY: all clean fclean



					  
