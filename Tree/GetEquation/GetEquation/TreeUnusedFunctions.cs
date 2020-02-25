using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GetEquation
{
    partial class Tree
    {
        public static int cur_level = 0;


        public static void Elongation(int new_level)
        {
            int index = XVarialables.Length;
            //Array.Resize(ref XYVarialables, new_level * 24 + 1);
            Array.Resize(ref XVarialables, new_level * 24 + 1);


            int level = cur_level + 1;

            while (level < new_level + 1)
            {
                for (int i = 0; i < 24; i++)
                {
                    XVarialables[index] = letters[i] + level.ToString();
                    //XYVarialables[index] = letters[i] + level.ToString();
                    index++;
                }
                level++;
            }
            cur_level = new_level;
        }


        public static string[] letters = new string[24]
        {
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "z"
        };


        //public static string[] XVarialables = new string[]
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


        //public static string[] XYVarialables = new string[]
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

    }
}
