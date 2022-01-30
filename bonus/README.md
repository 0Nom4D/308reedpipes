# 308reedpipes

308reedpipes is a B-MAT-500 EPITECH module project.

308reedpipes is about helping you cousin with his reed pipe enthusiasm.

## Before continuing...

This project is an EPITECH Project. If you are an EPITECH student, move out the way!

Nothing to see here... I don't want to be involved to your -42.

![Alt Text](https://media.tenor.com/images/5a5f5957db8b98be17ef208737663b9b/tenor.gif)

If you're not, no worries! You're welcome here!

### Prerequisites

To use this project, you'll need Python (Version 3.8) and Pytest for Unit Tests:

* [Python Installation](https://www.python.org/downloads/)
* [Pytest Installation](https://docs.pytest.org/en/6.2.x/getting-started.html#install-pytest)
* [Numpy Installation](https://pypi.org/project/numpy/)
* [Matplotlib Installation](https://pypi.org/project/matplotlib/)
* [Scipy Installation](https://pypi.org/project/scipy/)

### Building program

308reedpipes is a B-MAT-500 EPITECH module project.

308reedpipes is about helping you cousin with his reed pipe enthusiasm.

You can use this program as it follows:

```textmate
$> ./308reedpipes -h
USAGE
        ./308reedpipes r0 r5 r10 r15 r20 n
DESCRIPTION
        r0      radius (in cm) of pipe at the 0cm abscissa
        r5      radius (in cm) of pipe at the 5cm abscissa
        r10     radius (in cm) of pipe at the 10cm abscissa
        r15     radius (in cm) of pipe at the 15cm abscissa
        r20     radius (in cm) of pipe at the 20cm abscissa
        n       number of points needed to display the radius
```

You can also launch unit tests by using the command below at root of the repository:

```textmate
$> coverage run --rcfile=.coveragerc -m --source=sources/ pytest --capture=sys -rA tests/
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/nom4d/EPITECH/307multigrains
collected ... items

...

==================================== PASSES ====================================
_____________________                  ...                ______________________
----------------------------- Captured stdout call -----------------------------
...
=========================== short test summary info ============================
...
============================== ... passed in ...s ===============================
$> coverage report -m
// In order to show coverage report
```

### Bonus

This version of 308reedpipes includes a bonus which creates a graph showing a 2D shape of the constructed reedpipe.

![Alt Text](https://github.com/0Nom4D/308reedpipes/blob/master/bonus/reedpipe_analysis.png)

### Coding Style

308reedpipes is developed with Python. EPITECH doesn't impose any Coding Style to this but I tried to be as cleaner as possible.

## Authors

* **Arthur Adam** - [0Nom4D](https://github.com/0Nom4D)

This README file has been created with mdCreator. [Please check the project by clicking this link.](https://github.com/0Nom4D/mdCreator/)
