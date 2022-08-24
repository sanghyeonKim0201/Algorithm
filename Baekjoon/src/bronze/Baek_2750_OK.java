package bronze;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Baek_2750_OK {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		var sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		Integer arr[] = new Integer[n];
		for(int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.sort(arr);
		
		for(int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
		}
	}

}
