main :
	riscv32-unknown-elf-gcc src/main.c -o build/main.elf

show_all_build_res: show_build
	riscv32-unknown-elf-objdump -D build/main.elf

show_build_res:
	riscv32-unknown-elf-objdump -t build/main.elf