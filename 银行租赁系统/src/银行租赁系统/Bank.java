package 银行租赁系统;

import java.util.Scanner;

public class Bank {
	int account;
	private static User user;
	
	public static void main(String[] args) {
		Bank b = new Bank();
		//DBUtils dbU = DBUtils.getInstance();
		System.out.println("注册：1" + "\t" + "登陆:2" + "\t" );
		Scanner in = new Scanner(System.in);
		String s = in.nextLine();
		if("1".equals(s)) { 
		b.register();
		b.save();
		//dbU.update();
		b.login();
		b.operate();
		}else {
			b.login();
			b.operate();
		}
		
		
	}
	
	/*
	 * 账户金额存入，取出和查询操作
	 */
	public void operate() {
		Bank b = new Bank();
		while(true) {
			System.out.println("请选择您要进行的操作类型，按回车结束");
			System.out.println("存款：1" + "\t" + "取款:2" + "\t" + "查询余额：3" + "\t" + "退出：0");
			Scanner in = new Scanner(System.in);
			String s = in.nextLine();    //输入操作类型
			if("1".equals(s) || "2".equals(s)) {
				int num = 0;
				try {
					if("1".equals(s)) {
					System.out.println("请输入存款金额:");
					num = Integer.parseInt(in.nextLine());
					}else {
						System.out.println("请输入取款金额:");
						num = Integer.parseInt(in.nextLine());
					}
				}catch(Exception e) {
					System.out.println("金额输入错误！");
					continue;
				}
				switch (s) {
				case "1": //存款操作
				    b.income(num);
				    break;
				case "2": //取款操作
				    b.takeout(num);
				    break;
				}
			}else if("3".equals(s)) {
				b.show();
			}else if("0".equals(s)) {
				System.out.println("退出系统");
				return;
			}else {
				System.out.println("请输入0~3之间的数字选择相关的操作！");
			}
		}
	}
	/*
	 * 用户登陆网上银行
	 */
	public void login() {
		DBUtils dbutils = DBUtils.getInstance();
		System.out.println("欢迎进入网上银行！");
		
		while(true) {
			Scanner in = new Scanner(System.in); //键盘录入
			System.out.println("请输入银行卡号：");
			String cardId = in.nextLine();
		System.out.println("请输入银行卡密码:");
	 
		String cardPwd = in.nextLine()+"7716496";
		user = dbutils.getUser(cardId);
		//登陆
		if(dbutils.getUsers().containsKey(cardId)
				&& user.getCardPwd().equals(cardPwd)) {
			if(user.getSex().equals("男")) {
				System.out.println("登陆成功！欢迎" + user.getUserName() + "先生");
			    break;
			}else {
				System.out.println("登陆成功！欢迎" + user.getUserName() + "女士");
				break;
			}
		}else {
			System.out.println("银行卡号或密码错误！");
			continue;
		    }
	    }
    }
	/*
	 * 存款
	 */
	public void income(int num) {
		account = user.getAccount() + num;
		user.setAccount(account);
		System.out.println("存入金额" + num + "元成功！");
	}
	/*
	 * 取款
	 */
	public void takeout(int num) {
		if(user.getAccount() >= num) {
			account = user.getAccount() - num;
			user.setAccount(account);
			System.out.println("取出金额" + num +"元成功！");
		}else {
			System.out.println("余额不足，取款失败！");
		}
	}
	/*
	 * 查询余额
	 */
	public void show() {
		account = user.getAccount();
		System.out.println("账户总金额为" + account +"元");
	}
	private void register() {
		User u = new User();
		Scanner scanner = new Scanner(System.in);
		System.out.println("输入卡号：");
		u.setCardId(scanner.nextLine());
		System.out.println("输入密码：");
		u.setCardPwd(scanner.nextLine()+"7716496");
		System.out.println("输入用户名：");
		u.setUserName(scanner.nextLine());
		System.out.println("输入手机号：");
		u.setCall(scanner.nextLine());
		System.out.println("输入性别：");
		u.setSex(scanner.nextLine());
		System.out.println("输入余额:");
		u.setAccount(scanner.nextInt());
		DBUtils dbUtils = DBUtils.getInstance();
		dbUtils.addUser(u);
	}

	private void save() {
		DBUtils dbutil = DBUtils.getInstance();
		dbutil.update();
	}
}