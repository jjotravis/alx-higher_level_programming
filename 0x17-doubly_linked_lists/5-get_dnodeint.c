#include "lists.h"

/**
 * get_dnodeint_at_index - returns nth node of a linked list
 * @head: Pointer to head of list
 * @index: nth position to be found
 *
 * Return: nth node of the list
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int finder;
	dlistint_t *temp;

	finder = 0;
	temp = head;

	if (head == NULL)
		return (NULL);

	while (temp)
	{
		if (finder == index)
			return (temp);
		temp = temp->next;

		finder++;
	}
	return (NULL);
}
