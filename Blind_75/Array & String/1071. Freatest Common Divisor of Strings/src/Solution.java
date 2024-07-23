class Solution {

    public String gcdOfStrings(String str1, String str2) {

        if ((str1 + str2).equals(str2 + str1)) { // Verificar se a concatenação de duas strings em ordens diferentes
                                                 // resulta na mesma coisa
            int tam1 = str1.length();
            int tam2 = str2.length();
            int mdc = gcd(tam1, tam2); // cálculo do máximo denominador comum

            if (str1.length() > 0) {
                return str1.substring(0, mdc); // substring é um metodo da classe string que retorna uma nova string que
                                               // é um subconjunto da string original (começa em 0 até mdc)
            } else {
                return str2.substring(0, mdc);
            }
        } else {
            return "";
        }

    }

    static int gcd(int x, int y) { // essa função irá calcular o mdc em si, é recursiva e continua abstraindo até 0
        if (x == 0)
            return y;

        if (y == 0)
            return x;

        if (x == y)
            return x;

        if (x > y) {
            return gcd(x - y, y);
        }

        return gcd(x, y - x);
    }
}