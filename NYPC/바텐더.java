package NYPC;

import java.util.Scanner;

public class 바텐더 {
	
	static int[] a;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		a = new int[n];
		
		int mx = 0;
		for(int i = 0; i < a.length; i++) {
			a[i] = sc.nextInt();
			mx = mx < a[i] ? a[i] : mx;
//			mx = Math.max(mx, a[i]);
		}
		
		//(1,2,4) ���� ���� ä��
		int cnt = 0;
		for(int i = 0; i < a.length; i++) {
			int t = (mx-a[i])/7;
			cnt += t*3;
			a[i] += 7*t;
		}
		
		//1,2,4 ä��� ���
		int _4=0, _2=0, _1=0;
		for(int i = 0; i < a.length; i++) {
			_4 += (mx-a[i])/4;
			_2 += (mx-a[i])/2;
			_1 += (mx-a[i]);
		}
		
		//1,2,4 ä��� �켱���� �ݿ� �� ����
		_1 -= _2*2;
		_2 -= _4*2;
		
		//_4, _2, _1�� �ִ�
		int arr[] = {_4, _2, _1};
		int maxIdx = 0;
		for(int i=0; i<3; i++) {
			if(arr[maxIdx] < arr[i]) {
				maxIdx = i;
			}
		}

		System.out.println(cnt + arr[maxIdx]*3 - maxIdx);
	}
}
