
public class Example10 {

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		//创建线程
		Thread t = new Thread(new EmergencyThread(),"线程一");
		t.start();   //开启线程
		for(int i=1;i<6;i++) {
			System.out.println(Thread.currentThread().getName()+"输入："+i);
			if(i==2) {
				t.join();   //调用join()方法
			}
			Thread.sleep(500);    //线程休眠500毫秒
		}
	}

}
