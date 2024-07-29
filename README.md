# Programma di esempio per studiare il comportamento della tool chain di RISCV 32 compilata per RV32I
Inserito un esempio di programma per la compilazione, creato il makefile

## Compilazione
``` bash
make
```
Per vedere i simboli del file oggetto:
``` bash
make show_build_res
```

Per vedere il risultato dell'intera build (simboli + disassembly di tutto l'elf):
``` bash
make show_all_build_res
```

## Struttura del progetto
```
.
├── Makefile
├── README.md
├── build
│   └── main.elf
└── src
    └── main.c
````