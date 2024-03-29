package silver;

import java.io.*;
import java.util.*;

public class Baek_4673_OK {
    static boolean[] check = new boolean[10001];

    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i < 10001; i++) {
            if (!check[i]) d(i);
        }

        
        for (int i = 1; i < 10001; i++) {
            if (!check[i]) sb.append(i).append('\n');
        }
        System.out.println(sb);
    }

    // 재귀함수
    static int d(int n) {
        int sum = n;
        while (n != 0) {
            sum += n % 10;
            n /= 10;
        }
        if (sum < 10001) {
            check[sum] = true;
            d(sum);
        }
        return sum;
    }
}