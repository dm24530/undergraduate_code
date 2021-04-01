//定义Ticket1实现Runnable接口
public class SaleThread implements Runnable{

	private int tickets = 10;
	public void run() {
		while (tickets>0) {
			try {
				Thread.sleep(10);
			}catch (InterruptedException e) {
				e.printStackTrace();
			}
			System.out.println(Thread.currentThread().getName()+"---卖出的票"+tickets--);
		}
	}
}
