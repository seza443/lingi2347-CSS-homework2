#include <stdio.h>
#include <string.h>

// Based on this article: http://www.thegeekstuff.com/2013/06/buffer-overflow/?utm_source=feedly
int main(int argc, char *argv[])
{
    char vulnerable_buffer[15];
    int password_correct = 0;

    strcpy(vulnerable_buffer, argv[1]);

    if(strcmp(vulnerable_buffer, "rootpassword") == 0) // strcmp returns 0 if buffers are equals
    {
      password_correct = 1;
    }

    if(password_correct)
    {
        printf ("true");
    }
    else
    {
        printf ("false");
    }

    return 0;
}
