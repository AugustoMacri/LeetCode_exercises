import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        Solution solution = new Solution();

        // escolhendo o numero de criancas
        int numKids = sc.nextInt();
        int[] candies = new int[numKids];

        // Criando vetor de crianças
        for (int i = 0; i < numKids; i++) {
            candies[i] = sc.nextInt();
        }

        // escolhendo o valor de doces extras
        int extraCandies = sc.nextInt();

        // chamando funcao
        System.out.println(solution.kidsWithCandies(candies, extraCandies));
    }
}
