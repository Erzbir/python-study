#include<stdlib.h>
#include<stdio.h>
#include<malloc.h>
#define INIT_SIZE 5
#define INCREMENT 2
typedef int ElemType;
typedef struct
{
    ElemType *elem;
    int length;
    int listsize;
}SqList;
int InitList_Sq(SqList *L)
{
    L->elem=(ElemType *)malloc(INIT_SIZE*sizeof(ElemType));
    if(!L->elem)return -1;
    L->length=0;
    L->listsize=INIT_SIZE;
    return 1;
}
int ListInsert_Sq(SqList *L,int i,ElemType e)
{
    int j;
    ElemType *newbase;
    if(i<0 || i>L->length)  return -1;
    if(L->length>=L->listsize)
    {
        newbase=(ElemType *)realloc(L->elem,(L->listsize+INCREMENT)*sizeof(ElemType));
        if(!newbase)return -1;
        L->elem=newbase;
        L->listsize+=INCREMENT;
    }
    for(j=L->length-1;j>=i;j--)
         L->elem[j+1]=L->elem[j];
    L->elem[i]=e;
    ++L->length;
    return 1;     
}
int ListDelete_Sq(SqList *L,int i,ElemType *e)
{
    int j;
    if(i<0 || i>L->length-1 || i>L->length==0)
    *e=L->elem[i];
    for(j=i+1;j<=L->length-1;j++)
        L->elem[j-1]=L->elem[j];
        --L->length;
        return 1;
}
int LocateElem_Sq(SqList L,ElemType e)
{
    int i=0;
    while(i<L.length&&L.elem[i]!=e)
    i++;
    if(i>=L.length)
    return -1;
    else return i;
}
int main()
{
    
}

