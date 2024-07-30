main :
	riscv32-unknown-elf-gcc -T utils/ld_script.ld src/main.c -o build/main.elf

show_all_build_res: show_build_res
	riscv32-unknown-elf-objdump -D build/main.elf

show_build_res: 
	riscv32-unknown-elf-objdump -t build/main.elf

create_coe:
	python3 utils/create_venv.py
	$(\
		source .venv/bin/activate; \
		pip3 install pyelftools; \
	)
	python3 utils/elfToCoe.py build/main.elf