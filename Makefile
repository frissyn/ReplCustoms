export TARGET_FILE = app/application.cr
export SOURCE_FILES = $(shell find . **/*)

.PHONY: run
run: ./application
	./application

./application: $(SOURCE_FILES)
	crystal build --no-debug --progress $(TARGET_FILE)