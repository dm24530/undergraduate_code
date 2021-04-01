
public class Example14 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//创建两个DeadLockThread对象
		DeadLockThread d1=new DeadLockThread(true);
		DeadLockThread d2=new DeadLockThread(false);
		//创建并开启两个线程
		new Thread(d1,"Chinese").start();
		new Thread(d2,"American").start();
	}

}
