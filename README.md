[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fontclos/stat-mech-python-course/master?urlpath=lab)

# Introduction to Statistical Mechanics in Python 3

> :warning:  This is a legacy version of the repository, **no longer updated since Sept 2021**. If you are taking the *Intropduzione alla Fisica Statistica* course at the University of Milano during the 2021-2022 academic year or beyond, please [use the official repository with the latest updates](https://github.com/SZapperi/stat-mech-python-course).

Introduction to Statistical Mechanics in python 3.x, using jupyter notebooks.

## Installing jupyter on your computer
To follow these lectures, you need a modern installation of `python`, together with `jupyter`, `numpy`, `matplotlib` and some other standard python libraries. The simplest way to install all these packages without interfeering with your current python installation is the [Anaconda distribution](https://www.anaconda.com/download/). Choose **python 3.x** and your OS, download, install, and you should be good to go. 

## Using an online environment
Alternatively, if you cannot install `jupyter` on your computer, you can use the `mybinder` online environment, which is basically an online version of the repository. Notice that the code will not run on your computer, and that you will loose your work if you close the browser window. To launch the mybinder page for the course, click here!

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fontclos/stat-mech-python-course/master?urlpath=lab)

After completing a notebook, **remember to download it** to your local computer!


## Getting started
> These instructions should work for linux & mac users. Windows users might not be able to execute the `which` command, and might need to install the `git` command beforehand. In case of technical difficulties, please use the [binder online environment](https://mybinder.org/v2/gh/fontclos/stat-mech-python-course/master?urlpath=lab).

Open a terminal and `cd` to a directory of your choice
```bash
$ cd Documents
```
Check that you have correctly installed Anaconda's python. 
```bash
$ which python
/home/username/anaconda3/bin/python
```
Clone this repository
```bash
$ git clone https://github.com/fontclos/stat-mech-python-course.git
```
A new folder called `stat-mech-python-course` will be created. Enter it and start jupyter by typing `jupyter lab`
```bash
$ cd stat-mech-python-course
$ jupyter lab
```
A browser window/tab pointing to `localhost:8888` will open automatically. Open the `notebooks` folder, then open the first notebook by double-clicking `1-Generating-Random-Numbers.ipynb`. You are ready to go!


## Searching for help online
Being able to **re-use someone else's code** is as important as being able to write your own. You are *not* supposed to figure out everything by yourself, so googling *how to X in python* is just fine. In addition, some useful resources are:

+ Ask questions
  + [Stackoverflow](https://stackoverflow.com/)

+ Official documentation sites
  + [Numpy documentation](https://docs.scipy.org/doc/numpy/reference/routines.html)
  + [Scipy documentation](https://docs.scipy.org/doc/scipy/reference/)
  + [Jupyter Lab documentation](https://jupyterlab.readthedocs.io/en/stable/)

+ Tutorials
  + [Data Flair Python Tutorials](https://data-flair.training/blogs/python-tutorials-home/)
  + [Numpy Crash Course](https://cs231n.github.io/python-numpy-tutorial/)
  
+ Windows users
  + [Pre-compiled binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/)


