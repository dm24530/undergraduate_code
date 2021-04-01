
public class Example{

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TicketWindow tw = new TicketWindow();
		
		new Thread(tw,"老师1").start();
		new Thread(tw,"老师2").start();
		new Thread(tw,"老师3").start();
	}

}
