package 租赁影片;
import java.util.Enumeration;
import java.util.Vector;

public class Customer {

	//定义name为字符串型
		private String _name;
		//Vector类可以实现可增长的对象数组
		private Vector _rentals = new Vector();
		
		public Customer (String name) {
			_name = name;
		};
		public void addRental (Rental arg) {
			_rentals.addElement(arg);
		}
		public String getName() {
			return _name;
		};

public String statement() {
	int frequentRenterPoints = 0;
	
	Enumeration rentals = _rentals.elements();
	String result = "Rentals Record for" + getName() + "\n";
	//获取元素
	while (rentals.hasMoreElements()) {
		Rental each = (Rental) rentals.nextElement();

		//show figures for this rental
		result += "\t" + each.getMovie().getTitle() + "\t" +
		     String.valueOf(each.getCharge()) + "\n";
	}
	// add footer lines
	result += "Amount owed is :" + String.valueOf(getTotalCharge()) + "\n";
	result += "You earned " + String.valueOf(getTotalFrequentRenterPoints()) + 
			" frequent renter points";
	return result;
    }
private int getTotalFrequentRenterPoints() {
	// TODO Auto-generated method stub
	int result = 0;
	Enumeration rentals = _rentals.elements();
	while(rentals.hasMoreElements()) {
		Rental each = (Rental) rentals.nextElement();
		result += each.getFrequentRenterPoints();
	}
	return result;
}
private double getTotalCharge() {
	double result = 0;
	Enumeration rentals = _rentals.elements();
	while(rentals.hasMoreElements()) {
		Rental each = (Rental) rentals.nextElement();
		result += each.getCharge();
	}
	return result;
}
private double amountFor(Rental aRental) {
	       return aRental.getCharge();
    } 
}