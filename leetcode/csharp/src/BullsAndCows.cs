using System;
using System.Collections.Generic;

namespace BullsAndCows
{
    public static class DictionaryExtensions
    {
        public static TV GetOrDefault<TK, TV>(this Dictionary<TK, TV> dic, TK key, TV defaultValue = default) => dic.TryGetValue(key, out var result) ? result : defaultValue;
    }
    public class Solution
    {
        public string GetHint(string secret, string guess)
        {
            var smap = new Dictionary<char, int>();
            var gmap = new Dictionary<char, int>();
            int aCount = 0, bCount = 0;
            for (int i = 0; i < secret.Length; i++)
            {
                if (guess[i] == secret[i])
                {
                    aCount++;
                } else
                {
                    smap[secret[i]] = smap.GetOrDefault(secret[i]) + 1;
                    gmap[guess[i]] = gmap.GetOrDefault(guess[i]) + 1;
                }
            }
            foreach (var (val, count) in gmap)
            {
                bCount += Math.Min(smap.GetOrDefault(val), count); 
            }
            return $"{aCount}A{bCount}B";

        }
    }
}
