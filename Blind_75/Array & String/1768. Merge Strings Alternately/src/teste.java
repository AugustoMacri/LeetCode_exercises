import java.util.Scanner;

public class teste {
    public static void main(String[] args) {
        Solution sol = new Solution();

        Scanner sc = new Scanner(System.in);
        String word1 = sc.nextLine();
        String word2 = sc.nextLine();

        System.out.println(sol.mergeAlternately(word1, word2));


    }
}
