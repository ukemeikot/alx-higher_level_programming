#include "lists.h"
#include <stdio.h>
/**
  *insert_node - to insert a new node
  *@head: pointer to the head of the list
  *@number: where to insert the new list
  *Return: pointer to the node created
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	tmp = *head;
	while (tmp->next != NULL)
	{
		if (number >= tmp->n && number < tmp->next->n)
		{
			new_node->next = tmp->next;
			tmp->next = new_node;
			return (new_node);
		}
		tmp = tmp->next;
	}
	tmp->next = new_node;
	return (new_node);
}
