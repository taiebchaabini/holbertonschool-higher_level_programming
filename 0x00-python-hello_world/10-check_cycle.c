#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - Function that checks if a singly linked list has a cycle in it
 * @list: Take a listint_t as argument
 * Return: 1 if have a cycle otherwise 0
 **/
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *tmp = NULL;

	if (list == NULL || list->next == NULL)
		return (0);
	while (list != NULL)
	{
		if (i == 0)
			tmp = list;
		if (tmp->n == list->n && tmp->next == list->next && i != 0)
			return (1);
		list = list->next;
		i++;
	}
	return (0);
}
