package NYPC;

import java.util.Arrays;
import java.util.Scanner;

public class 모기 {
	static int map[][];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(); 
		int m = sc.nextInt(); 
	
		map = new int[n][n];
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				map[i][j] = sc.nextInt();
			}
		}
		
		int max = 0, temp = 0;
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map.length; j++) {

				temp = map[i][j];
				for(int k=1; k<=m; k++) {
					if(j-k>=0) temp+=map[i][j-k];
					if(j+k<n) temp+=map[i][j+k];
				}
				
				for(int k=1; k<=m; k++) {
					if(i-k>=0) temp+=map[i-k][j];
					if(i+k<n) temp+=map[i+k][j];
				}
				max = temp > max ? temp : max; 
				
				temp = map[i][j];
				for(int k=1; k<=m; k++) {
					if(i-k>=0 && j-k>=0) temp+=map[i-k][j-k];
					if(i-k>=0 && j+k<n) temp+=map[i-k][j+k];
				}
				
				for(int k=1; k<=m; k++) {
					if(i+k<n && j-k>=0) temp+=map[i+k][j-k];
					if(i+k<n && j+k<n) temp+=map[i+k][j+k];
				}
				
				
				max = temp > max ? temp : max;
				temp = 0;
			}
		}
		System.out.println(max); 
	}
}