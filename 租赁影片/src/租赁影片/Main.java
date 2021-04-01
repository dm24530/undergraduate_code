package 租赁影片;

public class Main {
	public static void main(String[] args) {
		
		Customer customer = new Customer("李一");
		
		Rental rental1 = new Rental(new Movie("梦回大唐",1),10);
		Rental rental2 = new Rental(new Movie("虎虎生威",2),5);
	    customer.addRental(rental1);
		customer.addRental(rental2);
		System.out.println(customer.statement());
	}
}