package factory;
import user.*;
import 改造.*;
public class YidongFactory implements Factory{
	//		创建移动公司
	public User produceuser() {
		return new Yidong();
	}
}
