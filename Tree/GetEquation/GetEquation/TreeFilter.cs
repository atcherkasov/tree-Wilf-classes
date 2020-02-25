using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GetEquation
{
    partial class TreeInit
    {
        /// <summary>
        /// проверяет два дерева a и b на равенство 
        /// </summary>
        /// <param name="a"></param>
        /// <param name="b"></param>
        /// <returns></returns>
        public static bool IsSame(TreeInit a, TreeInit b)
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
        /// проверяет являются ли два данных дерева симметричными
        /// </summary>
        /// <param name="a"></param>
        /// <param name="b"></param>
        /// <returns></returns>
        public static bool IsSymmetric(TreeInit a, TreeInit b)
        {
            if (a.ArrayForm.Length != b.ArrayForm.Length)
                return false;

            bool ans = true;
            // будем проверять на перевёрнутые массивы в порядке ёлочки
            int left = 0;
            int right = 0;
            while (right <= a.ArrayForm.Length - 1)
            {
                for (int i = left; i <= right; i++)
                {
                    if (a.ArrayForm[i] != b.ArrayForm[right - i + left])
                    {
                        ans = false;
                        break;
                    }
                }
                if (!ans)
                    break;
                left = 2 * left + 1;
                right = 2 * right + 2;
            }
            return ans;
        }
    }
}
