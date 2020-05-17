using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace GetEquation
{
    class Program
    {
        static string Gen_next(string s)
        {
            int n = (int)s.Length;
            string ans = "no";
            for (int i = n - 1, depth = 0; i >= 0; --i)
            {
                if (s[i] == '(')
                    --depth;
                else
                    ++depth;
                if (s[i] == '(' && depth > 0)
                {
                    --depth;
                    int open = (n - i - 1 - depth) / 2;
                    int close = n - i - 1 - open;
                    ans = s.Substring(0, i) + ')' + new string('(', open) + new string(')', close);
                    break;
                }
            }          
            return ans;
        }

        static int close_bracket_index_for_first_break(string brackets)
        {
            int count_opened = 1;
            for (int i = 1; i < brackets.Length; i++)
            {
                if (brackets[i] == '(')
                    count_opened++;
                else
                    count_opened--;
                if (count_opened == 0)
                    return i;
            }
            return -2;
        }
         

        static void Display(ref bool[] tree, string brackets, int curr)
        {
            tree[curr] = true;
            if (brackets == "")
                return;
            int index = close_bracket_index_for_first_break(brackets);

            Display(ref tree, brackets.Substring(1, index - 1), 2 * curr + 1);
            Display(ref tree, brackets.Substring(index + 1, brackets.Length - index - 1), 2 * curr + 2);

        }

        // числа Каталана. Поседний элемент массива - ответ на leaves = 20
        static int[] CatalanNumbers = {-1, 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 
            58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190};
        // 6564120420, 24466267020, 91482563640, 343059613650, 1289904147324, 4861946401452

        static void Main(string[] args)
        {
            Console.Write("Введите айайа n: ");

            int n;
            int.TryParse(Console.ReadLine(), out n);

            Tree[] AlreadyCounted = { }; 
            Array.Resize(ref AlreadyCounted, CatalanNumbers[n]);

            string curr_seq = "";
            for (int i = 0; i < n - 1; i++)
                curr_seq += '(';
            for (int i = 0; i < n - 1; i++)
                curr_seq += ')';

            int ind = 0;
            while (curr_seq != "no")
            {
                //Console.WriteLine(curr_seq);
                bool[] tree = new bool[(int)Math.Pow(2, n) - 1];
                Display(ref tree, curr_seq, 0);
                AlreadyCounted[ind] = new Tree(tree);
                curr_seq = Gen_next(curr_seq);
                ind++;
            }


            using (StreamWriter fs = new StreamWriter("../../../../../../degug_" + n + ".txt", false, System.Text.Encoding.Default))
            {
                int cnt = 0;
                for (int j = 0; j < AlreadyCounted.Length; j++)
                {
                    // проверка на повторяемость (нужна для того чтобы в файле Вольфрама не было
                    // одинаковых графов)
                    Console.WriteLine((100 * (double)j) / AlreadyCounted.Length + "%");
                    bool isRepeated = false;
                    for (int k = 0; k < j; k++)
                    {
                        if (Tree.IsSame(AlreadyCounted[k], AlreadyCounted[j]) || Tree.IsSymmetric(AlreadyCounted[k], AlreadyCounted[j]))
                        {
                            isRepeated = true;
                            break;
                        }
                    }

                    if (!isRepeated)
                    {
                        Tree.GetSystem(AlreadyCounted[j], out string system);

                        fs.WriteLine(AlreadyCounted[j].WolframForm());
                        fs.WriteLine(system);
                        cnt++;
                        //fs.WriteLine(AlreadyCounted[j].WolframForm());
                        //fs.WriteLine(systemX);
                        //Console.WriteLine();
                    }
                   
                }
                Console.WriteLine($"cnt: {cnt}");
            }
            Console.ReadLine();


        }
    }
}
