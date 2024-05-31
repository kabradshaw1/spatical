#include <iostream>
int main()
{
    int arr[2][4]={{0,1,2,3},{4,5,6,7}};
    for(int row=0; row<2; row++)
        for(int col=0; col<4; col++)
            std::cout<<row<<" , "<<col<<" , "<<arr[row][col]<<std::endl;
    return(0);
}
