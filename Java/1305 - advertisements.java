import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int L = Integer.parseInt(sc.nextLine());
        String ad = sc.nextLine();

        // KMP
        int[] pi = new int[L];
        int j = 0;
        for (int i = 1; i < L; i++) {
            while (j > 0 && ad.charAt(i) != ad.charAt(j)) {
                j = pi[j - 1];
            }
            if (ad.charAt(i) == ad.charAt(j)) {
                j++;
                pi[i] = j;
            }
        }

        System.out.println(L - pi[L - 1]);
    }
}