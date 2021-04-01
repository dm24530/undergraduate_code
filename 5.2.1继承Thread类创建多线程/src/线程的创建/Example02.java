package 线程的创建;

public class Example02 {
	
	public static void main(String[] args){
		MyThread myThread = new MyThread();
		myThread.start();
		while (true){
			System.out.println("Main()方法在运行");
		}
	}
}

