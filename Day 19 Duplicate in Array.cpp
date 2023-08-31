#include <bits/stdc++.h>

int findDuplicate(vector<int> &arr) {
    int n=arr.size();
    int n_sum=((n-1)*n)/2;
    int arr_sum=0;
    for(int i:arr)
    {
        arr_sum+=i;
    }
    return arr_sum-n_sum;
}
