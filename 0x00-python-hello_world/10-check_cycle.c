#include "lists.h"
#include <stdio.h>
/**
* check_cycle - Function that checks if a singly linked list has a cycle in it.
* @list: Take a listint_t as argument
* Return: 1 if have a cycle otherwise 0
**/
int check_cycle(listint_t *list)
{
	int i = 0, tmp = -1;

	if (list == NULL)
		return (0);
	while (list)
	{
		if (tmp == list->n)
			return (1);
		if (i == 0)
			tmp = list->n;
		list = list->next;
		i++;
	}
	return (0);
}
