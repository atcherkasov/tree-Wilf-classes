using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GetEquation
{
    class Tree
    {
        /// <summary>
        /// форма хранения дерева в массиве
        /// </summary>
        public bool[] ArrayForm;


        /// <summary>
        /// конструктор класса Tree от одного параметра (массива True и False)
        /// </summary>
        /// <param name="ArrayForm"></param>
        public Tree(bool[] ArrayForm)
        {
            this.ArrayForm = ArrayForm;
        }


        /// <summary>
        /// индексатор для удобства работы с полем массива ArrayForm
        /// </summary>
        /// <param name="i"></param>
        /// <returns></returns>
        public bool this[int i]
        {
            get => ArrayForm[i];
            set { ArrayForm[i] = value; }
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
        /// находит 2 в максимально большой степени, строго меньшее n + 2
        /// </summary>
        /// <param name="n"></param>
        /// <returns></returns>
        static int doublePow(int n)
        {
            int ans = 1;
            while (ans < 1000 * 1000 && ans * 2 - 2 < n)
            {
                ans *= 2;
            }

            return ans;
        }


        /// <summary>
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
                subtree[v - 1 - (doublePow(v) - 2) / 2] = true; // новые координаты левого сына в уже отрезанном поддереве
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
                    rightTree[i - doublePow(i)] = true; // новые координаты правого сына в уже отрезанном поддереве
                }
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
        /// проверяет два дерева a и b на равенство 
        /// </summary>
        /// <param name="a"></param>
        /// <param name="b"></param>
        /// <returns></returns>
        public static bool IsSame(Tree a, Tree b)
        {
            bool[] Arra = (bool[])a.ArrayForm.Clone();
            bool[] Arrb = (bool[])b.ArrayForm.Clone();
            Array.Resize(ref Arra, Math.Max(Arra.Length, Arrb.Length));
            Array.Resize(ref Arrb, Arra.Length);
            bool ans = true;
            for (int i = 0; i < Arra.Length; i++)
            {
                if (Arra[i] != Arrb[i])
                {
                    ans = false;
                    break;
                }
            }
            return ans;
        }


        /// <summary>
        /// добавляет новое дерево если оно раньше не было получено и бездействует в противном случае
        /// </summary>
        /// <param name="Stack">массив уже полученыых деревьев (путём потепенного составления уравнений системы)</param>
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
        /// массив доступных имён переменных (побочных деревьев)
        /// </summary>
        //public static string[] XYVarialables = new string[]
        //{
        //    "F",  "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1", "j1", "k1", "l1", "m1", "n1", "o1", "p1", "q1", "r1", "s1", "t1", "u1", "v1", "w1", "z1",
        //    "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2", "j2", "k2", "l2", "m2", "n2", "o2", "p2", "q2", "r2", "s2", "t2", "u2", "v2", "w2", "z2",
        //    "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3", "j3", "k3", "l3", "m3", "n3", "o3", "p3", "q3", "r3", "s3", "t3", "u3", "v3", "w3", "z3",
        //    //"a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "i4", "j4", "k4", "l4", "m4", "n4", "o4", "p4", "q4", "r4", "s4", "t4", "u4", "v4", "w4", "z4",
        //    //"a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "i5", "j5", "k5", "l5", "m5", "n5", "o5", "p5", "q5", "r5", "s5", "t5", "u5", "v5", "w5", "z5",
        //    //"a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "i6", "j6", "k6", "l6", "m6", "n6", "o6", "p6", "q6", "r6", "s6", "t6", "u6", "v6", "w6", "z6",
        //    //"a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "i7", "j7", "k7", "l7", "m7", "n7", "o7", "p7", "q7", "r7", "s7", "t7", "u7", "v7", "w7", "z7",
        //    //"a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "i8", "j8", "k8", "l8", "m8", "n8", "o8", "p8", "q8", "r8", "s8", "t8", "u8", "v8", "w8", "z8",
        //    //"a9", "b9", "c9", "d9", "e9", "f9", "g9", "h9", "i9", "j9", "k9", "l9", "m9", "n9", "o9", "p9", "q9", "r9", "s9", "t9", "u9", "v9", "w9", "z9",
        //    //"a10", "b10", "c10", "d10", "e10", "f10", "g10", "h10", "i10", "j10", "k10", "l10", "m10", "n10", "o10", "p10", "q10", "r10", "s10", "t10", "u10", "v10", "w10", "z10"
        //};

        public static string[] XYVarialables = new string[2000];
        //{
        //        "0",  "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "q1", "r1", "s1", "t1", "u1", "v1", "w1", "z1",
        //        "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2", "j2", "k2", "l2", "m2", "n2", "o2", "p2", "q2", "r2", "s2", "t2", "u2", "v2", "w2", "z2",
        //        "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3", "j3", "k3", "l3", "m3", "n3", "o3", "p3", "q3", "r3", "s3", "t3", "u3", "v3", "w3", "z3",
        //        "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "i4", "j4", "k4", "l4", "m4", "n4", "o4", "p4", "q4", "r4", "s4", "t4", "u4", "v4", "w4", "z4",
        //        "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "i5", "j5", "k5", "l5", "m5", "n5", "o5", "p5", "q5", "r5", "s5", "t5", "u5", "v5", "w5", "z5",
        //        "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "i6", "j6", "k6", "l6", "m6", "n6", "o6", "p6", "q6", "r6", "s6", "t6", "u6", "v6", "w6", "z6",
        //        "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "i7", "j7", "k7", "l7", "m7", "n7", "o7", "p7", "q7", "r7", "s7", "t7", "u7", "v7", "w7", "z7",
        //        "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "i8", "j8", "k8", "l8", "m8", "n8", "o8", "p8", "q8", "r8", "s8", "t8", "u8", "v8", "w8", "z8",
        //        "a9", "b9", "c9", "d9", "e9", "f9", "g9", "h9", "i9", "j9", "k9", "l9", "m9", "n9", "o9", "p9", "q9", "r9", "s9", "t9", "u9", "v9", "w9", "z9",
        //        "a10", "b10", "c10", "d10", "e10", "f10", "g10", "h10", "i10", "j10", "k10", "l10", "m10", "n10", "o10", "p10", "q10", "r10", "s10", "t10", "u10", "v10", "w10", "z10"
        //};

        public static string[] letters = new string[24]
        {
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "z"
        };

        /// <summary>
        /// массив доступных имён переменных (побочных деревьев)
        /// </summary>
        public static string[] XVarialables = new string[2000];
        //{
        //    //"G", "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1", "j1", "k1", "l1", "m1", "n1", "o1", "p1", "q1",
        //    //"r1", "s1", "t1", "u1", "v1", "w1", "z1",
        //    "0",  "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "q1", "r1", "s1", "t1", "u1", "v1", "w1", "z1",
        //    "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2", "j2", "k2", "l2", "m2", "n2", "o2", "p2", "q2", "r2",
        //    "s2", "t2", "u2", "v2", "w2", "z2",
        //    "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3", "j3", "k3", "l3", "m3", "n3", "o3", "p3", "q3", "r3",
        //    "s3", "t3", "u3", "v3", "w3", "z3",
        //    //"a4
        //};

        public static int cur_level = 0;

        public static void Elongation(int new_level)
        {
            int index = XYVarialables.Length;
            Array.Resize(ref XYVarialables, new_level * 24 + 1);
            Array.Resize(ref XVarialables, new_level * 24 + 1);


            int level = cur_level + 1;

            while (level < new_level + 1)
            {
                for (int i = 0; i < 24; i++)
                {
                    XVarialables[index] = letters[i] + level.ToString();
                    XYVarialables[index] = letters[i] + level.ToString();
                    index++;
                }
                level++;
            }
            cur_level = new_level;
        }

        /// <summary>
        /// метод строящий системы уравнений для заданного дерева
        /// </summary>
        /// <param name="tree"></param>
        /// <returns></returns>
        public static void GetSystem(Tree givenTree, out string systemX, out string systemXY)
        {
            //cur_level = 0;
            //XVarialables = new string[1] {"G"};
            //XYVarialables = new string[1] { "F" };

            //Elongation(1);
            for (int i = 0; i < 2000; i++)
            {
                XVarialables[i] = i.ToString();
                XYVarialables[i] = i.ToString();
            }

            //for (int i = 0; i < XYVarialables.Length; i++)
            //{
            //    Console.Write(XYVarialables[i] + " ");
            //}

            //Console.WriteLine();
            //for (int i = 0; i < XVarialables.Length; i++)
            //{
            //    Console.Write(XVarialables[i] + " ");
            //}
            Tree tree = new Tree((bool[])(givenTree.ArrayForm).Clone());
            Cut(tree, out Tree Tl, out Tree Tr);
            Tree[] Stack = new Tree[] { new Tree(new[] { true }), new Tree(new[] { true, true, true }) };
            int cnt = 1;
            systemXY = "";
            systemX = "";
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
                //if (cnt >= XYVarialables.Length || num1 >= XYVarialables.Length || num2 >= XYVarialables.Length ||
                //    num3 >= XYVarialables.Length || num4 >= XYVarialables.Length)
                //{
                //    int needable_level = Math.Max(Math.Max(num1, num2), Math.Max(num3, num4));
                //    needable_level = (Math.Max(needable_level, cnt) + 24) / 24;
                //    Elongation(needable_level * 2);
                //}
                systemXY += $"{XYVarialables[cnt]} {XYVarialables[num1]} {XYVarialables[num2]} {XYVarialables[num3]} {XYVarialables[num4]}\n";
                systemX += $"{XVarialables[cnt]} {XVarialables[num1]} {XVarialables[num2]} {XVarialables[num3]} {XVarialables[num4]}\n";
                cnt++;

            }
            //Console.WriteLine(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.");

            //for (int i = 0; i < XYVarialables.Length; i++)
            //{
            //    Console.Write(XYVarialables[i] + " ");
            //}
            //Console.WriteLine();

            //for (int i = 0; i < XVarialables.Length; i++)
            //{
            //    Console.Write(XVarialables[i] + " ");
            //}
            //Console.ReadLine();
            //Console.WriteLine();
            //Console.WriteLine();
            //Console.WriteLine();

        }


        /// <summary>
        /// по заданному дереву строит все возможные деревья полученные из него путём увеличения кол-ва листьев на 1
        /// </summary>
        /// <param name="v"></param>
        /// <param name="tree"></param>
        /// <param name="ans"></param>
        /// <returns></returns>
        public static Tree[] AddLeaf(int v, Tree tree, ref Tree[] ans)
        {
            if (2 * v + 2 >= tree.ArrayForm.Length)
            {
                Tree newTree = new Tree((bool[])tree.ArrayForm.Clone()); // новое дерево полученное из данного путём увеличения кол-ва листьев на 1
                Array.Resize(ref newTree.ArrayForm, newTree.ArrayForm.Length * 2 + 1);
                newTree.ArrayForm[2 * v + 1] = true;
                newTree.ArrayForm[2 * v + 2] = true;
                Array.Resize(ref ans, ans.Length + 1);
                ans[ans.Length - 1] = newTree;

            }
            else if (!tree[2 * v + 2])
            {
                Tree newTree = new Tree((bool[])tree.ArrayForm.Clone()); // новое дерево полученное из данного путём увеличения кол-ва листьев на 1
                newTree.ArrayForm[2 * v + 1] = true;
                newTree.ArrayForm[2 * v + 2] = true;
                Array.Resize(ref ans, ans.Length + 1);
                ans[ans.Length - 1] = newTree;
            }
            else
            {
                AddLeaf(2 * v + 1, tree, ref ans);
                AddLeaf(2 * v + 2, tree, ref ans);
            }
            return ans;
        }
    }
}
