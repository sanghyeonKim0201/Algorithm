package bronze;

import java.util.Scanner;

public class Baek_3052_OK {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		boolean check[] = new boolean[42];
		for (int i = 0; i < 10; i++) {
			check[sc.nextInt() % 42] = true;
		}
		var cnt = 0;
		for(var c : check) {
			if(c == true) {
				cnt++;
			}
		}
		System.out.println(cnt);
	}
}
