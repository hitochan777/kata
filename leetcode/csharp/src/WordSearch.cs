using System;
using System.Collections.Generic;

namespace WordSearch
{
    public class Solution
    {

        public bool Exist(char[][] board, int i, int j, string word, Dictionary<ValueTuple<int, int>, bool> visited)
        {
            if (word.Length == 0)
            {
                return true;
            }
            if (i < 0 || j < 0 || i >= board.Length || j >= board[0].Length)
            {
                return false;
            }
            if (visited.ContainsKey((i, j)))
            {
                return false;
            }
            if (board[i][j] != word[0])
            {
                return false;
            }
            visited[(i, j)] = true;
            var result = Exist(board, i - 1, j, word.Substring(1), visited) ||
                Exist(board, i + 1, j, word.Substring(1), visited) ||
                Exist(board, i, j - 1, word.Substring(1), visited) ||
                Exist(board, i, j + 1, word.Substring(1), visited);
            visited.Remove((i, j));
            return result;
        }
        public bool Exist(char[][] board, string word)
        {
            for (int i = 0; i < board.Length; i++)
            {
                for (int j = 0; j < board[i].Length; j++)
                {
                    var exist = Exist(board, i, j, word, new Dictionary<ValueTuple<int, int>, bool>());
                    if (exist)
                    {
                        return true;
                    }
                }
            }
            return false;
        }
    }
}

