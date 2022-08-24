package silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;



public class Exception {
	
	public static void main(String[] args) throws IOException {
		var bf = new BufferedReader(new InputStreamReader(System.in));
		int n[] = new int[2];
		for(int i = 0; i < n.length; i++) {
			n[i] = Integer.parseInt(bf.readLine().split(" ")[i]);
		}
		int map[][] = new int[n[0]][n[1]];
	}
}
