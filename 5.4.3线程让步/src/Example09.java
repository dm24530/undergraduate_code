
public class Example09 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//创建两个线程
		Thread t1 = new YieldThread("线程 A");
		Thread t2 = new YieldThread("线程 B");
		//开启两个线程
		t1.start();
		t2.start();
	}

}
