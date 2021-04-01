package 银行租赁系统;

public class User {
	    //电话号码
		private String call;
		//余额
		private int account;
		//用户名
		private String userName;
		//密码
		private String cardPwd;
		//卡号
		private String cardId;
		//性别
		private String sex;
		
		public void setCall(String call){
			this.call = call;
		}
		public String getCall(){
			return call;
		}
		
		public void setAccount(int account){
			this.account = account;
		}
		public int getAccount(){
			return account;
		}
		
		public void setUserName(String userName){
			this.userName = userName;
		}
		public String getUserName(){
			return userName;
		}
		
		public void setCardPwd(String cardPwd){
			this.cardPwd = cardPwd;
		}
		public String getCardPwd(){
			return cardPwd;
		}
		
		public void setCardId(String cardId){
			this.cardId = cardId;
		}
		public String getCardId(){
			return cardId;
		}
		public void setSex(String sex) {
			this.sex = sex;
		}
		public String getSex() {
			return sex;
		}

}
