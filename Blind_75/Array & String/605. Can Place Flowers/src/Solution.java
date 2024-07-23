class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int lenghtFlowebed = flowerbed.length;

        for (int i = 0; i < lenghtFlowebed; i++) {
            if (flowerbed[i] == 0) {
                boolean emptyL = (i == 0) || (flowerbed[i - 1] == 0);
                boolean emptyR = (i == lenghtFlowebed - 1) || (flowerbed[i + 1] == 0);

                if (emptyL && emptyR) {
                    flowerbed[i] = 1;
                    n--;
                    if (n == 0) {
                        return true;
                    }
                }
            }

            // System.out.printf(flowerbed[i] + "");

        }

        // System.out.println("");

        return n <= 0;
    }
}