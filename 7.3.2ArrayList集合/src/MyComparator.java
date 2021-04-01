import java.util.*;

public class MyComparator implements Comparator{
    @Override
	public int compare(Object obj1,Object obj2) {
		// TODO Auto-generated method stub
		 String id1 = (String) obj1;
	    String id2 = (String) obj2;
    	return id2.compareTo(id1);
	}
	
}
