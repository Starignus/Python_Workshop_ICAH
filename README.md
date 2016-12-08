# Introduction to Python

To download the material of the workshop to your computer just execute the following command line in the bash terminal ( you must be in the path where you want to save the folder in your computer):

```bash
cd /name/of/folder/where/to/save/
git clone https://github.com/Starignus/Python_Workshop_ICAH.git
```
or just download it from [here](https://github.com/Starignus/Python_Workshop_ICAH/archive/master.zip).

## Lessons

* [Introduction](Lessons/Introduction.ipynb)
* [Getting Start with Python](Lessons/Getting_Started_With_Python.ipynb)
  * [Python Object and Data Structure Basics](Lessons/Getting_Started_With_Python.ipynb)
* [Python Statements](Lessons/Python_Statements.ipynb)
* [Functions](Lessons/Functions.ipynb)
* [Scripting](Lessons/Script.ipynb)
* [Numerical Python (NumPy)](Lessons/Numpy.ipynb)
*  [Matplotlib](Lessons/Matplotlib.ipynb)
*  Pandas

Optional:
* [Object Oriented Programming](Lessons/Object_Oriented_Programming.ipynb)

# Required preparations

For this workshop, the participants are encouraged to use their computers to ensure the proper setup of tools required for an efficient workflow. The lessons assume no previous knowledge of the tools or skills, but working through the workshop requires to have a copy of the code on your computer. Please, make sure to install all the software needed before working through the lessons.

### Setting Up Python

We recommend installing [Anacoda](https://www.continuum.io/downloads) distribution of [Python](http://python.org/), which is an all-in-one installer. Individually installing all of its scientific packages can be slow and arduous.

Regardless of how you choose to install it, please make sure you install Python version 2.x (e.g., 2.7.12 is fine).

During the lessons, we will be using the [Jupyter Notebook](http://jupyter.org/), a programming environment that runs in a web browser. Therefore, we will need a reasonably up-to-date browser. The current versions of the Chrome, Safari and Firefox browsers are all [supported](http://ipython.org/ipython-doc/2/install/install.html#browser-compatibility) (some older browsers, including Internet Explorer version 9 and below, are not).

#### Windows

1. Open the  [Anaconda](http://continuum.io/downloads) download website.
2. Download the default Python 2.x installer (If you are not use to the command line commands download the graphical installer).
3. Use all of the defaults for installation __except__ make sure to check **Make Anaconda the default Python.**


#### Mac OS X

1. Open the  [Anaconda](http://continuum.io/downloads) download website.
2. Download the default Python 2.x installer (If you are not use to the command line commands download the graphical installer).
3. Use all of the defaults for installation.

#### Linux

1. Open the  [Anaconda](http://continuum.io/downloads) download website.
2. Download the default Python 2.x installer, save it in your home folder.
3. Install Python 2.x using all of the defaults for installation. (Installation requires using the shell. If you aren't comfortable doing the installation yourself stop here and request help.)
4. Open a terminal window.
5. Type
``` bash
bash Anaconda-
```
and then press tab. The name of the file you just downloaded should appear.
6. Press enter. You will follow the text-only prompts. When there is a colon at the bottom of the screen press the down arrow to move down through the text. Type ``yes`` and press enter to approve the license. Press enter to approve the default location for the files. Type ``yes`` and press enter to prepend Anaconda to your PATH (this makes the Anaconda distribution the default Python).

#### Checking our installation is working.

To make sure Anaconda installation was successful, you can download the script [check_python_installation.py](https://github.com/Starignus/Python_Workshop_ICAH/blob/master/check_python_installation.py) that will check if Anaconda has been correctly installed on your system. From your terminal, navigate to the directory where you downloaded the script and execute the following:
```bash
python check_python_installation.py
```
If you receive an AssertionError, it will inform you how to correct your installation. Otherwise, it will tell you that your system is good to go and ready for you.

__Note:__ In case you are unfamiliar with bash commands you can practise in a [command line interface](https://learncodethehardway.org/unix/) or use this [cheatsheet](https://gist.github.com/LeCoupa/122b12050f5fb267e75f).

### Jupyter Notebook

The Jupyter Notebook is a web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text.

In case you Jupyter is not by default installed, you should have got a message telling you so when running the ``check_python_installation.py``. If that is the case, you have to install it.

In **Linux and Mac** open a terminal and type:
```bash
conda update jupyter
```   
then enter.

In **Windows**:

1. Go to the _Start Menu_ and type in: _anaconda command prompt_ and click or enter in the option.
2. A terminal shell looking interface will pop out.
3. Follow the same steps as above for Linux and Mac.


#### Running the Notebook

Start the notebook server from the command line:

```bash
jupyter notebook
```
__Note:__ For Windows open the _anaconda command prompt_ window and type in the command of above.

This will print some information about the notebook server in your terminal, including the URL of the web application (by default, http://localhost:8888).

```bash
$ jupyter notebook
[I 08:58:24.417 NotebookApp] Serving notebooks from local directory: /Users/catherine
[I 08:58:24.417 NotebookApp] 0 active kernels
[I 08:58:24.417 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
[I 08:58:24.417 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

You should see the notebook open in your browser to this URL:

<img src="tryjupyter_file.png" alt="jupyter" style="width: 400px;"/>

When the notebook opens in your browser, you will see the Notebook Dashboard, which will show a list of the notebooks, files, and subdirectories in the directory where the notebook server was started. Most of the time, you will wish to start a notebook server in the highest level directory containing notebooks. Often this will be your home directory.

You have done your preparations for the course, see you in the workshop.

Reference [[1](https://jupyter.readthedocs.io/en/latest/running.html#running)]
