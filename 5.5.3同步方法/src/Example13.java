
public class Example13 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Ticket1 ticket = new Ticket1();
		//创建并开启四个线程
		new Thread(ticket,"线程一").start();
		new Thread(ticket,"线程二").start();
		new Thread(ticket,"线程三").start();
		new Thread(ticket,"线程四").start();
	}

}
