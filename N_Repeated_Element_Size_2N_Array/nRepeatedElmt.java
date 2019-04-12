class Solution {
    public int repeatedNTimes(int[] a) {
        int n = a.length / 2;
        HashMap<Integer, Integer> count = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < a.length; i++) {
            count.put(a[i], count.getOrDefault(a[i], 0) + 1);

            if(count.get(a[i]) == n) {
                return a[i];
            }
        }
        return -1;
    }
}
