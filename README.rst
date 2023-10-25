DiaDEM documentation
=======================================
Purpose 
--------
This respository contains the public documentation of the DiaDEM platform, including user manual, scientific documentation (computational methods), documentation of the database, and terms of usage. 

The documentation is hosted on read the docs: https://diadem.readthedocs.io/en/latest/

Restructured Text (rst)
-----------------------
The documentation is written in restructured Text. Checkout a the cheat sheet of rst: https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst ; another available here: https://docutils.sourceforge.io/docs/user/rst/quickref.html

Local build (testing)
----------------------
To locally build the documentation, cd into the docs folder and run
make html

Note that you need to have sphinx installed for this 
pip install sphinx
pip install sphinx-rtd-theme

Commings and PRs
-------------------
Please work in a separate branch, not in main. 
1. Create and checkout a new branch
2. While you work, best commit every releasable increment separately; push every now and then.
3. If you want your changes to go online, log in to the github repository and create a pull request (PR)
4. The admins will review the PR and merge into main, the changes will then go online automatically
