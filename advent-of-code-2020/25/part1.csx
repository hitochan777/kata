public static class Transformer
{
	public static long TransformOnce(long current, long subject)
	{
		current *= subject;
		return current % 20201227;
	}

	public static long FindLoopSize(long publicKey)
	{
		var current = 1L;
		var loopSize = 0;
		while (current != publicKey)
		{
			current = TransformOnce(current, 7);
			loopSize++;
		}
		return loopSize;
	}

	public static long Transform(long loopSize, long subject)
	{
		var value = 1L;
		for (var i = 0; i < loopSize; i++)
		{
			value = TransformOnce(value, subject);
		}
		return value;
	}
}

var cardPublicKey = 2069194;
// var cardPublicKey = 5764801;
var doorPublicKey = 16426071;
// var doorPublicKey = 17807724;
var cardLoopSize = Transformer.FindLoopSize(cardPublicKey);
// var doorLoopSize = Transformer.FindLoopSize(doorPublicKey);
Console.WriteLine(cardLoopSize);
var encryptionKey = Transformer.Transform(cardLoopSize, doorPublicKey);
Console.WriteLine(encryptionKey);