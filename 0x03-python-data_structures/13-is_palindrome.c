#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: head of list
 *
 * Return: head of reversed list
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	head = prev;

	return (head);
}

/**
 * is_palindrome - determines if a list is a palindrome
 * @head: head of list
 *
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	unsigned int length = 0, half = 0, i = 0;
	listint_t *cursor, *second;

	cursor = *head;
	while (cursor != NULL)
	{
		cursor = cursor->next;
		length++;
	}

	half = length / 2;
	cursor = *head;
	for (i = 0; i < half; i++)
	{
		cursor = cursor->next;
	}
	second = reverse_list(cursor);
	cursor = *head;

	while (second != NULL)
	{
		if (cursor->n != second->n)
			return (0);
		cursor = cursor->next;
		second = second->next;
	}
	return (1);
}
