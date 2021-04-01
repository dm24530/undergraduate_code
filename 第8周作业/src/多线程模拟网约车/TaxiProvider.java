package 多线程模拟网约车;

public class TaxiProvider implements Runnable{

private TaxiBase taxiBase;
	
	public TaxiProvider(TaxiBase taxiBase){
		this.taxiBase = taxiBase;
	}
	
	public void run() {
		while(true)
		{
			taxiBase.come();
		}
	}
}

