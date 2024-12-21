# Variables
CC = gcc
CFLAGS = -fno-stack-protector
LDFLAGS = -no-pie -Wl,-z,relro,-z,now

# Source files
SRC = chall.c
OBJ = $(SRC:.c=.o)
EXEC = chall

# Target to build the executable
all: $(EXEC)

# Link the object files to create the executable
$(EXEC): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $(OBJ)
	rm -rf $(OBJ)

# Compile source files into object files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean object files and executable
.PHONY: clean
clean:
	rm -f $(EXEC)
