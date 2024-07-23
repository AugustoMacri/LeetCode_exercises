import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> resp;

        resp = new ArrayList<Boolean>();

        int val = -1;
        int ii = 0;

        // Pegando o tamanho do vetor
        for (int i : candies) {
            ii++;
        }

        // Pegando o maior valor do vetor
        for (int j = 0; j < ii; j++) {
            int val2 = candies[j];

            if (val2 > val) {
                val = val2;
            }
        }

        for (int k = 0; k < ii; k++) {
            if ((candies[k] + extraCandies) >= val) {
                resp.add(true);
            } else {
                resp.add(false);
            }
        }

        return resp;
    }
}