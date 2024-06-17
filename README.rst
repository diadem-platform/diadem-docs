DiaDEM Documentation
====================

Purpose
-------
This repository contains the public documentation of the DiaDEM platform, including the user manual, scientific documentation (computational methods), documentation of the database, and terms of usage.

The documentation is hosted on Read the Docs: `DiaDEM Documentation <https://diadem.readthedocs.io/en/latest/>`_

Restructured Text (rst)
-----------------------
The documentation is written in reStructuredText. Check out the cheat sheet of reStructuredText: `Cheat Sheet <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_; another available here: `Quick Reference <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_

Local Build (Testing)
---------------------
To locally build the documentation, navigate into the ``docs`` folder and run:

.. code-block:: sh

    make html

Note that you need to have Sphinx installed for this:

.. code-block:: sh

    pip install sphinx
    pip install sphinx-rtd-theme

Commits and Pull Requests (PRs)
-------------------------------
Please work in a separate branch, not in ``main``.

1. Create and checkout a new branch.
2. While you work, commit every releasable increment separately; push every now and then.
3. If you want your changes to go online, log in to the GitHub repository and create a pull request (PR).
4. The admins will review the PR and merge it into ``main``; the changes will then go online automatically.


Conventions
-----------

Images
~~~~~~

Create a folder named after your `.rst` file and place images there.

Example:

```
source/
└── path/
    └── to/
        └── my_file/
            ├── my_name.rst
            └── my_name/
                ├── my_image_1.png
                └── my_image_2.png
```


Files
~~~~~

Place in the `_static` folder, mimicking the path structure of your `.rst` file.

Example:


```
    source/
    ├── _static/
    │   └── path/
    │       └── to/
    │           └── my_file/
    │               └── my_text_file.txt
    └── path/
        └── to/
            └── my_file/
                └── my_name.rst
```