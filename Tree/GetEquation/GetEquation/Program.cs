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
        static void Main(string[] args)
        {
            Console.Write("Введите n: ");


            int n;
            int.TryParse(Console.ReadLine(), out n);

            string[] ans = new string[0];

            Tree[] AlreadyCounted = new Tree[1] { new Tree(new[] { true, true, true }) }; // массив деревьев с n листьями
                                                                                          // (n - изменяется) для который мы уже составил системы
            Tree[] Counting = new Tree[0]; // массив деревьев с n + 1 листьями (n - изменяется)
                                           // для который мы ещё не составили системы

            for (int i = 3; i <= n; i++) // цикл по размерности массива Counting
                                         // (то есть в данный момент строим все деревья с i листьями )
            {
                for (int j = 0; j < AlreadyCounted.Length; j++) // цикл перебирает все деревья с i - 1 листьями
                                                                // (которые вес уже построены и лежат в массиве AlreadyCounted),
                                                                // чтобы к каждому из них добавить по листу всевозможными способами
                {
                    Tree[] newTrees = new Tree[0]; // массив со всевозможными деревьями с i листьями,
                                                   // которые можно получить из дерева AlreadyCounted[j]
                    Tree.AddLeaf(0, AlreadyCounted[j], ref newTrees);
                    Array.Resize(ref Counting, Counting.Length + newTrees.Length);
                    for (int k = Counting.Length - newTrees.Length;
                            k < Counting.Length;
                            k++) // добавляем все полученные деревья с i в массив Counting
                    {
                        Counting[k] = newTrees[k - Counting.Length + newTrees.Length];
                    }
                }

                AlreadyCounted = (Tree[])Counting.Clone();
                Counting = new Tree[0];
            }

            using (StreamWriter fs = new StreamWriter("../../../../../input_files/short_equations_" + n + ".txt", false, System.Text.Encoding.Default))
            {

                Console.WriteLine(AlreadyCounted.Length);
                for (int j = 0; j < AlreadyCounted.Length; j++)
                {
                    // проверка на повторяемость (нужна для того чтобы в файле Вольфрама не было
                    // одинаковых графов)
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
                        Tree.GetSystem(AlreadyCounted[j], out string systemX, out string systemXY);

                        fs.WriteLine(AlreadyCounted[j].WolframForm());
                        fs.WriteLine(systemXY);
                        //fs.WriteLine(AlreadyCounted[j].WolframForm());
                        //fs.WriteLine(systemX);
                        //Console.WriteLine();
                    }
                }
            }


        }
    }
}
