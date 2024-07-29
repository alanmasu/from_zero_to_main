void copia_stringa(char source[], char dest[]);

int main(){
    char a [10] = "ciao";
    char b [10] = "";
    copia_stringa(a, b);
    return 0;
}


void copia_stringa(char source[], char dest[]){
    unsigned int i = 0;
    while(source[i] != '\0'){
        dest[i] = source[i];
    }
}
