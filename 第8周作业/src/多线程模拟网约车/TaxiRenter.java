package 多线程模拟网约车;

public class TaxiRenter implements Runnable{
private TaxiBase taxiBase;
	
	public TaxiRenter(TaxiBase taxiBase){
		this.taxiBase = taxiBase;
	}
	
	public void run() {
		while(true) {
			taxiBase.go();
		}
	}
}
