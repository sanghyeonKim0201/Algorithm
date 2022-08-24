package bronze;

public class Baek_15596_OK {
	
	long sum(int[]a) {
		long l = 0;
		for(int i = 0; i < a.length; i++) {
			l += a[i];
		}
		return l;
	}
}
