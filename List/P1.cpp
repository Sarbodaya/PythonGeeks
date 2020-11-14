#include<iostream>
using namespace std;
void chef(int q[], int n, int k)
{
    int leftQ = 0;
    for (int i = 0; i < n; i++)
    {
        if(q[i] > k)
        {
            leftQ = q[i] + leftQ;
            leftQ = q[i] - k;
        }
        else if (q[i] == k) 
        {
            leftQ = leftQ + q[i];
            leftQ = leftQ - k;
        }
        else
        {
            leftQ = leftQ + q[i];
            if(leftQ >= q[i])
            {
                leftQ = leftQ - k;
            }
            else
            {
                cout<<i+1;
            }
            
        }
        
        
    }
    
}
int main(){
    int t;
    cin>>t;
    while (t--)
    {
        int n,k;
        cin>>n;
        int q[n];
        for (int i = 0; i < n; i++)
        {
            cin>>q[i];
        }
        chef(q,n,k);
    }
    
    
    return 0;
}