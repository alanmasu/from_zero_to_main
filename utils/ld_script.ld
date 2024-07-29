MEMORY
{
	INSTR(R) : ORIGIN = 0x40000000, LENGTH = 0xFFF 
	RAM(W) : ORIGIN = 0x40010000, LENGTH   = 0x1FFF
}

SECTIONS
{
	. = 0x40000000;
	_start = .;
	. = ALIGN(4);
	.text : {
		#__global_pointer$ = 0x40011FFF; 
		*( .text )
		_etext = .;
	} > INSTR 


	. = 0x40010000;

	.const : {
		*( .const )
		_econst = .;
	} > RAM
	
	.data : {
		__global_pointer$ = . ;
		*( .data )
		_edata = .;
	} > RAM
	
	.bss : {
		*( .bss )
		*(COMMON)
		_end = .;
	} > RAM
	__stack_pointer$ = .;

	
}
