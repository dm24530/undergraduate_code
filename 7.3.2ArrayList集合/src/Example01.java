import java.util.*;
public class Example01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	TreeMap map = new TreeMap(new MyComparator());
	map.put("1", "Jack");
	map.put("2", "Rose");
	map.put("3","Lucy");
	map.put("3","Lucy");
//	Collection values = map.values();
//	Set entrySet = map.entrySet();
//	Set entrySet = map.entrySet();
//	Collection values = map.values();
	Set keySet = map.keySet();
	Iterator it = keySet.iterator();
	while(it.hasNext()) {
//		Map.Entry entry = (Map.Entry) (it.next());
//		Object key = entry.getKey();
//		Object value = entry.getValue();
		Object key = it.next();
		Object Value = map.get(key);
		System.out.println(key+":"+Value);
	}
	}
}
 