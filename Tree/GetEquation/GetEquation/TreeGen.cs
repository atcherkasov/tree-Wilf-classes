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
