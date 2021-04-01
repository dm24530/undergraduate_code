
public class TicketWindow extends Thread{
	
	private int tickets = 10;
	public void run(){
		while(true) {
		if(tickets > 0) {
			Thread th = Thread.currentThread();
			String th_name = th.getName();
			System.out.println(th_name + "Ö¸¶¨" + tickets);
			tickets--;
		}
		else
			break;
	}
	}
}
