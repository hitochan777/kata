
var lastIndices = new Dictionary<int, int>{};
var spokenNums = Console.ReadLine().Split(",").Select(n => int.Parse(n)).ToList();
for (var i = 0; i < spokenNums.Count - 1; i++) {
    lastIndices[spokenNums[i]] = i + 1;
}
var lastSpoken = spokenNums[^1];
while (spokenNums.Count < 30000000 ) {
    if (!lastIndices.ContainsKey(lastSpoken)) {
        spokenNums.Add(0);
    } else {
        spokenNums.Add(spokenNums.Count - lastIndices[lastSpoken]);
    }
    lastIndices[lastSpoken] = spokenNums.Count - 1;
    lastSpoken = spokenNums.Last();
}
Console.WriteLine(spokenNums[^1]);
