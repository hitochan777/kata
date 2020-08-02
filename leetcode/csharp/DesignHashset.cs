public class MyHashSet {
	public const int SIZE = 10000;
	public int[] list = new int[SIZE];
    /** Initialize your data structure here. */
    public MyHashSet() {
		for (int i = 0; i < list.Length; i++) {
			list[i] = -1;
		}
	}
    
    public void Add(int key) {
        if (Contains(key)) {
            return;
        }
		int p = key % SIZE;
        while(list[p] != -1) {
			p = (p + 1) % SIZE;
		}
		list[p] = key;
    }
    
    private int FindIndex(int key) {
		int p = key % SIZE;
		int count = 0;
        while(list[p] != -1 && count <= SIZE) {
            if (list[p] == key) {
                return p;
            }
			p = (p + 1) % SIZE;
			count++;
		}        
        return -1;
    }
    
    public void Remove(int key) {
		int index = FindIndex(key);
        if (index != -1) {
            list[index] = -1;
        }
    }
    
    public bool Contains(int key) {
		int index = FindIndex(key);
        return index != -1;
    }
}
