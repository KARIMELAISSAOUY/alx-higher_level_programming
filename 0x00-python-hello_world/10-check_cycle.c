/*
 * File: 10-check_cycle.c
 * Author : KARIMELAISSAOUY
 */

#include <stdlib.h>
#include "lists.h"

/**
 * Check_Cycle --  Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: true if there is a cycle, false otherwise.
 */
bool check_cycle(const listint_t *list)
{
	const listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return false;

	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return true;

		turtle = turtle->next;
		hare = hare->next->next;
	}

	return false;
}

