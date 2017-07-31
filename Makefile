wdev:
	pip install -r requirements/development.txt

git_alias:
	#git config --global alias.st status
	@echo "This will change your git alias. it's better for you to run it yourself"
	@echo "git config --global alias.st status"

dumpdata:
	python manage.py dumpdata --indent 4 > fixtures/data.json
	python manage.py dumpdata emplois --indent 4 > fixtures/db.emplois.json
	@echo 'dumping the Database for backup...we never knows '

efficient:
	@echo 'Runing pytest-watch ptw -v -c --ext=.py'
	ptw -v -c

test:
	@echo 'Runing py.test -v'
	py.test -v

test_debug:
	@echo 'Runing py.test -x --pdb '
	pytest -x --pdb 

test_failed:
	@echo 'only run the tests that failed the last time it was executed'
	@ehco 'exhaustive, informative traceback formatting'
	py.test --lf --tb=long -v

test_failed_first:
	@echo "all tests will be executed, but re-ordered based on whether they've failed in the previous run or not. Failures first, successful tests after."
	@echo "Traceback: only one line per failure"
	py.test --ff --tb=line  -v