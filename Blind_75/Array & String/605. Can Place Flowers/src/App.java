import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        Solution solution = new Solution();

        //num de rodadas
        int flores = sc.nextInt();
        int[] flowerbed = new int[flores];
        

        for(int i = 0; i < flores; i++){
            flowerbed[i] = sc.nextInt();
        }

        int n = sc.nextInt();

        System.out.println(solution.canPlaceFlowers(flowerbed, n));
    }
}
