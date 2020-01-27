using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace HypothesTest
{
    class Program
    {
        static void Main(string[] args)
        {
            //Name = openFileDialog1.FileName;
            //string inPut = File.ReadAllText(Name);

            string path = "../../../../../series_9_21.txt";
            string[] commands = { };

            if (File.Exists(path))
                commands = File.ReadAllLines(path);


            // массив строк-комманд полученных из заданного файла

            string[] SystemX = new string[0] { };
            string[] SystemXY = new string[0] { };



            for (int i = 0; i < commands.Length; i++)
            {
                if (i % 4 == 1)
                {
                    Array.Resize(ref SystemXY, SystemXY.Length + 1);
                    SystemXY[SystemXY.Length - 1] = commands[i];
                }
                if (i % 4 == 2)
                {
                    Array.Resize(ref SystemX, SystemX.Length + 1);
                    SystemX[SystemX.Length - 1] = commands[i];
                }
            }



            int[][] XGroups = new int[0][] { };  // массив массивов в котормом каждый массив содержит
                                                 // в себе те и только те функйии по X которые равны

            int[][] XYGroups = new int[0][] { }; // массив массивов в котормом каждый массив содержит
                                                 // в себе те и только те функйии по XY которые равны

            bool[] usedX = new bool[] { }; // массим булов. Каждый бул соответствует по номеру функции
                                           // из массива SystemX и означает закинули ли мы уже эту функцию
                                           // в какуюто группу из XGroups или нет
            Array.Resize(ref usedX, SystemX.Length);

            bool[] usedXY = new bool[] { }; // массим булов. Каждый бул соответствует по номеру функции
                                            // из массива SystemXY и означает закинули ли мы уже эту 
                                            // функцию в какуюто группу из XYGroups или нет
            Array.Resize(ref usedXY, SystemXY.Length);


            // построение XGroups
            for (int i = 0; i < SystemX.Length; i++)
            {
                if (!usedX[i])
                {
                    Array.Resize(ref XGroups, XGroups.Length + 1);
                    XGroups[XGroups.Length - 1] = new int[1] { i };
                    for (int j = i + 1; j < SystemX.Length; j++)
                    {
                        if (!usedX[j] && SystemX[i] == SystemX[j])
                        {
                            usedX[j] = true;
                            Array.Resize(ref XGroups[XGroups.Length - 1],
                                XGroups[XGroups.Length - 1].Length + 1);
                            XGroups[XGroups.Length - 1][XGroups[XGroups.Length - 1].Length - 1] = j;
                        }
                    }

                    Array.ForEach(XGroups[XGroups.Length - 1], y => Console.Write(y + " "));
                    Console.WriteLine();
                }
            }

            Console.WriteLine("wwww");
            //if (Gfunction.Checked) goto AvoidanceCase;

            // построение XYGroups
            for (int i = 0; i < SystemXY.Length; i++)
            {
                if (!usedXY[i])
                {
                    Array.Resize(ref XYGroups, XYGroups.Length + 1);
                    XYGroups[XYGroups.Length - 1] = new int[1] { i };
                    for (int j = i + 1; j < SystemXY.Length; j++)
                    {
                        if (!usedXY[j] && SystemXY[i] == SystemXY[j])
                        {
                            usedXY[j] = true;
                            Array.Resize(ref XYGroups[XYGroups.Length - 1],
                                XYGroups[XYGroups.Length - 1].Length + 1);
                            XYGroups[XYGroups.Length - 1][XYGroups[XYGroups.Length - 1].Length - 1] = j;
                        }
                    }

                    Array.ForEach(XYGroups[XYGroups.Length - 1], y => Console.Write(y + " "));
                    Console.WriteLine();
                }
            }

            string ans = "";

            //просто проверяем совпадают ли 2 массива массивов XGroups и XYGroups
            if (XGroups.Length != XYGroups.Length)
            {
                Console.WriteLine($"Rouland hypothesis is FALSE for given input\n");
                Console.ReadLine();
                return;
            }
            for (int i = XGroups.Length - 1; i > -1; i--)
            {
                if (XGroups[i].Length != XYGroups[i].Length)
                {
                    Console.WriteLine($"Rouland hypothesis is FALSE for given input\n");
                    Console.ReadLine();
                    //return;
                }

                for (int j = 0; j < XGroups[i].Length; j++)
                {
                    if (XYGroups[i][j] != XGroups[i][j])
                    {
                        Console.WriteLine($"Rouland hypothesis is FALSE for given input\n");
                        //return;
                        ///////////////////////////////////////////
                    }
                }

            }

            ans += $"\nRouland hypothesis is TRUE for given input\n\n" +
                                    $"Количество различных функций: {XGroups.Length}\n" +
                                    $"Количество функций в группах:\n";
            int sum = 0;
            for (int i = XGroups.Length - 1; i > -1; i--)
            {
                sum += XGroups[i].Length;
                ans += XGroups[i].Length + " ";
            }
            ans += $"\nВсего деревьев: {sum}";
            if (sum != SystemX.Length)
                Console.WriteLine("Сумма групп размеров НЕ совпала с данным количеством \n" +
                                "дереавьев во входном файле");
            Console.WriteLine(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
            Console.WriteLine(ans);
            string a = Console.ReadLine();

            //AvoidanceCase:
            //    verdictTextBox.Text += $"Количество различных функций: {XGroups.Length}\n" +
            //                            $"Количество функций в группах:\n";
            //    sum = 0;
            //    for (int i = XGroups.Length - 1; i > -1; i--)
            //    {
            //        sum += XGroups[i].Length;
            //        verdictTextBox.Text += XGroups[i].Length + " ";
            //    }
            //    verdictTextBox.Text += $"\nВсего деревьев: {sum}";
            //    if (sum != SystemX.Length)
            //        MessageBox.Show("Сумма групп размеров НЕ совпала с данным количеством \n" +
            //                        "дереавьев во входном файле");

        }
    }
}
