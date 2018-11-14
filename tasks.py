from invoke import task

@task
def run(c):
    """ Runs main function """
    c.run('python3 data_mine/amazon/mine.py')

@task
def setup(c):
    c.run('python3 nltk_setup.py')
