# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dganapat <dganapat@student.42kl.edu.my>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 14:26:54 by dganapat          #+#    #+#              #
#    Updated: 2026/03/25 16:37:21 by dganapat         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Standard
NAME				= push_swap_1

# Directories
HEADER				= header/
SRC_DIR				= source/
OBJ_DIR				= objects/

# Compiler and Cflags
CC					= cc
CFLAGS				= -Wall -Werror -Wextra -I
RM					= rm -f

# Source Files 
COMMANNDS_DIR		= $(SOURCE_DIR)commands/push.c \
					  $(SOURCE_DIR)commands/rotate.c \
					  $(SOURCE_DIR)commands/rev_rotate.c \
					  $(SOURCE_DIR)commands/swap.c \
					  $(SOURCE_DIR)commands/sort_three.c \
					  $(SOURCE_DIR)commands/sort_stack.c 

PUSH_SWAP_DIR		= $(SOURCE_DIR)push_swap/handle_errors.c \
					  $(SOURCE_DIR)push_swap/init_a_to_b.c \
					  $(SOURCE_DIR)push_swap/init_b_to_a.c \
					  $(SOURCE_DIR)push_swap/push_swap.c \
					  $(SOURCE_DIR)push_swap/split.c \
					  $(SOURCE_DIR)push_swap/stack_init.c \
					  $(SOURCE_DIR)push_swap/stack_utils.c  

SRCS 				= $(COMMANNDS_DIR) $(PUSH_SWAP_DIR)

OBJS				= $(patsubsr $(SOURCE_DIR)%.c,$(OBJ_DIR)%.o,$(SRCS))

start:
					@make all
					
all:				$(NAME)

$(NAME):			$(OBJS)
					@$(CC) $(CFLAGS) $(HEADER) $(OBJS) -o $(NAME)

#Complie objects from the source files
$(OBJ_DIR)%.o:		$(SOURCE_DIR)%.c
					@mkdir -p $(@D)
					@$(CC) $(CFLAGS) $(HEADER) -c $< -o $@

clean:
					@$(RM) -r $(OBJS_DIR)

fclean:				clean
					@$(RM) $(NAME)

re:					fclean all

.PHONEY:			all clean fclean re


					  
