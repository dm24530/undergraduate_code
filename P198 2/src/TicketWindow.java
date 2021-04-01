
public class TicketWindow implements Runnable{

	 int tickets = 80;
		public void run(){
			while(true) {
			if(tickets > 0) {
				Thread th = Thread.currentThread();
				String th_name = th.getName();
				System.out.println(th_name + "正在分发" + tickets + "份作业");
				tickets--;
			}
			else
				break;
		}
		}
}
