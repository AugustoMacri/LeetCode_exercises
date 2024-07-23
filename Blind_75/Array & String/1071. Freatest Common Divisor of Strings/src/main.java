import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        String str1 = sc.nextLine();
        String str2 = sc.nextLine();

        System.out.println(sol.gcdOfStrings(str1, str2));
    }
}
