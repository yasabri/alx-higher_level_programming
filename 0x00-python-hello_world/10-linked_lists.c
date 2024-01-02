#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to the head of list
 * Return: nods number
 */
size_t print_listint(const listint_t *h)
{
  const listint_t *current;
  unsigned int x;

  current = h;
  x = 0;
  while (current != NULL)
    {
      printf("%i\x", current->x);
      current = current->next;
      x++;
    }

  return (x);
}

/**
 * add_nodeint - inserts a fresh node at the start of a listint_t list
 * @n: integer to be included in node
 * @head: pointer to a pointer of start, list
 * Return: the address of new element , NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
  listint_t *new;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);

  new->n = n;
  new->next = *head;
  *head = new;

  return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: the pointer to the list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
  listint_t *current;

  while (head != NULL)
    {
      current = head;
      head = head->next;
      free(current);
    }
}
