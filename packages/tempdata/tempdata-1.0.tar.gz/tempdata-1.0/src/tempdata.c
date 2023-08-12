#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <Python.h>
#include <tempdata.h>

#define INIT_TABLE_SIZE 256
#define KEY_LENGTH 100

/** ================================================================================================
 *  Static methods
 */

static size_t
hash(const char *str)
{
    unsigned char *unsigned_str = (unsigned char *) str;
    size_t hash = 5381;
    int c;

    while ((c = *unsigned_str++))
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

    return hash;
}

static node_int *
create_node_int(const char *key, long value)
{
    node_int* node = malloc(sizeof(node_int));
    node->key = calloc(1, strlen(key)+1);
    node->value = value;
    node->next = NULL;
    strcpy(node->key, key);
    return node;
}

static table_int *
create_table_int(size_t size)
{
    table_int* table = malloc(sizeof(table_int));
    table->size  = size;
    table->used  = 0;
    table->nodes = calloc(size, sizeof(node_int *));
    return table;
}

static int
set_int(database* db, const char *key, long value)
{
    /* This is a empty table. */
    if (db->tb_int == NULL) 
        db->tb_int = create_table_int(INIT_TABLE_SIZE);

    node_int **pnode = (node_int **)find_pnode(hash(key), db->tb_int);

    /* This is a empty node. */
    if (*pnode == NULL) {
        *pnode = create_node_int(key, value);
        return 0;
    }

    node_int *prev, *node = *pnode;

    /* Over write existing node value if key exist. */
    while (node != NULL) {
        if (!strcmp(node->key, key)) {
            node->value = value;
            return 0;
        }
        prev = node;
        node = node->next;
    }

    /* Create new node with key. */
    prev->next = create_node_int(key, value);
    return 0;
}


/** ================================================================================================
 *  Wrapper
 */

PyObject *
db_create(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    database* self;
    self = (database *) type->tp_alloc(type, 0);

    if (self != NULL)
        self->tb_int = NULL;

    return (PyObject *) self;
}

int
db_init(database *self, PyObject *args, PyObject *kwds)
{
    return 0;
}

void
db_delete(database *self)
{
    Py_TYPE(self)->tp_free((PyObject *) self);
}

PyObject *
db_status(database *db, PyObject *Py_UNUSED(ignored))
{
    node_int *node;

    printf("----------------------------------------\n");
    printf("Status of TempData(%p):\n", db);
    printf("Table Int:\n");
    for (size_t i = 0; i < db->tb_int->size; i++) {
        node = db->tb_int->nodes[i];

        while (node != NULL) {
            printf("[%zu] (%s): (%ld)\n", i, node->key, node->value);
            node = node->next;
        }
    }
    printf("----------------------------------------\n");

    Py_INCREF(Py_None);
    return Py_None;
}

PyObject *
iset(database *db, PyObject *args)
{
    const char *key;
    long value;

    if (!PyArg_ParseTuple(args, "sl",
                                     &key, &value))
        return NULL;

    if (set_int(db, key, value)) {
        PyErr_SetString(PyExc_ValueError, "Unexpected ERROR occurred!");
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

PyObject *
iget(database *db, PyObject *args)
{
    const char *key;

    if (!PyArg_ParseTuple(args, "s", &key))
        return NULL;

    node_int *node = *find_pnode(hash(key), db->tb_int);

    while (node != NULL) {

        if (!strcmp(node->key, key))
            return PyLong_FromLong(node->value);

        node = node->next;
    }

    PyErr_SetString(PyExc_KeyError, key);
    return NULL;
}

PyObject *
db_int_add(database *db, PyObject *args)
{
    long value;

    if (!PyArg_ParseTuple(args, "l", &value))
        return NULL;

    node_int *node;
    for (size_t i = 0; i < db->tb_int->size; i++) {
        node = db->tb_int->nodes[i];

        while (node != NULL) {
            node->value += value;
            node = node->next;
        }
    }

    Py_INCREF(Py_None);
    return Py_None;
}
