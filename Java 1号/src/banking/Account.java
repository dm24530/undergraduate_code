package banking;

public class Account {

	private double balance;//余额
	
	public Account(double init_balance) {
		this.balance = init_balance;
	}
	
	//得到余额
	public double getBalance(){
		return balance;
	}
	
	//存钱
	public void deposit(double money){
		balance +=money;
	}
	
	public void withdraw(double money){
		balance -=money;
	}
	
	public static void main(String[] args) {
		System.out.println("创建余额为500.00的帐户 ");
		Account a = new Account(500.00);
		
		System.out.println("提取150.00 ");
		a.withdraw(150.00);
		System.out.println("存款22.50 ");
		a.deposit(22.50);
		System.out.println("提取47.62     ");
		a.withdraw(47.62);
		System.out.println("账户余额"+a.getBalance());
	}
}
