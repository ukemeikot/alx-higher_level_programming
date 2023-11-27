#include "lists.h"
#include <stdio.h>
/**
  *check_cycle - checcks for the exixtence of a cycle in a linked list.
  *@list: this list to be parsed as arguments.
  *Return: 0 if there is none and 1 if there is a cycle.
  */

int check_cycle(listint_t *list)
{
	listint_t *ahead = list, *behind = list;

	while (behind != NULL && ahead != NULL && ahead->next != NULL)
	{
		behind = behind->next;
		ahead = ahead->next->next;

		if (ahead == behind)
			return (1);
	}
	return (0);
}
