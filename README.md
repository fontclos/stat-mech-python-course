[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fontclos/stat-mech-python-course/master?urlpath=lab)

# Introduction to Statistical Mechanics in Python 3
Introduction to Statistical Mechanics in python 3.x, using jupyter notebooks.
This repository is part of the University of Milano course *Introduzione alla Fisica Statistica*. 

We will go through the notebooks of each seassion together. Each notebook explores a different topic and proposes some **exercises for you to do**. There will be some time for you to try the exercises, and we will solve some of them together. You are expected then to solve the rest of exercises on your own. 

Please send your solutions **no later than the indicated date** to *francesc.font@unimi.it*. Also, please rename the `.ipynb` file and add your name to it, e.g.: *1.1-Generating-Random-Numbers-**Mario-Rossi**.ipynb*. 

| Session | Deadline |
|---------|-----------|
| session-1-intro-probability | 2019-04-28, 23:59h |

## Updating your local copy of the repository
New material be added to the repository during the semester. To update your local copy of the repository and get the new material, run 

```bash
$ cd stat-mech-python-course
$ git pull
```
Remember to **rename the notebooks** you are working on to avoid content being overwritten.

## Getting started
Open a terminal and `cd` to a directory of your choice
```bash
$ cd Documents
```
If you are using a desktop computer at *Laboratorio Calcolo*, you need to activate the anaconda python installation
```bash
$ module load python3/anaconda
```
If you are using your laptop, check that you have correctly installed Anaconda's python. 
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
A browser window/tab pointing to `localhost:8888` will open automatically. Open the `session-1-intro-probability` folder, then open the first notebook by double-clicking `1.1-Generating-Random-Numbers.ipynb`. You are ready to go!


## Installing jupyter in your computer
If you want to try this at home, you need a modern installation of `python`, together with `jupyter`, `numpy`, `matplotlib` and some other standard python libraries. The simplest way to install all this without interfeering with your current python installation is the [Anaconda distribution](https://www.anaconda.com/download/). Choose **python 3.x** and your OS, download, install, and you should be good to go. 

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
  
## Contact
You can reach me at `francesc.font@unimi.it` if you need any help, or pass by my office DC/T/6 (right behind Aula Caldirola). Since I am not always in my office, it is better if you make an appointment beforehand.


