##
## EPITECH PROJECT, 2021
## 308reedpipes
## File description:
## Makefile
##

NAME            =    308reedpipes

RM              =    @rm -f

SOURCES     =    sources/

all: $(NAME)

$(NAME):
	@cp $(SOURCES)main.py $@
	@chmod +x $@

clean:
		$(RM) -r __pycache__
		$(RM) -r $(SOURCES)__pycache__

fclean: clean
		$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
