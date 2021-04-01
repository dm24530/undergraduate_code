import car.*;
import carfactory.*;
import scheduler.TaxiBase;
import scheduler.TaxiProvider;
import scheduler.TaxiRenter;
import utility.XMLUtility;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TaxiBase taxiBase = new TaxiBase();
		TaxiRenter taxiRenter = new TaxiRenter(taxiBase);
		TaxiProvider taxiProvider = new TaxiProvider(taxiBase);
		new Thread(taxiRenter).start();
		new Thread(taxiProvider).start();
	}
		
}
