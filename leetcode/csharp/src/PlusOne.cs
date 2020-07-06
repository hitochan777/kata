using System.Collections.Generic;

namespace Kata.PlusOne
{
    public class Solution
    {
        public int[] PlusOne(int[] digits)
        {
            int i = digits.Length - 1;
            for (; i >= 0 && digits[i] == 9; i--) { }
            if (i >= 0)
            {
                digits[i]++;
                for (int j = digits.Length - 1; j > i; j--)
                {
                    digits[j] = 0;
                }
            }
            else
            {
                var li = new List<int> { 1 };
                for (int j = 0; j < digits.Length; j++)
                {
                    li.Add(0);
                }
                digits = li.ToArray();
            }
            return digits;
        }
    }
}