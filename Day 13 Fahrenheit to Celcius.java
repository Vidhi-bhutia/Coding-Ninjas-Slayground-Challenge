import java.util.* ;
import java.io.*; 

public class Solution {

public static List<List<Integer>> fahrenheitToCelsius(int s, int e, int w) {
	List<List<Integer>> list= new ArrayList<>();
	while(s<=e){
		int celcius= ((s-32)*5)/9;
		List<Integer> ans=new ArrayList<>();
		ans.add(s);
		ans.add(celcius);
		list.add(ans);
		s=s+w;
	}
	return list;
	}
}
