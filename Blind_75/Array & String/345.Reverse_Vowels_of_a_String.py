class Solution(object):
    def reverseVowels(self, string):

        # Primeiro vamos convertr a string em uma lista pq o python não deixa modificar a string

        string = list(string)

        # Criar uma lista para armazenar as vogais
        vogais = []

        for char in string:

            if char.lower() in "aeiou":
                vogais.append(char)

        # Agora é substituir, podemos usar o -1 para percorrer o array ao contrário
        cont = -1
        for i in range(len(string)):

            if string[i].lower() in "aeiou":

                string[i] = vogais[cont]

                cont -= 1

        # Agora precisa devolver a lista em formato de string de novo
        return "".join(string)


if __name__ == "__main__":
    string = input()
    solution = Solution()
    print(solution.reverseVowels(string))
