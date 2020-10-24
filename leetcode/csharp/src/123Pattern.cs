using System.Collections.Generic;

namespace src {
    class Find132Pattern {
        public bool Solve(int[] nums) {
            var stack = new Stack<(int, int)>();
            foreach (var num in nums) {
                if (stack.Count == 0 || num < stack.Peek().Item1) {
                    stack.Push((num, num));
                }
                else {
                    var min  = stack.Peek().Item1;
                    while (stack.Count > 0 && stack.Peek().Item2 < num) {
                        stack.Pop();
                    }
                    (int, int)? top = null;
                    if (stack.Count > 0) {
                        top = stack.Peek();
                    } 
                    if (top?.Item1 < num && top?.Item2 > num) {
                        return true;
                    }
                    else {
                        stack.Push((min, num));
                    }
                }
            }
            return false;
        }
    }
}