#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * Return: 0 if no cycle, 1 is yes
 */
int check_cycle(listint_t *list)
{
	listint_t *step = list;
	listint_t *jump_step = list;

	if (!list)
		return (0);

	while (1)
	{
		/* visit successive nodes in linked list */
		if (jump_step->next != NULL && jump_step->next->next != NULL)
		{
			jump_step = jump_step->next->next;
			step = step->next;

			if (jump_step == step) /* cycle found */
				return (1);
		}
		else
			return (0);
	}
}
