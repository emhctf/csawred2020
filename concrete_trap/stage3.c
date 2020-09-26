#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

uint64_t stage3(int32_t first, int32_t second, int32_t third, int32_t fourth, int32_t fifth) {
    char cVar1;
    char cVar2;
    uint64_t uVar3;
    int64_t in_FS_OFFSET;
    int i = 0; 
    i = 0;
    while (i < 5) {
        cVar1 = (char)fourth;
        first = second >> ((char)third + cVar1 * (char)first & 0x1fU);
        cVar2 = (char)(int32_t)fifth;
        second = fourth << (cVar2 - cVar1 * (char)first & 0x1fU);
        third = (int32_t)fifth >> ((char)first + (char)third * (char)second & 0x1fU);
        fourth = second << ((char)third - cVar1 * cVar2 & 0x1fU);
        fifth = third >> ((char)fourth + (char)second * cVar2 & 0x1fU);
        i = i + 1;
    }
    uVar3 = (uint64_t)((int32_t)fifth + first + second + third + fourth == 0x7a69);
    
    if (uVar3 == 0) {
      puts("Bad failure L");
      exit(0);
    }
    puts("Great");

    
    return uVar3;

}

int main() {}

