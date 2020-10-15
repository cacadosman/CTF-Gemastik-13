// gcc CDLL.c -o CDLL -fstack-protector-all -pie -Wl,-z,relro,-z,now

#include<stdio.h>
#include<malloc.h>
#include<unistd.h>
#include<stdlib.h>

struct node
{
    char node_name[8];
    struct node *next;
    struct node *prev;
    unsigned long int data_size;
    char data[];
};

struct node *CurrentNode;

void read_str(unsigned int n, char* str){
    unsigned int c;
    c = read(0, str, n);
    if(c < 0){
        puts("Read error!");
        exit(-1);
    }
    else if (c > 0){
        str[c-1] = 0;
    }
}

unsigned int read_int(){
    char c[8];
    read_str(8, c);
    return (unsigned int) atoi(c);
}

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
}

void create_node(unsigned int isPrev){
    struct node *Node;
    unsigned int dataSize;

    printf("Data size : ");
    dataSize = read_int();
    if(dataSize < 0x80){
        Node = malloc(dataSize + 32);

        Node->data_size = dataSize;
        printf("Node name : ");
        read_str(16, Node->node_name);
        printf("Data : ");
        read_str(dataSize, Node->data);
        
        if(CurrentNode == NULL){
            Node->prev = Node;
            Node->next = Node;
            CurrentNode = Node;
        }
        else if(isPrev == 0){
            Node->prev = CurrentNode;
            Node->next = CurrentNode->next;
            CurrentNode->next->prev = Node;
            CurrentNode->next = Node;
        }
        else{
            Node->prev = CurrentNode->prev;
            Node->next = CurrentNode;
            CurrentNode->prev->next = Node;
            CurrentNode->prev = Node;
        }
    }
    else{
        puts("Too large!");
    }
}

void edit_current_node(){
    if(CurrentNode != NULL){
        printf("Data : ");
        read_str(CurrentNode->data_size, CurrentNode->data);
    }
    else
        printf("NULL\n");
}

void goto_node(unsigned int isPrev){
    if(CurrentNode != NULL){
        if(isPrev == 1)
            CurrentNode = CurrentNode->prev;
        else
            CurrentNode = CurrentNode->next;
    }
    else
    {
        printf("NULL\n");
    }
    
}

void delete_node(unsigned int isPrev){
    struct node *temp;

    if(CurrentNode != NULL){
        if(isPrev == 1){
            temp = CurrentNode->prev;
            CurrentNode->prev = CurrentNode->prev->prev;
            CurrentNode->prev->next = CurrentNode;
        }
        else{
            temp = CurrentNode->next;
            CurrentNode->next = CurrentNode->next->next;
            CurrentNode->next->prev = CurrentNode;
        }
        
        free(temp);
    }
    else
    {
        printf("NULL\n");
    }
    
}

void print_menu(){
    puts("\n=== MENU ===\n");
    if(!CurrentNode)
        puts("Current node Name : -");
    else
        printf("Current node name : %s\n\n", CurrentNode->node_name);

    puts("[1] Insert next");
    puts("[2] Insert prev");
    puts("[3] Go to next node");
    puts("[4] Go to prev node");
    puts("[5] Delete next");
    puts("[6] Delete prev");
    puts("[7] Edit current node data");
    puts("[8] Reset");
    puts("[9] Exit");
    printf("> ");
}

int main(){
    int c = 0;
    init();
    while (c != 9)
    {
        print_menu();
        c = read_int();
        switch (c)
        {
        case 1:
            create_node(0);
            break;
        case 2:
            create_node(1);
            break;
        case 3:
            goto_node(0);
            break;
        case 4:
            goto_node(1);
            break;
        case 5:
            delete_node(0);
            break;
        case 6:
            delete_node(1);
            break;
        case 7:
            edit_current_node();
            break;
        case 8:
            CurrentNode = NULL;
            break;
        case 9:
            break;
        
        default:
            puts("Invalid choice!");
            break;
        }
    }
    
}