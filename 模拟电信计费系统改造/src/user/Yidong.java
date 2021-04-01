package user;

public class Yidong implements User{

	@Override
	public double feilv() {
		// TODO Auto-generated method stub
		//费率为每分钟0.22元
		return (double) 0.22;
	}

	@Override
	public String name() {
		// TODO Auto-generated method stub
		//营业商是移动公司
		return "移动公司为您服务";
	}

}
