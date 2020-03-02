using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GetEquation
{
    partial class Tree
    {
        /// <summary>
        /// Функция используется в методе Cut
        /// находит 2 в максимально большой степени, строго меньшее n + 2
        /// </summary>
        /// <param name="n"></param>
        /// <returns></returns>
        static int DoublePow(int n)
        {
            int ans = 1;
            while (ans < 1000 * 1000 && ans * 2 - 2 < n)
            {
                ans *= 2;
            }

            return ans;
        }


        /// <summary>
        /// Функция используется в методе Cut
        /// строит левое поддерево
        /// </summary>
        /// <param name="v"></param>
        /// <param name="bigTree"></param>
        /// <param name="subtree"></param>
        public static void dfs(int v, Tree bigTree, ref Tree subtree)
        {
            if (bigTree[v])
            {
                bigTree[v] = false;
                subtree[v - 1 - (DoublePow(v) - 2) / 2] = true; // новые координаты левого сына в уже отрезанном поддереве
                if (2 * v + 2 < bigTree.ArrayForm.Length)
                {
                    dfs(2 * v + 1, bigTree, ref subtree);
                    dfs(2 * v + 2, bigTree, ref subtree);
                }
            }
            return;
        }


        /// <summary>
        /// разрезаем данное дерево bigTree на два поддерева leftTree и rightTree
        /// </summary>
        /// <param name="bigTree"></param>
        /// <param name="leftTree"></param>
        /// <param name="rightTree"></param>
        public static void Cut(Tree bigTree, out Tree leftTree, out Tree rightTree)
        {
            leftTree = new Tree(new bool[bigTree.ArrayForm.Length / 2]);
            rightTree = new Tree(new bool[bigTree.ArrayForm.Length / 2]);
            Tree ProcessedTree = new Tree((bool[])bigTree.ArrayForm.Clone());
            dfs(1, ProcessedTree, ref leftTree);
            Array.ConvertAll(rightTree.ArrayForm, y => false);
            for (int i = 2; i < ProcessedTree.ArrayForm.Length; i++)
            {
                if (ProcessedTree[i])
                {
                    rightTree[i - DoublePow(i)] = true; // новые координаты правого сына в уже отрезанном поддереве
                }
            }
            return;
        }

        /// <summary>
        /// Нужно для генерации деревьев в составлении системы уранений и всё !
        /// В генерации деревьев эта функия не учавствует !!!
        /// добавляет новое дерево если оно раньше не было получено и бездействует в противном случае
        /// </summary>
        /// <param name="Stack">массив уже полученыых деревьев (путём постепенного составления уравнений системы)</param>
        /// <param name="A">дерево которые мы проверяем на налчие в этом массиве</param>
        /// <param name="ownNum">это номер который будет у дерева после выполнения этого метода</param>
        public static void Add(ref Tree[] Stack, Tree A, out int ownNum)
        {
            bool haveA = false;
            ownNum = -1;
            for (int i = 0; i < Stack.Length; i++)
            {
                if (IsSame(Stack[i], A))
                {
                    haveA = true;
                    ownNum = i;
                    break;
                }
            }
            if (!haveA)
            {
                Array.Resize(ref Stack, Stack.Length + 1);
                Stack[Stack.Length - 1] = new Tree((bool[])A.ArrayForm.Clone());
                ownNum = Stack.Length - 1;
            }
            return;
        }


        /// <summary>
        /// функция объединения двух деревьев a и b
        /// </summary>
        /// <param name="a"></param>
        /// <param name="b"></param>
        /// <returns></returns>
        public static Tree Join(Tree a, Tree b)
        {
            Array.Resize(ref a.ArrayForm, Math.Max(a.ArrayForm.Length, b.ArrayForm.Length));
            Array.Resize(ref b.ArrayForm, a.ArrayForm.Length);
            for (int i = 0; i < a.ArrayForm.Length; i++)
            {
                if (b[i])
                {
                    a[i] = true;
                }
            }
            return a;
        }


        /// <summary>
        /// возвращает строку, которая при запуске в Wolfram Mathematica рисует заданное дерево
        /// </summary>
        /// <param name="ArrayForm"></param>
        /// <returns></returns>
        public string WolframForm()
        {
            string ans = "Graph[{";
            for (int i = 1; i < this.ArrayForm.Length; i++)
            {
                if (this[i])
                {
                    ans += $"{(i - 1) / 2}->{i},";
                }
            }
            if (ans == "Graph[{")
            {
                ans += "0->0}]";
            }
            else
            {
                ans = ans.Substring(0, ans.Length - 1) + "}]";
            }
            return ans;
        }


        /// <summary>
        /// метод строящий системы уравнений для заданного дерева
        /// </summary>
        /// <param name="tree"></param>
        /// <returns></returns>
        public static void GetSystem(Tree givenTree, out string system)
        {
            for (int i = 0; i < 200; i++)
            {
                XVarialables[i] = i.ToString();
                //XYVarialables[i] = i.ToString();
            }

            Tree tree = new Tree((bool[])(givenTree.ArrayForm).Clone());
            Cut(tree, out Tree Tl, out Tree Tr);
            Tree[] Stack = new Tree[] { new Tree(new[] { true }), new Tree(new[] { true, true, true }) };
            int cnt = 1;
            system = "";
            while (cnt < Stack.Length)
            {
                // получаем так называемые Pl и Pr
                Cut(Stack[cnt], out Tree Pl, out Tree Pr);

                // добавляем их в массив переменных
                Add(ref Stack, Pl, out int num1);
                Add(ref Stack, Pr, out int num2);

                Tree PlJoinTl = Join(Pl, Tl); // получаем объеденение Pl и Tl
                Tree PrJoinTr = Join(Pr, Tr); // получаем объеденение Pr и Tr

                // добавляем их в массив переменных
                Add(ref Stack, PlJoinTl, out int num3);
                Add(ref Stack, PrJoinTr, out int num4);
                
                while (cnt >= XVarialables.Length || num1 >= XVarialables.Length || num2 >= XVarialables.Length ||
                    num3 >= XVarialables.Length || num4 >= XVarialables.Length)
                {
                    Array.Resize(ref XVarialables, XVarialables.Length * 2);
                    //Array.Resize(ref XYVarialables, XYVarialables.Length * 2);
                    for (int i = XVarialables.Length / 2; i < XVarialables.Length; i++)
                    {
                        XVarialables[i] = i.ToString();
                        //XYVarialables[i] = i.ToString();
                    }
                }
                //system += $"{XYVarialables[cnt]} {XYVarialables[num1]} {XYVarialables[num2]} {XYVarialables[num3]} {XYVarialables[num4]}\n";
                system += $"{XVarialables[cnt]} {XVarialables[num1]} {XVarialables[num2]} {XVarialables[num3]} {XVarialables[num4]}\n";
                cnt++;

            }
        }
    }
}
