#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int count_lines(char* filename) {
    FILE *fp = fopen(filename, "r");

    int ch = 0, lines = 0;
    while (!feof(fp)) {
        ch = fgetc(fp);
        if (ch == '\n') {
            lines++;
        }
    }
    fclose(fp);
    return lines;
}

char* get_column(char* line, int num) {
    char* tok;
    for (tok = strtok(line, ","); tok && *tok; tok = strtok(NULL, ",\n")) {
        if (!--num) {
            return tok;
        }
    }
    return NULL;
}

int longest_string(char** array, int num_rows) {
    int longest = 0;
    for (int i=0; i < num_rows; i++) {
        int length = strlen(array[i]);
        if (length > longest) {
            longest = length;
        }
    }
    return longest;
}

void print_csv(char** names, char** ages, char** genders, int num_rows) {
    int names_size = longest_string(names, num_rows);
    int ages_size = longest_string(ages, num_rows);
    int genders_size = longest_string(genders, num_rows);

    int i;
    for (i=0; i<num_rows; i++) {
        printf("%-*s ", names_size, names[i]);
        printf("%-*s ", ages_size, ages[i]);
        printf("%-*s\n", genders_size, genders[i]);
    }
}

int main() {
    char* filename = "people.csv";

    int num_rows = count_lines(filename);
    char* rows_name[num_rows];
    char* rows_age[num_rows];
    char* rows_gender[num_rows];

    FILE* file = fopen(filename, "r");
    char line[1024];
    int i = 0;
    while (fgets(line, 1024, file)) {
        rows_name[i] = get_column(strdup(line), 1);
        rows_age[i] = get_column(strdup(line), 2);
        rows_gender[i] = get_column(strdup(line), 3);
        i++;
    }
    fclose(file);

    print_csv(rows_name, rows_age, rows_gender, num_rows);
    printf("%d\n", "bob" == "bob");
    return 0;
}
