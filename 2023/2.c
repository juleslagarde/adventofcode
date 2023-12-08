#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef enum {
    RED = 0,
    GREEN,
    BLUE,
    NB_COLORS,
} color_t;

typedef int game_t[NB_COLORS];

game_t valid_game = { /*RED*/ 12, /*GREEN*/ 13, /*BLUE*/ 14};

color_t get_color(const char* c){
    if (strcmp(c, "red") == 0) return RED;
    else if (strcmp(c, "green") == 0) return GREEN;
    else if (strcmp(c, "blue") == 0) return BLUE;
    printf("%s\n", c); fflush(stdout);
    // Add default case
    assert(false);
    return 0;
}

int main(){
    char buffer[256];
    int sum = 0, sumPower = 0;
    for(int i=0; fgets(buffer, sizeof(buffer), stdin); i++){
        //printf("  buffer: %s\n", buffer); fflush(stdout);
        int size = strnlen(buffer, sizeof(buffer));
        buffer[--size] = '\0'; //remove the '\n' at the end
        char *pt1_start = strchr(buffer, ':');
        assert(pt1_start!=NULL);
        game_t max_game = {0};
        do { //iterate over ';'
            //printf("    pt1_start+1: %s\n", pt1_start+1); fflush(stdout);
            char *pt1_end = strchrnul(pt1_start+1, ';');
            char *pt2_start = pt1_start;
            do { //iterate over ','
                assert(pt2_start[1]==' ');
                pt2_start += 2;//skip the separator and the space
                char *pt2_end = strchrnul(pt2_start, ',');
                pt2_end = (pt1_end>pt2_end)?pt2_end:pt1_end; //if the next ',' is after ';' choose ';'
                *pt2_end = '\0';//replace the comma with end string
                char *pt_space = strchr(pt2_start, ' ');
                *pt_space = '\0';//replace the space with end string
                int n = atoi(pt2_start);
                color_t c = get_color(pt_space+1);
                //printf("      color: %s: %d\n", (c==0)?"red":(c==1?"green":"blue"), n);
                max_game[c] = (max_game[c] < n)?n:max_game[c];

                pt2_start = pt2_end;
            } while(pt2_start < pt1_end);

            pt1_start = pt1_end; 
        } while(pt1_start < buffer+size);

        //printf("  %d<=%d && %d<=%d && %d<=%d\n", max_game[0],valid_game[0] , max_game[1],valid_game[1] , max_game[2],valid_game[2]);
        //printf("  game %d - validity:%b\n", i+1, max_game[0]<=valid_game[0] && max_game[1]<=valid_game[1] && max_game[2]<=valid_game[2]);
        if(max_game[0]<=valid_game[0] && max_game[1]<=valid_game[1] && max_game[2]<=valid_game[2])
            sum += i+1;  // game id == line number
        sumPower += max_game[0]*max_game[1]*max_game[2]; assert(NB_COLORS == 3);
    }
    printf("sum : %d\n",sum);
    printf("sumPower : %d\n",sumPower);
    return EXIT_SUCCESS;
}
