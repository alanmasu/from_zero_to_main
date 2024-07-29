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
---

Il formato tipico dell'uscita è simile al seguente:

```
SYMBOL TABLE:
00000000 l    df *ABS* 00000000 crtstuff.c
00000000 l    d  .text 00000000 .text
00000000 l    d  .data 00000000 .data
00000000 l    d  .bss  00000000 .bss
00000000 g    F .text 00000074 main
00000000 g    O .data 00000004 myGlobalVar
00000000 g    F .text 00000028 myFunction
00000000 g    F .text 00000000 myOtherFunction
```

Le colonne principali che puoi vedere sono:

1. **Indirizzo**: Questo è l'indirizzo di memoria in cui si trova il simbolo.
2. **Tipo**: Questa colonna può contenere una combinazione di lettere che indicano vari attributi del simbolo. Ad esempio:
   - `l` indica che il simbolo è locale (non esportato).
   - `g` indica che il simbolo è globale (esportato).
   - `u` indica che il simbolo è undefined (non definito in questo file oggetto).
   - `F` indica che il simbolo è una funzione.
   - `O` indica che il simbolo è un oggetto dati (variabile).
   - `d` indica che il simbolo è una sezione di dati.
   - `D` indica che il simbolo è in una sezione di dati inizializzati.
   - `B` indica che il simbolo è in una sezione BSS (dati non inizializzati).
   - `T` indica che il simbolo è in una sezione di codice (text).
   - `*ABS*` indica che il simbolo ha un indirizzo assoluto.

3. **Sezione**: Il nome della sezione in cui si trova il simbolo (come `.text`, `.data`, `.bss`).
4. **Dimensione**: La dimensione del simbolo in byte.
5. **Nome del simbolo**: Il nome del simbolo stesso (funzione, variabile, ecc.).

Esempio spiegato:

```
00000000 g    F .text 00000074 main
```

- **Indirizzo**: `00000000`
- **Tipo**: `g` (globale), `F` (funzione)
- **Sezione**: `.text`
- **Dimensione**: `00000074` (116 bytes)
- **Nome del simbolo**: `main`

Questo indica che `main` è una funzione globale, situata nella sezione `.text` con una dimensione di 116 byte.

---

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
├── src
│   └── main.c
└── utils
    └── ld_script.ld
````