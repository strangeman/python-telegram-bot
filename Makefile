all: install run

install:
	./install.sh

run:
	./run.sh

reset_state:
	./reset_state.sh

clean: reset_state
	rm -r ./data/log/*