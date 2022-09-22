#include <stdio.h>
#include <Python.h>
#include <string.h>

/**
 * print_python_string - prints some basic info about python string
 * @p: object of python
 *
 * Return: None
 */
void print_python_string(PyObject *p)
{
	ssize_t len;
	wchar_t *str;

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		print(" [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");

	len = PyUnicode_GET_LENGTH(p);

	printf(" length: %ld\n", len);

	str = PyUnicode_AsWideCharString(p, &len);

	printf(" value: %ls\n", str);
}
