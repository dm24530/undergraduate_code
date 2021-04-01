
public class Example06 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("main线程是后台程序？"+Thread.currentThread().isDaemon());
		DamonThread dt = new DamonThread();         //创建一个DamonThread对象dt
		Thread t= new Thread(dt,"后台线程");         //创建线程t共享dt资源
		System.out.println("t线程默认是后台线程吗？"+t.isDaemon());        //判断是否为后台线程
		t.setDaemon(true);           //将t设置为后台线程
		t.start();              //调用star的方法开启线程t
		for(int i=0;i<10;i++) {
			System.out.println(i);
		}
		
	}

}
