#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - checks if a list has a cycle
 * @list: points to list to be checked
 * Return: 0 if there is no cycle else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL)
		return (1);

	temp = list->next;
	while (temp != NULL && temp != list)
	{
		temp = temp->next;
	}
	if (temp == list)
		return (1);
	else
		return (0);
}
