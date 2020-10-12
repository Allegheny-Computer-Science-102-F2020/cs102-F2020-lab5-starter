# cs102-F2020-lab5-starter

![](../../workflows/build/badge.svg)

## Table of Contents

* [Objectives](#objectives)
* [Introduction](#introduction)
* [Continuous Learning](#continuous-learning)
* [Assignment Reminders](#assignment-reminders)
* [Accessing the Assignment](#accessing-the-assignment)
* [Laboratory Assignment Tasks](#laboratory-assignment-tasks)
  + [Installing Programs that Support Python Programming](#installing-programs-that-support-python-programming)
  + [Summarizing Real-World Populate Data Using Functions and Iteration Constructs](#summarizing-real-world-populate-data-using-functions-and-iteration-constructs)
  + [Running a Pytest Test Suite to Establish a Confidence in Function Correctness](#running-a-pytest-test-suite-to-establish-a-confidence-in-function-correctness)
  + [Reflecting on the Laboratory Assignment](#reflecting-on-the-laboratory-assignment)
  + [Transferring Your Source code and Technical Writing to GitHub](#transferring-your-source-code-and-technical-writing-to-github)
* [Automated Checks with GatorGrader](#automated-checks-with-gatorgrader)
* [Assignment Assessment](#assignment-assessment)
* [Advance Feedback on an Assignment](#advance-feedback-on-an-assignment)
* [Discussion of a Graded Assignment](#discussion-of-a-graded-assignment)
* [Additional Resources](#additional-resources)
  + [System Commands](#system-commands)
  + [Using Docker](#using-docker)
* [Commands for an Interactive Docker Shell](#commands-for-an-interactive-docker-shell)
* [Upgrading the Docker Container](#upgrading-the-docker-container)
  + [Downloading Project Updates](#downloading-project-updates)
  + [Using GitHub Actions](#using-github-actions)
  + [System Requirements](#system-requirements)
  + [Reporting Problems](#reporting-problems)
  + [Receiving Assistance](#receiving-assistance)

**Due: October 19, 2020 at 2:30 pm**

## Objectives

The learning objectives for this laboratory assignment are as follows:

- To configure Git and GitHub on your laptop and on the GitHub servers
- To transfer files from your laptop to your GitHub repository
- To use a Docker container to run the automated checks performed by GatorGrader
- To install the programs that you need to support the creation of a Python program
- To use a terminal window to run a Python program and observe its output
- To use conditional logic to avoid an incorrect division by zero
- To use iteration constructs and functions to transform the type of data
- To calculate the mean and median of a sequence of floating-point numbers
- To calculate the variance and standard deviation of a sequence of floating-point numbers
- To combine the use of iteration, conditional logic, and lists of floating-point numbers in a Python program
- To apply data summarization techniques to the characterization of a real-world data set
- To use your text editor and a terminal window to run a test suite for a Python program

## Introduction

Designed for use with [GitHub Classroom](https://classroom.github.com/) and
[GatorGrader](https://github.com/GatorEducator/gatorgrader/), this repository
contains a laboratory assignment for an introductory computer science class
that uses the Python programming language. The source code and technical
writing for this assignment must pass tests set by the [GatorGrader
tool](https://github.com/GatorEducator/gatorgrader). When you use the `git
commit` and `git push` commands to transfer your source code to your GitHub
repository, GitHub Actions will initialize a build of your assignment, checking
to see if it meets all of the requirements. If both your source code and
writing meet all of the established requirements, then you will see a green ✔
in the listing of commits in GitHub. If your submission does not meet the
requirements, a red ❌ will appear instead. Please note that, at the option of
the course instructor, some checks may be run in GitHub Actions that are not
run locally by the [GatorGrader
tool](https://github.com/GatorEducator/gatorgrader).

## Continuous Learning

If you have not done so already, please read all of the relevant [GitHub
Guides](https://guides.github.com/) that explain how to use many of the features
that GitHub provides. In particular, please make sure that you have read the
following GitHub guides: [Mastering
Markdown](https://guides.github.com/features/mastering-markdown/), [Hello
World](https://guides.github.com/activities/hello-world/), and [Documenting Your
Projects on GitHub](https://guides.github.com/features/wikis/). Each of these
guides will help you to understand how to use both [GitHub](http://github.com) and
[GitHub Classroom](https://classroom.github.com/).

Students who want to learn more about how to use
[Docker](https://www.docker.com) should review the [Docker
Documentation](https://docs.docker.com/). Students are also encouraged to review
the documentation for their text editor, which is available in the [VS Code
docs](https://code.visualstudio.com/docs). You should also review the [Git
documentation](https://git-scm.com/doc) to learn more about how to use the Git
command-line client. In addition to talking with the instructor and technical
leader for your course, students are encouraged to search
[StackOverflow](https://stackoverflow.com/) for answers to their technical
questions.

As outlined in the course schedule in the [course planning
repository](https://github.com/Allegheny-Computer-Science-102-F2020/cs102-F2020-plans),
students should also read all of the assigned readings for up to and including
the week of the semester on which this laboratory assignment was assigned.

## Assignment Reminders

- **Follow each step carefully**. Slowly read each sentence in this document,
  making sure that you precisely follow each instruction. Take notes about each
  step that you attempt, recording your questions and ideas and the challenges
  that you faced. If you are stuck, then please tell a technical leader or the
  course instructor what assignment step you recently completed.

- **Regularly ask and answer questions**. Please log into Slack at the start of
  the laboratory session and then join the appropriate channel. If you have a
  question about one of the steps in an assignment, then you can post it to the
  designated channel, discussing your questions through both Slack and the
  Google Meet designated for the class.

- **Store your files in GitHub**. Starting with this laboratory assignment, you
  will be responsible for storing all of your files (e.g., Python source code
  and Markdown-based writing) in a Git repository using GitHub Classroom. Please
  verify that you have saved your source code in your Git repository by using
  `git status` to ensure that everything is updated. You can see if your
  assignment submission meets the established correctness requirements by using
  the provided checking tools on your local computer and by checking the commits
  in GitHub.

- **Keep all of your files**. Don't delete your programs, output files, and
  written reports after you submit them through GitHub; you will need them
  again when you study for the course assessments and work on the other
  laboratory, practical, and technical challenge assignments.

- **Hone your technical writing skills**. Computer science assignments require
  to you write technical documentation and descriptions of your experiences when
  completing each task. Take extra care to ensure that your writing is
  interesting and both grammatically and technically correct, remembering that
  computer scientists must effectively communicate and collaborate with their
  team members and the student technical leaders and course instructor.

- **Review the Honor Code on the syllabus**. While you may discuss your
  assignments with others, copying source code or technical writing is a
  violation of Allegheny College's Honor Code.

## Accessing the Assignment

To access this assignment, you should go into the `#announcements` channel in
our Slack workspace and find the announcement that provides a link for it. Copy
this link and paste it into your web browser. Now, you should accept the
laboratory assignment and see that GitHub Classroom created a new GitHub
repository for you to access the assignment's starting materials and to store
the completed version of your assignment. Specifically, to access your new
GitHub repository for this assignment, please click the green "Accept" button
and then click the link that is prefaced with the label "Your assignment has
been created here". If you accepted the assignment and correctly followed these
steps, you should have created a GitHub repository with a name like
`Allegheny-Computer-Science-102-Fall-2020/computer-science-102-fall-2020-lab-5-gkapfham`.
Unless you provide the course instructor with documentation of the extenuating
circumstances that you are facing, not accepting the assignment means that you
automatically receive a failing grade for all of its components.

Before you move to the next step of this laboratory assignment, please make
sure that you read all of the content on the web site for your new GitHub
repository, paying close attention to the technical details about the commands
that you will type and the output that your program must produce. Now you are
ready to download the starting materials to your laboratory computer. Click the
"Clone or download" button and, after ensuring that you have selected "Clone
with SSH", please copy this command to your clipboard. To enter into your
course directory directory you should now type `cd cs102F2020`. Next, you can
type the either `ls` (on either MacOS or Linux) or `dir` (on Windows 10 Pro or
Windows 10 Enterprise) and see that there are no files or directories inside of
this directory. By typing `git clone` in your terminal and then pasting in the
string that you copied from the GitHub site you will "download" all of the code
for this assignment. For instance, if the course instructor ran the `git clone`
  command in the terminal, it would look like:

```
git clone git@github.com:Allegheny-Computer-Science-102-F2020/computer-science-102-fall-2020-lab-5-gkapfham.git
```

After this command finishes, you can use `cd` to change into the new directory.
If you want to "go back" one directory from your current location, then you can
type the command `cd ..`. Finally, please continue to use the `cd` and `ls`
commands to explore the files that you automatically downloaded from GitHub. If
one of the aforementioned commands does not work correctly, then it is possible
that your terminal window is not up-to-date or not configured correctly. In this
case, please share your specific error messages with the instructor, ultimately
working to master the use of terminal commands. What files and directories do
you see? What do you think is their purpose? Spend some time exploring, telling
your discoveries to a student technical leader.

## Laboratory Assignment Tasks

### Installing Programs that Support Python Programming

If you have not already done so, you need to install the [Poetry
tool](https://python-poetry.org/docs/) for dependency management and packaging
of Python programs. After ensuring that you have Python 3.8 installed on your
laptop, please follow the installation instructions for Poetry. For instance,
you are using either MacOS or Linux you need to type the following command in
your terminal window `curl -sSL
https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py |
python`. Importantly, this command will only work if you have already installed
a program called `curl`. If you are using Windows 10 Pro then you will need to
follow the PowerShell installation instructions on Poetry's web site.

Now, making sure that you are in your "home base" directory for this laboratory
assignment, you need to install the dependencies for the `iterator` program
that you will implement, debug, and observe. To complete this step you need to
type `cd iterator` and then `poetry install`. What output did this command
produce? What do you think that this step did? Why is important to type these
commands? Make sure that you know the answers to these question before moving
onto the next step of the assignment.

Finally, it is important to note that if you are not able to correctly install
Python 3.8.5 and Poetry on your laptop, you can opt to use Python and the Poetry
tool in the Docker container provided by the course instructor. Please refer to
the content in this assignment sheet about how to run an interactive shell in a
Docker container and then use the Poetry commands mentioned in both this section
and the next sections of the assignment sheet.

### Summarizing Real-World Populate Data Using Functions and Iteration Constructs

Please make sure that you investigate all of the Python source code files
provided in the assignment repository. You should notice that there are `TODO`
markers indicating that you need to add Python source code that will, for
instance, read in data values from a file, convert textual data values to
floating point numbers, and compute the arithmetic mean of the numbers. To get
started, make sure that you investigate the type of data that the
`inputs/data.txt` file contains. Here is a sample of the first ten lines of this
file:

```
1970-01-01,81.342
1971-01-01,83.300
1972-01-01,84.700
1973-01-01,85.500
1974-01-01,86.100
1975-01-01,87.000
1976-01-01,87.600
1977-01-01,87.600
1978-01-01,88.000
1979-01-01,88.100
1980-01-01,88.869
```

Before you continue to work on this assignment, please make sure that you
understand the meaning of the data in this file. To accomplish this task, you
should examine the discussion of this data set, including its visualization from
1970 until 2019, from the [Residential Population in Crawford County,
PA](https://fred.stlouisfed.org/series/PACRAW0POP) from the [Federal Reserve
Bank of St. Louis](https://fred.stlouisfed.org/). The idea of this program is
that it should summarize the population data for Crawford County, the county in
which Allegheny College is located. Perhaps the best way to understand the
expected behavior of this program is to observe the output of a completed
version of it. For instance, the command `poetry run python
superdatasummarizer --data-file inputs/data.txt` produces the following output:

```
The data file contains 50 data values in it!
Let's do some SUPER summarizing! 🚀

The computed mean is 87.79945999999998!
The computed median is 88.05!

The computed variance is 3.692208448400001!
The computed standard deviation is 1.9215120214039778!
```

If you have questions about how to calculate any of these values, please refer
to your textbook called *Doing Math with Python* so that you can review the
equations and Python source code to calculate the mean, median, variance, and
standard deviation. In summary, you must follow all of the instructions next to
the `TODO` markers in the provided source code to implement a program that can
correctly compute the four summary statistics for the provided data values in
the `datasummarizer/inputs/data.txt` file. In addition to ensuring that your
program is adequately documented, has the correct format, and adheres to all of
the industry best practices for the chosen Python source code constructs, you
must implement functions that pass a provided Pytest test suite, as explained
next.

### Running a Pytest Test Suite to Establish a Confidence in Function Correctness

Your GitHub repository for this assignment also contains a small [Pytest
](https://docs.pytest.org/en/stable/) test suite that provides a function under
test with inputs and then checks to see if it produces the expected output. You
can run the four tests in the test suite by typing the following command in your
terminal window: `poetry run pytest -v`. If your program is implemented correctly,
then it should produce output like the following:

```
================================================================== test session starts ==================================================================
platform linux -- Python 3.8.5, pytest-5.4.3, py-1.9.0, pluggy-0.13.1 -- /home/gkapfham/.cache/pypoetry/virtualenvs/superdatasummarizer-Cf2dfZ4V-py3.8/bin/python
cachedir: .pytest_cache
rootdir: /home/gkapfham/working/teaching/github-classroom/Allegheny-Computer-Science-102-F2020/solutions/cs102-F2020-lab5-solution/superdatasummarizer
collected 13 items

tests/test_summarize.py::test_summarize_empty_number_list_mean PASSED                                                                             [  7%]
tests/test_summarize.py::test_summarize_pos_neg_number_list PASSED                                                                                [ 15%]
tests/test_summarize.py::test_summarize_equal_number_list PASSED                                                                                  [ 23%]
tests/test_summarize.py::test_summarize_different_number_list PASSED                                                                              [ 30%]
tests/test_summarize.py::test_summarize_empty_number_list_median PASSED                                                                           [ 38%]
tests/test_summarize.py::test_summarize_full_list_median_even PASSED                                                                              [ 46%]
tests/test_summarize.py::test_summarize_full_list_median_odd PASSED                                                                               [ 53%]
tests/test_summarize.py::test_compute_difference_empty_list PASSED                                                                                [ 61%]
tests/test_summarize.py::test_summarize_compute_difference PASSED                                                                                 [ 69%]
tests/test_summarize.py::test_summarize_full_list_variance_even PASSED                                                                            [ 76%]
tests/test_summarize.py::test_summarize_full_list_standard_deviation_even PASSED                                                                  [ 84%]
tests/test_transform.py::test_transform_empty_text_list_to_number_list PASSED                                                                     [ 92%]
tests/test_transform.py::test_transform_small_text_list_to_number_list PASSED                                                                     [100%]

================================================================== 13 passed in 0.03s ===================================================================
```

If your test suite has failing test cases in it, then you need to keep working
to enhance your program, ultimately ensuring that the test suites passes and
that all runs of the program produce the expected output. If you are interested
in doing so, please add more test cases to either the `tests/test_summarize.py`
test suite or the `tests/test_transform.py` test suite so as to better ensure
that the functions under test work correctly. Since it is also important to
ensure that your program's source code adheres to all industry-standard best
practices, you should run the command `poetry run pylint superdatasummarizer
tests`, fixing any issues that it raises. Finally, you can ensure that your
program's source code has an industry-standard format by running the command
`poetry run black superdatasummarizer tests`.

### Reflecting on the Laboratory Assignment

Once you have finished both of the previous technical tasks, use your text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block, explain the meaning of the source code segments, and answer all of the
other questions about your experiences in completing this laboratory assignment.

### Transferring Your Source code and Technical Writing to GitHub

As you are working on your laboratory assignment, please make sure that you use
VSCode to regularly save your work and transfer it to the GitHub servers. For
instance, please use the `git commit` command in your terminal window or use the
similar feature in VSCode to "stage" your changes in your repository. Once you
have committed your source code to your repository, you can use the `git push`
command to transfer your work to your GitHub repository, making it available for
the course instructor to assess. Please make sure that you regularly commit your
source code and technical writing, using descriptive commit messages to explain
how each commit changes the contents of the repository. Please do not use
vacuous commit messages that do not explain how your commit changes the contents
of the repository!

## Automated Checks with GatorGrader

In addition to meeting all of the requirements outlined in this assignment
sheet, your submission must pass the following checks that
[GatorGrader](https://github.com/GatorEducator/gatorgrader) automatically
assesses:

If [GatorGrader's](https://github.com/GatorEducator/gatorgrader) automated
checks pass correctly, the tool will produce the output like the following in
addition to returning a zero exit code (which you can access by typing the
command `echo $?`). You will need to run
[GatorGrader](https://github.com/GatorEducator/gatorgrader) in a Docker
container by following the steps in the [Using Docker](#using-docker) section.

- The command `cd superdatasummarizer; poetry install; poetry run python superdatasummarizer --data-file inputs/data.txt; cd ..` executes correctly
- The file __main__.py exists in the superdatasummarizer/superdatasummarizer directory
- The file reflection.md exists in the writing directory
- The file summarize.py exists in the superdatasummarizer/superdatasummarizer directory
- The file test_summarize.py exists in the superdatasummarizer/tests directory
- The file test_transform.py exists in the superdatasummarizer/tests directory
- The file transform.py exists in the superdatasummarizer/superdatasummarizer directory
- The __main__.py in superdatasummarizer/superdatasummarizer has at least 2 multiple-line Python comment(s)
- The __main__.py in superdatasummarizer/superdatasummarizer has at least 4 single-line Python comment(s)
- The __main__.py in superdatasummarizer/superdatasummarizer has exactly 0 of the `TODO` fragment
- The __main__.py in superdatasummarizer/superdatasummarizer has exactly 1 of the `summarize.compute_mean` fragment
- The __main__.py in superdatasummarizer/superdatasummarizer has exactly 1 of the `transform.transform_string_to_number_list` fragment
- The reflection.md in writing has at least 1 of the `code` tag
- The reflection.md in writing has at least 3 of the `code_block` tag
- The reflection.md in writing has at least 500 word(s) in total
- The reflection.md in writing has exactly 0 of the `Add Your Name Here` fragment
- The reflection.md in writing has exactly 0 of the `TODO` fragment
- The reflection.md in writing has exactly 9 of the `heading` tag
- The repository has at least 5 commit(s)
- The summarize.py in superdatasummarizer/superdatasummarizer has at least 2 multiple-line Python comment(s)
- The summarize.py in superdatasummarizer/superdatasummarizer has at least 3 of the `nan` fragment
- The summarize.py in superdatasummarizer/superdatasummarizer has at least 4 of the `-> float` fragment
- The summarize.py in superdatasummarizer/superdatasummarizer has at least 6 of the `List[float]` fragment
- The summarize.py in superdatasummarizer/superdatasummarizer has exactly 0 of the `TODO` fragment
- The summarize.py in superdatasummarizer/superdatasummarizer has exactly 1 of the `from typing import List` fragment
- The test_summarize.py in superdatasummarizer/tests has at least 5 multiple-line Python comment(s)
- The test_summarize.py in superdatasummarizer/tests has exactly 0 of the `TODO` fragment
- The test_transform.py in superdatasummarizer/tests has at least 3 multiple-line Python comment(s)
- The test_transform.py in superdatasummarizer/tests has exactly 0 of the `TODO` fragment
- The transform.py in superdatasummarizer/superdatasummarizer has at least 2 multiple-line Python comment(s)
- The transform.py in superdatasummarizer/superdatasummarizer has exactly 0 of the `TODO` fragment
- The transform.py in superdatasummarizer/superdatasummarizer has exactly 1 of the `from typing import List` fragment

```
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Passed 32/32 (100%) of checks for cs102-F2020-lab5! ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Assignment Assessment

Taking inspiration from the principles of [specification-based
grading](https://www.amazon.com/Specifications-Grading-Restoring-Motivating-Students/dp/1620362422),
the grade that a student receives on a laboratory assignment will be based on
whether or not it meets the standards for technical work in the fields of
software engineering and discrete structures. Instead of receiving a single
numerical or letter grade for this assignment, your grade will have the
following components:

- **Percentage of Correct GatorGrader Checks Ranging Between 0 and 100**: Your
  submitted Python program must pass all of GatorGrader's checks by, for
  instance, ensuring that it produces the correct output and has all of the
  required characteristics. Your technical writing must pass all of
  GatorGrader's checks about, for instance, the length of its output and its use
  of the required Markdown language features for technical writing. For this
  component of a laboratory assignment's grade, your work will receive a
  percentage, ranging from 0 to 100, that corresponds to the percentage of
  GatorGrader checks that automatically pass inside of a GitHub Actions build.

- **GitHub Actions Build Status of Either ✔  or ❌**: Since additional checks on
  the Python source code and/or technical writing are encoded in GitHub Action
  workflows and, moreover, all of the GatorGrader checks are also run in GitHub
  Actions, your work will receive a checkmark grade if the last
  before-the-deadline build in GitHub Actions passes and a ✔  appears in the
  GitHub commit log instead of an ❌. The build status reported by GitHub
  Actions will only be a ✔ if the source code and technical writing in the
  GitHub repository pass all of both the GatorGrader checks and the additional
  checks.

- **Technical Writing Mastery of Either ✔  or ❌**: Students will also receive a
  ✔ grade when the responses to the technical writing questions presented in the
  `writing/reflection.md` reveal a mastery of technical writing skills. To
  receive a checkmark grade, the submitted writing should have correct spelling,
  grammar, punctuation, and formatting in addition to following the rules of the
  Markdown language. Your work will receive a ✔ grade for this component
  if the build report from GitHub Actions reveals that there are no detected
  mistakes in the technical writing.

- **Technical Knowledge and Skill Mastery of Either ✔  or ❌**: Students will
  also receive a checkmark grade when the GitHub repository reveals that they
  have mastered all of the technical knowledge and skills developed during the
  completion of the laboratory assignment. As a part of this grade, the
  instructor will assess aspects of the project including, but not limited to,
  the use of effective Python source code comments, correct Git commit messages,
  and accurate responses to the technical writing questions.

## Advance Feedback on an Assignment

Students who wish to receive feedback on their work for any course assignment
should first open an issue on the issue tracker for their assignment's GitHub
repository, giving an appropriate title and description for the type of feedback
that you would like the course instructor to provide. After creating this issue,
you will see that GitHub has created a unique web site that references it. To
alert the course instructor to the fact that the issue was created and that you
want feedback on your work, please send it to him by a Slack direct message at
least 24 hours in advance of the project's due date. After the instructor
responds to the issue, please resolve all of the stated concerns and participate
in the discussion until the issue is resolved and ultimately marked as closed.

## Discussion of a Graded Assignment

Students who wish to receive feedback on their work for any graded course
assignment should leave question in the same region of Github where the course
instructor submitted the assignment's grade. For example, if the instructor
submits your grade to a pull request in your repository for a laboratory
assignment, then you should ask questions about your grade in that pull request,
bearing in mind the need to @-mention the course instructor in the body of your
comment. Students can continue to discuss the graded assignment with the course
instructor until they understand all the technical topics that were the
focus of the particular assignment.

## Additional Resources

### System Commands

This project invites students to enter system commands into a terminal window.
This assignment uses [Docker](https://www.docker.com) to deliver programs, such
as `gradle` and the source code and packages needed to run
[GatorGrader](https://github.com/GatorEducator/gatorgrader), to a students'
computer, thereby eliminating the need for a programmer to install them on their
development workstation. Individuals who do not want to install Docker can
optionally install of the programs mentioned in the [Project
Requirements](#requirements) section of this document.

### Using Docker

Once you have installed [Docker
Desktop](https://www.docker.com/products/docker-desktop), with MacOS and Linux
you can use the following `docker run` command to start `gradle grade` as a
containerized application, using the
[DockaGator](https://github.com/GatorEducator/dockagator) Docker image available
on
[DockerHub](https://cloud.docker.com/u/gatoreducator/repository/docker/gatoreducator/dockagator).

```bash
docker run --rm --name dockagator \
  -v "$(pwd)":/project \
  -v "$HOME/.dockagator":/root/.local/share \
  gatoreducator/dockagator
```

Please note that not all version of the Windows terminal window will correctly
recognize the use of the `%cd%` and `%HomeDrive%%HomePath%` variables. In this
case, you should substitute the actual directory for a specific course
assignment for the `%cd%` variable and the drive letter that contains the
`.dockagator` directory for the `%HomeDrive%%HomePath%` variable. Finally, the
Windows terminal window may not work correctly when you attempt to run a
multi-line command. In this case, you should break up the aforementioned
four-line command into separate lines, like `docker run --rm --name dockagator`
and `-v "%cd%:/project"` and then connect them into a single long line that you
separate by a single space. Here is an example of what the long command would
look like, again assuming that the Windows `cmd` terminal correctly interprets
the `%cd%` and `%HomeDrive%%HomePath%` variables:

```bash
docker run -it --rm --name dockagator -v "%cd%:/project" -v "%HomeDrive%%HomePath%/.dockagator:/root/.local/share" gatoreducator/dockagator /bin/bash
```

Here are some additional commands that you may need to run when using Docker:

* `docker info`: display information about how Docker runs on your workstation
* `docker images`: show the Docker images installed on your workstation
* `docker container list`: list the active images running on your workstation
* `docker system prune`: remove many types of "dangling" components from your workstation
* `docker image prune`: remove all "dangling" docker images from your workstation
* `docker container prune`: remove all stopped docker containers from your workstation
* `docker rmi $(docker images -q) --force`: remove all docker images from your workstation

## Commands for an Interactive Docker Shell

Since the above `docker run` command uses a Docker images that, by default, runs
`gradle grade` and then exits the Docker container, you may want to instead run
the following command so that you enter an "interactive terminal" that will
allow you to repeatedly run commands within the Docker container. Don't forget
that, if you are using the Windows operating system, then you will need to use a
different command to run Docker, as explained previously in this document.
Importantly, the command that you type if you are a Windows user should still
contain the `-it` at the start of the `docker run` and the `/bin/bash` at the
end of the command. However, the other components of this command need to be
customized for the Windows operating system.

If you use either MacOS or Linux, then this is the command that you would run to
enter into the interactive terminal provided by a Docker container:

```bash
docker run -it --rm --name dockagator \
  -v "$(pwd)":/project \
  -v "$HOME/.dockagator":/root/.local/share \
  gatoreducator/dockagator /bin/bash
```

If you use Windows, then this is the command that you would run to enter into
the interactive terminal provided by a Docker container:

```bash
docker run -t --rm --name dockagator \
  -v "%cd%:/project" \
  -v "%HomeDrive%%HomePath%/.dockagator:/root/.local/share" \
  gatoreducator/dockagator /bin/bash
```

Once you have typed this command, you can use the [GatorGrader
tool](https://github.com/GatorEducator/gatorgrader) in the Docker container by
typing the command `gradle grade` in your terminal. Running this command will
produce a lot of output that you should carefully inspect. If GatorGrader's
output shows that there are no mistakes in a course assignment, then your source
code and technical writing are passing all of the automated baseline checks.
However, if the output indicates that there are mistakes, then you will need to
understand what they are and then try to fix them.

Remember, to correctly run any of the commands mentioned in this guide, you must
be in the main (i.e., "home base") directory for this assignment where the
`build.gradle` file is located.

## Upgrading the Docker Container

If the course instructor provides a new version of the Docker container called
`gatoreducator/dockagator` and you want to receive it immediately, you must
first delete the existing Docker container on your laptop by running the command
`docker rmi gatoreducator/dockagator`. Next, you can re-run one of the
aforementioned Docker commands, like the following one, which would work on
MacOS or Linux:

```
docker run -it --rm --name dockagator \
  -v "$(pwd)":/project \
  -v "$HOME/.dockagator":/root/.local/share \
  gatoreducator/dockagator /bin/bash
```

Please note that if you attempt to run `gradle grade` in an updated Docker
container it is possible that the command will execute incorrectly if you
previously used GatorGrader with a Docker container that featured a different
version of the Python programming language. In this situation, you should delete
the directories inside of the `.dockagator` directory and then again attempt to
run the `gradle grade` command inside of the Docker container. Specifically, you
will need to delete directories in `.dockagator` that are normally called
`gatorgrader`, `virtualenv`, and `virtualenvs`.

### Downloading Project Updates

If GatorGrader's maintainers push updates to this sample assignment and you
received it through GitHub Classroom and you would like to also receive these
updates, then you can type this command in the main directory for this
assignment:

```
git remote add download git@github.com:Allegheny-Computer-Science-102-F2020/cs102-F2020-lab5-starter.git
```

You should only need to type this command once; running the command additional
times may yield an error message but will not negatively influence the state of
your Git repository. Now, you are ready to download the updates provided by the
GatorGrader maintainers by typing this command:

```
git pull download master
```

This second command can be run whenever the maintainers needs to provide you
with new source code for this assignment. However, please note that, if you have
edited the files that we updated, running the previous command may lead to Git
merge conflicts. If this happens, you may need to manually resolve them with the
help of the instructor or a student technical leader. Finally, please note that
the [Gradle plugin](https://github.com/GatorEducator/gatorgradle) for
[GatorGrader](https://github.com/GatorEducator/gatorgrader) will automatically
download the newest version of GatorGrader.

### Using GitHub Actions

This assignment uses [GitHub Actions](https://github.com/features/actions) to
automatically run [GatorGrader](https://github.com/GatorEducator/gatorgrader)
and additional checking programs every time you commit to your GitHub
repository. The checking will start as soon as you have accepted the assignment
&mdash; thus creating your own private repository &mdash; and the course
instructor and/or GitHub enables GitHub Actions on it. If you do not see either
a yellow &#9679; or a green ✔ or a red ❌ in your listing of commits, then
please ask the instructor to see whether or not GitHub Actions was correctly
enabled.

### System Requirements

This assignment was developed to work with the following software and versions:

- Docker Desktop
- Operating Systems
  - Linux
  - MacOS
  - Windows 10 Pro
  - Windows 10 Enterprise
- Programming Language Tools
  - Gradle 6.6
  - MDL 0.5.0
  - Python 3.7 or 3.8

### Reporting Problems

If you have found a problem with this assignment's provided source code or
documentation, then you can go to the [Computer Science 102 Fall 2020 Planning
Repository](https://github.com/Allegheny-Computer-Science-102-F2020/cs102-F2020-plans)
and [raise an
issue](https://github.com/Allegheny-Computer-Science-102-F2020/cs102-F2020-plans/issues).
If you have found a problem with the [GatorGrader
tool](https://github.com/GatorEducator/gatorgrader) and the way that it checks
your assignment, then you can also [raise an
issue](https://github.com/GatorEducator/gatorgrader/issues) in that repository.
To ensure that your issue is properly resolved, please provide as many details
as is possible about the problem that you experienced. Individuals who find, and
use the appropriate GitHub issue tracker to correctly document, a mistake in any
aspect of this assignment will receive extra credit towards their grade for the
course.

### Receiving Assistance

If you are having trouble completing any part of this project, then please talk
with either the course instructor or a student technical leader during the
course session. Alternatively, you may ask questions in the Slack workspace for
this course. Finally, you can schedule a meeting during the course instructor's
office hours.
