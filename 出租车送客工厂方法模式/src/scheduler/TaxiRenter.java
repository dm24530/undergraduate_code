package scheduler;

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
