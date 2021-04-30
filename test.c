#include <stdio.h>

main()
{
    int space,c;
    space=0;
    while((c=getchar())!=EOF){
        if(c!=' '){
            printf("%c",c);
        }
        else{
            if(space!=1){
                printf("%c",c);
                space=1;
            }
        }
    }
}