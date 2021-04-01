package user;

public class Liantong implements User {

	@Override
	public double feilv() {
		// TODO Auto-generated method stub
		//费率为每分钟0.18元
		return (double) 0.18;
	}

	@Override
	public String name() {
		// TODO Auto-generated method stub
		//营业商是联通公司
		return "联通公司为您服务";
	}

}
