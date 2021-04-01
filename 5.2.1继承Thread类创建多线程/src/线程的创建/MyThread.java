package 线程的创建;

class MyThread extends Thread{
	public void run() {
	while (true){
		System.out.println("MyThread类的方法run()正在运行");
	}
}
}