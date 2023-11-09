#include "lists.h"

/**
 * sum_dlistint - sums up all data in a list
 * @head: pointer to head of the list
 *
 * Return: Sum
 */
int sum_dlistint(dlistint_t *head)
{
	int sum = 0;

	if (head == NULL)
		sum = 0;

	while (head != NULL)
	{
		sum += head->n;
		head = head->next;
	}
	return (sum);
}

