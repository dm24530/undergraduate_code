package banking;

public class Customer {
	
	private String firstName;
	private String lastName;
	private Account account;
	
	public Customer(String firstName, String lastName) {
		super();
		this.firstName = firstName;
		this.lastName = lastName;
	}
	
	public String getFirstName(){
		return firstName;
	}
	
	public String getLastName() {
		return lastName;
	}
	
	public void setAccount(Account account){
		this.account = account;
	}
	
    public Account getAccount(){
		return account;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Account a = new Account(500.00);
		System.out.println("创建客户乔碧螺");
		System.out.println("用500.00的余额创建她的账户");
		System.out.println("提取150.00 ");
		a.withdraw(150.00);
		System.out.println("存款22.50 ");
		a.deposit(22.50);
		System.out.println("取款47.62客户[乔碧螺]     ");
		a.withdraw(47.62);
		System.out.println("有"+a.getBalance()+"的余额");
	}

}
