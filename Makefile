install:
	pip install pyinstaller
	pip install py2app
execute:
ifneq (,$(findstring i, $(MAKEFLAGS)))
	pyinstall src/init.py --clean --windowed
else
	python setup.py py2app
endif
