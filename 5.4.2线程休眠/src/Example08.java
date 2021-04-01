			
public class Example08 {

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		//创建一个线程
		new Thread(new SleepThread()).start();
		for(int i=1;i<=10;i++) {
			if(i==5) {
				Thread.sleep(2000);     //当前线程休眠2秒
			}
			System.out.println("主线程正在输出："+i);
			Thread.sleep(500);     //当前线程休眠500毫秒
		}

	}

}
