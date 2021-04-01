//定义SleepThread类实现Runnable接口
public class SleepThread implements Runnable{
	public void run() {
		for(int i=1;i<=10;i++) {
			if(i==3) {
				try {
					Thread.sleep(2000);    //当前线程休眠2秒
				}catch(InterruptedException e) {
					e.printStackTrace();
				}
			}
			System.out.println("线程一正在输入："+i);  
			try {
				Thread.sleep(500);   //当前线程休眠500毫秒
			}catch(Exception e) {
				e.printStackTrace();
			}
		}
	}
}
