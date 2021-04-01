
public class TicketWindow extends Thread{
	
	private int tickets = 100;
	public void run(){
		while(true) {
		if(tickets > 0) {
			Thread th = Thread.currentThread();
			String th_name = th.getName();
			System.out.println(th_name + "正在售票" + tickets + "张票");
			tickets--;
		}
		else
			break;
	}
	}
}
