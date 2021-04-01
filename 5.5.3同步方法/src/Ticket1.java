
public class Ticket1 implements Runnable{
	private int tickets=10;
	public void run() {
		while(true) {
			saleTicket();
			if(tickets<=0) {
				break;
			}
		}
	}
	//定义一个同步方法saleTicket()
	private synchronized void saleTicket() {
		if(tickets>0) {
			try {
				Thread.sleep(10);
			}catch(InterruptedException e) {
				e.printStackTrace();
			}
			System.out.println(Thread.currentThread().getName()+"---卖出的票"+tickets--);
		}
	}
}
