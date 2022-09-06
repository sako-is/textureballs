CC := clang
CFLAGS := -Wall
EXEC := tball

BUILD := bin
TARGETS := $(BUILD)/$(EXEC)
FILES := $(shell find . -type f -name "*.c")

FLAGS := -g
LINKERFLAGS = -lraylib -lm

DEFINES :=

all:
	$(CC) $(FILES) $(CFLAGS) $(FLAGS) -o $(TARGETS) $(DEFINES) $(LINKERFLAGS)

clean:
	rm -rf $(BUILD)/$(EXEC)