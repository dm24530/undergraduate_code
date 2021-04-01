//定义YieldThread类继承Thread类
public class YieldThread extends Thread{
	//定义一个有参的构造方法
	public YieldThread(String name) {
		super(name);  //调用父类的构造方法
	}
	public void run() {
		for(int i=0;i<5;i++) {
			System.out.println(Thread.currentThread().getName()+"---"+i);
			if(i==3) {
				System.out.println("线程让步:");
				Thread.yield();
			}
		}
	}
}
