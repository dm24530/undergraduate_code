package factory;
import user.*;
import 改造.*;
public class DianxinFactory implements Factory{
	//创建电信公司
	public User produceuser() {
		return new Dianxin();
	}
}
