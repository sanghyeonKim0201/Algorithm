package bronze;

import java.util.Scanner;

public class Baek_25304_OK {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int x = sc.nextInt(), n = sc.nextInt();
		int total = 0;
		for(int i = 0; i < n; i++) {
			int a = sc.nextInt(), b = sc.nextInt();
			total += (a * b);
		}
		System.out.println(total == x ? "Yes" : "No");
	}

}
