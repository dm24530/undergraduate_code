package 模拟多线程分段下载文件;

public class Example {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
TicketWindow tw = new TicketWindow();
		
		new Thread(tw,"线程1").start();
		new Thread(tw,"线程2").start();
		new Thread(tw,"线程3").start();
		new Thread(tw,"线程4").start();
		new Thread(tw,"线程5").start();
		
	}

}
