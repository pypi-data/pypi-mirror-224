#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <tempdata.h>


/* =================================================================================================
 * Get version
 **/

static PyObject *
version(PyObject *self, PyObject *args)
{
    PyObject *obj = NULL;

    if (!PyArg_ParseTuple (args, "O", &obj))
        return NULL;

    PyObject_Print(obj, stdout, Py_PRINT_RAW);
    printf("\n");
    printf("%s", PyUnicode_AsUTF8(obj));
    char *string = "this";
    printf("length is: %d\n", (int)strlen(string));
    PyErr_SetString(PyExc_KeyError, string);

    return NULL;
}


/* =================================================================================================
 * Define type TempData.
 **/

static PyMethodDef methods_tempdata[] = {
    {"iset", (PyCFunction) iset, METH_VARARGS, "Set int value to database."},
    {"iget", (PyCFunction) iget, METH_VARARGS, "Get int value from database."},
    {"status",  (PyCFunction) db_status, METH_NOARGS, "Get status of database."},
    {"int_add", (PyCFunction) db_int_add, METH_VARARGS, ""},
    {NULL},
};

static PyTypeObject type_tempdata = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "TempData",
    .tp_doc = PyDoc_STR("Temporary data."),
    .tp_basicsize = sizeof(database),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_new = db_create,
    .tp_init = (initproc) db_init,
    .tp_methods = methods_tempdata,
    .tp_dealloc = (destructor)db_delete,
};

/* =================================================================================================
 * Define module.
 **/

static PyMethodDef methods_module[] = {
    {"version", version, METH_VARARGS, "Get version."},
    {NULL},
};

static PyModuleDef module_tempdata = {
    PyModuleDef_HEAD_INIT,
    .m_name    = "tempdata",
    .m_doc     = "Package of organize temporary data.",
    .m_size    = -1,
    .m_methods = methods_module,
};

PyMODINIT_FUNC PyInit_tempdata(void)
{
    PyObject *m;

    if (PyType_Ready(&type_tempdata) < 0)
        return NULL;

    m = PyModule_Create(&module_tempdata);

    if (m == NULL)
        return NULL;

    Py_INCREF(&type_tempdata);
    if (PyModule_AddObject(m, "TempData", (PyObject *) &type_tempdata) < 0) {
        Py_DECREF(&type_tempdata);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
