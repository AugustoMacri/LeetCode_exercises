public class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder solution = new StringBuilder();

        if (word1.length() > word2.length()) {
            for (int i = 0; i < word1.length(); i++) {
                // System.out.println(word1.charAt(i));
                solution.append(word1.charAt(i));
                if (i < word2.length()) {
                    // System.out.println(word2.charAt(i));
                    solution.append(word2.charAt(i));
                }
            }
        } else if (word2.length() > word1.length()) {
            for (int i = 0; i < word2.length(); i++) {
                if (i < word1.length()) {
                    solution.append(word1.charAt(i));
                    solution.append(word2.charAt(i));
                }else{
                    solution.append(word2.charAt(i));
                }
            }
        } else {
            for (int i = 0; i < word1.length(); i++) {
                solution.append(word1.charAt(i));
                solution.append(word2.charAt(i));
            }
        }

        return solution.toString();
    }

}

/*
Another solution from user yashpalgirase692:
    class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb= new StringBuilder();
        int n1=word1.length();
        int n2 = word2.length();
        int i = 0;
        while (i<n1 || i<n2){
            if(i<n1)
                sb.append(word1.charAt(i));
            if(i<n2)
            sb.append(word2.charAt(i));
            i++;
        }
        return sb.toString();
    }
}
 */
