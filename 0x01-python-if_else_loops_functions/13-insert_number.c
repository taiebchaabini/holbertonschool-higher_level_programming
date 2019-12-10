#include "lists.h"
/**
 * findPos - find the position of the hval / lowval
 * @hval: Highest value of head->n
 * @lowval: Lowest value of head->n
 * Return: return the current position
 **/
int findPos(int hval, int lowval)
{
	int max = 0, low = 0, pos = 0;

	while (max < hval || max < lowval)
		max++;

	low = hval > lowval ? lowval : hval;
	max = hval < lowval ? lowval : hval;
	while (pos <= low && pos < max)
		pos++;
	return (pos);
}
/**
 * insert_node - function in C that inserts a number into
 * a sorted singly linked list.
 * @head:  pointer to pointer of first node of listint_t list
 * @number: number to insert into the sorted linked list
 * Return: Updated list with the new sorted linked list
**/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *count, *current, *new;
	int lowval = 0, highval = 0, i = 0, pos = 0;

	count = *head;
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	while (count)
	{
		if (count->n > number)
			highval++;
		if (count->n < number)
			lowval++;
		count = count->next;
	}
	pos = findPos(highval, lowval);
	while (current)
	{
		if (i == pos)
		{
			new->next = current->next;
			current->next = new;
		}
		i++;
		current = current->next;
	}
	return (current);
}
