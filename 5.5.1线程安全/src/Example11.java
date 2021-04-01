
public class Example11 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SaleThread saleThread = new SaleThread();    //创建saleThread对象
		//创建并开启四个线程
		new Thread(saleThread,"线程一").start();
		new Thread(saleThread,"线程二").start();
		new Thread(saleThread,"线程三").start();
		new Thread(saleThread,"线程四").start();
	}

}
