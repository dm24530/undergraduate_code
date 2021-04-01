
public class Example12 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Ticket1 ticket = new Ticket1();    //创建saleThread对象
		//创建并开启四个线程
		new Thread(ticket,"线程一").start();
		new Thread(ticket,"线程二").start();
		new Thread(ticket,"线程三").start();
		new Thread(ticket,"线程四").start();
	}

}
//定义Ticket1实现Runnable接口
class Ticket1 implements Runnable{
	private int tickets = 10;
	Object lock = new Object();    //定义任意一个对象，用作同步代码的锁
	public void run() {
		while (true) {
			synchronized(lock) {      //定义同步代码块
			try {
				Thread.sleep(10);
			}catch (InterruptedException e) {
				e.printStackTrace();
			}
			if(tickets>0) {
			System.out.println(Thread.currentThread().getName()+"---卖出的票"+tickets--);
		        }else {
		        	break;
		        }
			}
	    }
	}
}

