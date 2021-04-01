
public class Example07 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//创建两个线程
		Thread minPriority = new Thread(new MinPriority(),"优先级较低的线程");
		Thread maxPriority = new Thread(new MaxPriority(),"优先级较高的线程");
		minPriority.setPriority(Thread.MIN_PRIORITY);     //设置线程优先级为1
		maxPriority.setPriority(10);       //设置线程优先级为10
		//开启两个线程
		maxPriority.start();
		minPriority.start();
	}

}
