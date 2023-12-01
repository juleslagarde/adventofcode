#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// step1 result with STEP2=false, step2 result with STEP2=true
#define STEP2 true

static const char* digits[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

bool match(const char *a, const char *b){
    for(;*a==*b && *b!='\0' && *a!='\0';a++, b++){}
    return *a=='\0' || *b=='\0';//if we reached the end that means the string match
}

int get_digit(int i, char* line){
    char c = line[i];
    if('1' <= c && c <= '9'){
        return c-'0';
    }else{
#if STEP2
        for(int j=0; j<sizeof(digits)/sizeof(digits[0]); j++){
            if(match(line+i, digits[j])) return j+1;
        }
#endif
        return 0;
    }
}

int main(){
    char buffer[128];
    while(fgets(buffer, sizeof(buffer), stdin)){
        int first=0, last=0;
        int size = strnlen(buffer, sizeof(buffer));
        for(int i=0; i<size && first==0; i++){
            if((first = get_digit(i, buffer)) != 0)
                break;
        }
        for(int i=size-1; i>=0 && last==0; i--){
            if((last = get_digit(i, buffer)) != 0)
                break;
        }
        printf("%d%d\n", first, last);
    }
    return EXIT_SUCCESS;
}
