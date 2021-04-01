package 出租车接乘客;

public class TicketWindow implements Runnable{

	 int tickets = 100;
	 int[] arr=new int[tickets];
	 
		public void run(){
			while(true) {
			if(tickets > 0) {
				Thread th = Thread.currentThread();
				String th_name = th.getName();
				System.out.println(th_name + "正在下载第" + tickets-- + "份文件");
				
			}
			else
				break;
		}
		}
}
