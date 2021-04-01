package 租赁影片;

import java.util.Enumeration;
import java.util.Vector;

public class Customer {
	//定义name为字符串型
	private String _name;
	//Vector类可以实现可增长的对象数组
	private Vector _rentals = new Vector();
	//将获得的name存入_name中
	public Customer (String name) {
		_name = name;
	};
	//租金元素？？？
	public void addRental (Rental arg) {
		_rentals.addElement(arg);
	}
	//获取电影名字并返回
	public String getName() {
		return _name;
	};

public String statement() {
	double totalAmount = 0;
	int frequentRenterPoints = 0;
	Enumeration rentals = _rentals.elements();
	String result = "Rentals Record for" + getName() + "\n";
	//获取元素
	while (rentals.hasMoreElements()) {
		//double thisAmount = 0;
		Rental each = (Rental) rentals.nextElement();
		frequentRenterPoints += each.getFrequentRenterPoints();
	    //thisAmount = each.getCharge();
	
		//dentermine amounts for each line（每行的dentermine数量）
		
		/*
		//常客积分计算
		//add frequent renter points
		frequentRenterPoints ++;
		//add bonus for a two day new release rental
		if((each.getMovie().getPriceCode() == Movie.NEW_RELEASE) && 
				each.getDaysRented() > 1) frequentRenterPoints ++;
		*/
		
	//	frequentRenterPoints += each.getFrequentRenterPoints();
		//show figures for this rental
		result += "\t" + each.getMovie().getTitle() + "\t" +String.valueOf(each.getCharge()) + "\n";
		totalAmount += each.getCharge();
	}
	// add footer lines
	result += "Amount owed is :" + String.valueOf(getTotalCharge()) + "\n";
	result += "You earned " + String.valueOf(getTotalFrequentRenterPoints()) + 
			" frequent renter points";
	return result;
  }

private int getTotalFrequentRenterPoints() {
	int result = 0;
	Enumeration rentals = _rentals.elements();
	while(rentals.hasMoreElements()) {
		Rental each = (Rental) rentals.nextElement();
		result += each.getCharge();
	}
	return result;
}

private double getTotalCharge() {
	// TODO Auto-generated method stub
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

/*
private double amountFor(Rental aRental) {
	
	double result = 0;
	
	switch (aRental.getMovie().getPriceCode()) {
		case Movie.REGULAR:
			result += 2;
			if(aRental.getDaysRented() > 2)
				result += (aRental.getDaysRented() - 2) * 1.5;
			break;
		case Movie.NEW_RELEASE:
			result += aRental.getDaysRented() * 3;
			break;
		case Movie.CHILDRENS:
			result += 1.5;
			if(aRental.getDaysRented() > 3)
				result += (aRental.getDaysRented() - 3) * 1.5;
			break;
		}
	return result;
}
*/
}