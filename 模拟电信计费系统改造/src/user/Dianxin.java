package user;

public class Dianxin implements User{

	@Override
	public double feilv() {
		// TODO Auto-generated method stub
		//费率为每分钟0.2元
		return (double) 0.2;
	}

	@Override
	public String name() {
		// TODO Auto-generated method stub
		//营业商的名字为电信公司
		return "电信公司为您服务";
	}

}
