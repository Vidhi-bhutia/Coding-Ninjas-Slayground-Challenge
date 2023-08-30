int removeDuplicates(vector<int> &arr, int n) 
{
 	int newLen = 1;
 	for( int i = 1; i < n; i++ ) 
	{
 		if( arr[i-1] != arr[i] ) 
 			newLen++;
 	}
	return newLen;
}
